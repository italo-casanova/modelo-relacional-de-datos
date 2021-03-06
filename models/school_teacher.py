from odoo import fields, models

class Teacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string =  "Nombre del profesor")
    profile = fields.Text(string = "profile")
    subject_ids = fields.One2Many("school.subject", "teacher_id", string = "subject")
