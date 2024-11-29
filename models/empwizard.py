from odoo import models, fields, api
from odoo.exceptions import UserError

class EmpWizard(models.TransientModel):
    _name = 'library.empwizard'
    _description = 'Wizard to add borrow records'

    borrower_id = fields.Many2one('library.borrower', string='Borrower', required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today, required=True, readonly=True)
    end_date = fields.Date(string='End Date', required=True)
    loan_line_ids = fields.Many2many('library.loan.line', string='Loan Lines')

    def add_borrow(self):
        borrow_record = self.env['library.loan'].create({
            'borrower_id': self.borrower_id.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'loan_line_ids': [(6, 0, self.loan_line_ids.ids)]
        })
        
        return {'type': 'ir.actions.act_window_close'}

    def reset_borrowings(self):
        if not self.borrower_id:
            raise UserError("Please select a borrower to reset borrowings.")

        loans = self.env['library.loan'].search([('borrower_id', '=', self.borrower_id.id)])
        loans.unlink()