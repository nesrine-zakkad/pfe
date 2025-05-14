from odoo import models, fields

class Session(models.Model):
    _inherit = 'event.event'

    is_session = fields.Boolean(string="Is Academic Year", default=False)
dissertation_ids = fields.One2many('pfe.dissertation', 'session_id', string="Dissertations")