from odoo import fields, models

class Employee(models.Model):
    _inherit = 'hr.employee'

    date_debut = fields.Date(string="Start Date")
    nombre_annee = fields.Integer(string="Number of Years")
    num_retraite = fields.Char(string="Retirement Number")
    date_retraite = fields.Date(string="Retirement Date")
