from odoo import models, fields, api
from odoo.exceptions import UserError

class ResetWizard(models.TransientModel):
    _name = 'library.resetwizard'
    _description = 'Wizard to reset a borrow'

    borrower_id = fields.Many2one('library.borrower', string='Borrower', required=True)
    
    

    def reset_borrowings(self):
            if not self.borrower_id:
                raise UserError("Please select a borrower to reset borrowings.")

            loans = self.env['library.loan'].search([('borrower_id', '=', self.borrower_id.id)])
            loans.unlink()