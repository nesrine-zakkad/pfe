from odoo import models, fields
class DissertationAvancement(models.Model):
    _name = 'pfe.dissertation.avancement'
    _description = 'Dissertation Progress'

    name = fields.Char(string="Progress Title", required=True)
    date = fields.Date(string="Date", required=True)
    #text html
    progress_percent = fields.Float(string="Progress (%)", required=True)
    dissertation_id = fields.Many2one('pfe.dissertation', string="Dissertation", ondelete='cascade')