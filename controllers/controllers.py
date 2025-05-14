from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

class TopicPortal(http.Controller):

    @http.route('/create_topic/', type='http', auth='user', website=True)
    def topic_submit_form(self, **kw):
        return http.request.render('pfe.topic_submit_templateA', {})

    @http.route('/my/topic/submit/save', type='http', auth='user', methods=['POST'], website=True, csrf=True)
    def topic_submit_save(self, **post):
        try:
            employee = request.env.user.employee_id
            if not employee:
                raise ValidationError("This user is not linked to any employee.")

            request.env['pfe.topic'].sudo().create({
                'name': post.get('name'),
                'description': post.get('description'),
                'tools': post.get('tools'),
                'supervisor_id': employee.id,
            })
            return request.render('pfe.topic_submit_success', {})
        except ValidationError as e:
            return request.render('pfe.topic_submit_templateA', {
                'error': str(e),
            })
