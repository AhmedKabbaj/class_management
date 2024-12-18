from odoo import models, fields, api, _
from ..utils import get_school_year



class Student(models.Model):
    """Tutoring center student"""
    _name = "class.student"
    _description = __doc__
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "absences_cound desc"

    name = fields.Char(string="Nom et prenom")
    birthday = fields.Date(default=lambda self: fields.Date.today())
    phone = fields.Char('Telephone')
    group_id = fields.Many2one("class.group", string="Groupe")
    absences_cound = fields.Integer("Nombre d'absences", compute="_compute_absences_count", store=True)

    @api.depends("group_id.absence_ids")
    def _compute_absences_count(self):
        for rec in self:
            absences_count = rec.group_id.absence_ids.search([('student_id', '=', rec.id)]).__len__()
            rec.absences_cound = absences_count