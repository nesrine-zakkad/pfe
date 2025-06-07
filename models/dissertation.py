from odoo import models, fields,exceptions

class Dissertation(models.Model):
    _name = 'pfe.dissertation'
    _description = 'Dissertation'
    _rec_name= 'title'

    title = fields.Char(string="Title", required=False)
    objectif = fields.Text(string="Objective")
    defense_date = fields.Date(string="Defense Date")
    document = fields.Binary(string="Attached Document")
    document_filename = fields.Char(string="Filename")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('rejected', 'Rejected'),
    ], string="State", default='draft', tracking=True)
    topic_id = fields.Many2one('pfe.topic', string="Topic", required=True, readonly=True)
    supervisor_id = fields.Many2one('hr.employee', string="Supervisor")
    avancement_ids = fields.One2many('pfe.dissertation.avancement', 'dissertation_id', string="Progress")
    group_id = fields.Many2one('pfe.sgroupe', string="Assigned Group")
    choose_id = fields.One2many('pfe.choose_list', 'dissertation_id', string="Choose_list", required=False)
    is_free = fields.Boolean(string="Is Free", default=True, help="Indicates if this dissertation is available for selection.")
    session_id = fields.Many2one('event.event', string="Session", domain="[('is_session', '=', True)]", help="The academic session to which this dissertation belongs.")
