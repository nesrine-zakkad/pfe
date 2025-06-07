from odoo import http
from odoo.http import request

class DissertationAvancementPortal(http.Controller):
    @http.route('/dissertation_avancement/', type='http', auth='user', website=True)
    def dissertation_avancement_form(self, **kw):
        dissertations = request.env['pfe.dissertation'].sudo().search([])
        return request.render('pfe.portal_dissertation_avancement_form', {
            'dissertations': dissertations
        })

    @http.route('/dissertation_avancement/submit', type='http', auth='user', methods=['POST'], website=True)
    def dissertation_avancement_submit(self, **post):
        try:
            request.env['pfe.dissertation.avancement'].sudo().create({
                'name': post.get('name'),
                'date': post.get('date'),
                'progress_percent': post.get('progress_percent'),  # keep as string
                'dissertation_id': int(post.get('dissertation_id')),
                'stage': post.get('stage'),
            })
            return request.render('pfe.portal_dissertation_avancement_success')
        except Exception as e:
            return request.render('pfe.portal_error_template', {
                'error_message': str(e)
            })
