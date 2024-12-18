from odoo import models, fields, api, _
from ..utils import get_school_year



class Group(models.Model):
    """Tutoring center groups"""
    _name = "class.group"
    _description = __doc__
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nom")
    absence_ids = fields.One2many("class.absence", inverse_name="group_id", string="Absences")
    student_ids = fields.One2many("class.student", string="Etudients", inverse_name="group_id")