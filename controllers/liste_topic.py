from odoo import _, fields, http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class DissertationCustomerPortal(CustomerPortal):

    @http.route('/topics/list1', type='http', auth="user", website=True, sitemap=False)
    def display_topics(self, sortby=None, **kw):
        searchbar_sortings = {
            'name': {'label': _('Title'), 'order': 'name'},
            'supervisor': {'label': _('Supervisor'), 'order': 'supervisor_id.name'},
        }

        if not sortby:
            sortby = 'name'
        order = searchbar_sortings[sortby]['order']

        topics = request.env['pfe.topic'].sudo().search(
            [('state', '=', 'validated')], order=order)

        return request.render('pfe.topic_portal_list', {
            'topics': topics,
            'page_name': 'topic',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })