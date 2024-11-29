from odoo import models, fields, api
from odoo.exceptions import AccessError, ValidationError

class Loan(models.Model):
    _name = 'library.loan'
    _description = 'Loan'

    borrower_id = fields.Many2one('library.borrower', string='Borrower', required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today, required=True)
    end_date = fields.Date(string='End Date', required=True)
    returned = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Returned', default='no')
    loan_line_ids = fields.One2many('library.loan.line', 'loan_id', string='Loan Lines')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date >= record.end_date:
                raise ValidationError("La date de début doit etre avant la date de fin")

    @api.onchange('end_date')
    def _onchange_end_date(self):
        for record in self:
            if record.end_date == fields.Date.today():
                record.returned = 'yes'

    
