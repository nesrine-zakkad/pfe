from odoo import http
from odoo.http import request

class DissertationAvancementPortal(http.Controller):

    @http.route('/dissertation_avancement/', type='http', auth='user', website=True)
    def dissertation_avancement_form(self, **kw):
        return request.render('pfe.portal_dissertation_avancement_form')

    @http.route('/dissertation_avancement/', type='http', auth='user', methods=['POST'], website=True)
    def dissertation_avancement_submit(self, **post):
        try:
            request.env['pfe.dissertation.avancement'].sudo().create({
                'name': post.get('name'),
                'date': post.get('date'),
                'progress_percent': float(post.get('progress_percent', 0)),
                'dissertation_id': int(post.get('dissertation_id')),
            })
            return request.render('pfe.portal_dissertation_avancement_success')
        except Exception as e:
            return f"Error submitting progress: {e}"
