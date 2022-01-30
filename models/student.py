from odoo import api, fields, models

class Studen(models.Model):
    _name = "school.student"

    name = fields.Char(string = "Student name") 
    birth_date = fields.Date()
    age = fields.Integer()
    final_exam_grade = fields.Float()
    subject_ids = fields.Many2Many("school.subject", "student_ids", string = "subjects")
