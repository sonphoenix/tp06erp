from odoo import models, fields, api
from odoo.exceptions import AccessError

class Borrower(models.Model):
    _name = 'library.borrower'
    _description = 'Borrower'

    name = fields.Char(string='Name')
    first_name = fields.Char(string='First Name')
    birth_date = fields.Date(string='Birth Date')
    state = fields.Char(string='State')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    loan_count = fields.Integer(string='Loan Count', compute='_compute_loan_count')
    loan_ids = fields.One2many('library.loan', 'borrower_id', string='Loans')

    def _compute_loan_count(self):
        for record in self:
            record.loan_count = len(record.loan_ids)

    @api.model
    def create(self, vals):
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to create records.")
        return super(Borrower, self).create(vals)

    def write(self, vals):
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to update records.")
        return super(Borrower, self).write(vals)

    
