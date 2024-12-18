from odoo import models, fields, api, _

class Absence(models.Model):
    """Tutoring center service"""
    _name = "class.absence"
    _description = __doc__
    _order = "date desc"

    name = fields.Selection([('morning', 'matin'), ('after_noon', 'Après-midi')], default='morning')

    group_id = fields.Many2one("class.group", string="Groupe")
    student_id = fields.Many2one("class.student", string="Etudient")
    date = fields.Date(required=True)

    year = fields.Integer(string="Year", compute="_compute_year", store=True)
    month = fields.Integer(string="Month", compute="_compute_month", store=True)
    day = fields.Integer(string="Day", compute="_compute_day", store=True)

    @api.depends('date')
    def _compute_year(self):
        for record in self:
            record.year = record.date.year if record.date else 0

    @api.depends('date')
    def _compute_month(self):
        for record in self:
            record.month = record.date.month if record.date else 0

    @api.depends('date')
    def _compute_day(self):
        for record in self:
            record.day = record.date.day if record.date else 0