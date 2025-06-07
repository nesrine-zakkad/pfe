from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError


class TopicWebsiteController(http.Controller):

    @http.route('/create_topic/', type='http', auth="user", website=True, csrf=True)
    def submit_topic_save(self, **post):
        title = post.get('title')
        description = post.get('description')
        tools = post.get('tools')
        raw_category_ids = request.httprequest.form.getlist('category_ids')

        error = None
        if not title:
            error = "Title is required."

        # Process category_ids: split between existing IDs and new tag names
        existing_ids = []
        new_names = []
        for value in raw_category_ids:
            if value.startswith('new:'):
                new_names.append(value[4:].strip())
            elif value.isdigit():
                existing_ids.append(int(value))

        # Create new tag records if needed
        new_tag_ids = []
        if new_names:
            for name in new_names:
                if name:
                    existing_tag = request.env['pfe.topic_category'].sudo().search([('name', '=ilike', name)], limit=1)
                    if existing_tag:
                        new_tag_ids.append(existing_tag.id)
                    else:
                        new_tag = request.env['pfe.topic_category'].sudo().create({'name': name})
                        new_tag_ids.append(new_tag.id)

        all_tag_ids = existing_ids + new_tag_ids

        if not error:
            try:
                employee = request.env.user.employee_id
                request.env['pfe.topic'].sudo().create({
                    'title': title,
                    'description': description,
                    'tools': tools,
                    'category_ids': [(6, 0, all_tag_ids)],
                    'supervisor_id': employee.id,


                })
                return request.redirect('/topic/submit/success')
            except Exception as e:
                error = "An error occurred while submitting the topic. Please try again."

        # If error: reload form with error message
        values = {
            'error': error,
            'category_ids': request.env['pfe.topic_category'].sudo().search([]),
        }
        return request.render('pfe.topic_submit_templateA', values)

    @http.route('/topic/submit/success', type='http', auth="user", website=True)
    def topic_submit_success(self):
        return request.render('pfe.topic_submit_success')
