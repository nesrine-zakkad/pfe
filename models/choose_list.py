from odoo import models, fields,api

class Choose(models.Model):
    _name = 'pfe.choose_list'
    _description = 'List of dissertation choices by group'

    group_id = fields.Many2one('pfe.sgroupe', string="Student's Group", required=True, ondelete='cascade')
    dissertation_id = fields.Many2one('pfe.dissertation', string="Dissertation", required=True)
    sequence = fields.Integer( compute='set_seq',string='sequence')

    _sql_constraints = [
        ('group_dissertation_sequence_unique',
         'UNIQUE(group_id, sequence)',
         'Each group must have a unique sequence for each dissertation choice.')
    ]

    @api.depends('dissertation_id')
    def set_seq(self):
        for record in self:
            if record.group_id:
                # نجيبو كل الاختيارات الخاصة بهاد المجموعة مرتبين حسب ID
                group_choices = self.search([('group_id', '=', record.group_id.id)], order='id')
                for index, rec in enumerate(group_choices, start=1):
                    rec.sequence = index
