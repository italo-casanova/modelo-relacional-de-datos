from odoo import api, fields, models

class Teacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string =  "name")
    profile = fields.Text(string = "profile")
    subject_ids = fields.One2Many("school.student", "teacher_id", string = "subject")
