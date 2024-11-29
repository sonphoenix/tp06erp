from odoo import models, fields
from odoo import models, fields, api
from odoo.exceptions import AccessError

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    title = fields.Char(string='Title')
    language = fields.Selection([('fr', 'French'), ('ar', 'Arabic'), ('en', 'English')], string='Language')
    isbn = fields.Char(string='ISBN')
    page_count = fields.Integer(string='Page Count')
    cover_image = fields.Binary(string='Cover Image')
    author_id = fields.Many2one('library.author', string='Author')
    loan_line_ids = fields.One2many('library.loan.line', 'book_id', string='Loan Lines')
    
    @api.model
    def create(self, vals):
        # Prevent creation if the user belongs to 'group_library_secretary'
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to create records.")
        return super(Book, self).create(vals)

    def write(self, vals):
        # Prevent writing if the user belongs to 'group_library_secretary'
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to update records.")
        return super(Book, self).write(vals)

    def unlink(self):
        # Prevent deletion if the user belongs to 'group_library_secretary'
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to delete records.")
        return super(Book, self).unlink()
