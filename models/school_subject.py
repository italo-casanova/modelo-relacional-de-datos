from odoo import fields, models

class Subject(models.Model):
    _name = "school.Subject"
    _description = "datos del curso"

    name = fields.Char(string = "name")
    credits = fields.Integer("creditos del cursos")
    max_students = fields.Integer("cantidad de estudiantes")
    active = fields.Boolean(string = "Active Subject")
    student_ids = fields.Many2Many("school.student", "subject_id", string = "students")
    teacher_id = fields.Many2One("school.teacher", "subject_ids",string = "teacher")

