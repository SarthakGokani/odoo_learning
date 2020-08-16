from odoo import api, fields, models

class MyEmployee(models.Model):

    _name = 'myemployee.myemployee'
    _descripation = 'my employees'

    photos = fields.Binary(string='Profile Picture')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    dob = fields.Date(string='Birth Date(DOB)', help='22/08/1998')
    contact_no = fields.Char(string='Contact No.')
    email = fields.Char(string='Email')
    date_of_joining = fields.Date(string='Date Of Joining', help='04/11/2018')
    wages_type = fields.Selection([('salary', 'Salary'), ('hourlu', 'Hourly')], string = 'Wages Type')
    wages_or_salary = fields.Integer(string='Wages/Salary')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    hobbies = fields.Char(string='Hobbies')
    job_position = fields.Selection([('manager', 'Manager'), ('worker', 'Worker'), ('other', 'Other')], string='Job Position')
    status = fields.Selection([('interview_one', 'Interview One'), ('interview_two', 'Interview Two'), ('hired', 'Hired')], string='Status')


