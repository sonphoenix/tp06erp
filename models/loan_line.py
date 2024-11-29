from odoo import models, fields

class LoanLine(models.Model):
    _name = 'library.loan.line'
    _description = 'Loan Line'

    loan_id = fields.Many2one('library.loan', string='Loan')
    book_id = fields.Many2one('library.book', string='Book')
    isbn = fields.Char(related='book_id.isbn', store=True, readonly=True)
    language = fields.Selection(related='book_id.language', store=True, readonly=True)
    page_count = fields.Integer(related='book_id.page_count', store=True, readonly=True)
