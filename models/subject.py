from odoo import api, fields, models

class Subject(models.Model):
    _name = "school.Subject"

    name = fields.Char(string = "name")
    credits = fields.Integer()
    max_students = fields.Integer()
    active = fields.Boolean(string = "Active Subject")
    students_id = fields.Many2Many("school.student", "subject_id", string = "students")
    teacher_id = fields.Many2One("school.teacher", "subject_ids",string = "teacher")

