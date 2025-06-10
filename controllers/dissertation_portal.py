from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class PortalDissertations(CustomerPortal):

    @http.route(['/my/topics_dissertations'], type='http', auth="user", website=True)
    def portal_my_topics_dissertations(self, **kwargs):
        user = request.env.user
        topics = request.env['pfe.topic'].sudo().search([
            ('supervisor_id.user_id', '=', user.id),
            ('state', '=', 'validated')
        ])
        return request.render("your_module_name.portal_my_topics_with_dissertations", {
            'topics': topics
        })

    @http.route(['/my/dissertation/<int:diss_id>'], type='http', auth="user", website=True)
    def view_or_add_progress(self, diss_id, **kwargs):
        dissertation = request.env['pfe.dissertation'].sudo().browse(diss_id)
        return request.render("your_module_name.portal_dissertation_progress_form", {
            'dissertation': dissertation,
        })
    @http.route(['/my/dissertation/add_progress'], type='http', auth="user", methods=['POST'], website=True)
    def dissertation_add_progress(self, **post):
        request.env['pfe.avancement'].sudo().create({
            'title': post.get('title'),
            'percentage': float(post.get('percentage', 0)),
            'stage': post.get('stage'),
            'dissertation_id': int(post.get('dissertation_id')),
            'date': fields.Date.today(),
        })
        return request.redirect('/my/topics_dissertations')

