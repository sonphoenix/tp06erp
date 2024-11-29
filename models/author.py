from odoo import models, fields, api
from odoo.exceptions import AccessError


class Author(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string='Last Name')
    first_name = fields.Char(string='First Name')
    birth_date = fields.Date(string='Birth Date')
    nationality = fields.Char(string='Nationality')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    book_ids = fields.One2many('library.book', 'author_id', string='Books')

    @api.model
    def create(self, vals):
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to create records.")
        return super(Author, self).create(vals)

    def write(self, vals):
        # Prevent writing if the user belongs to 'group_library_secretary'
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to update records.")
        return super(Author, self).write(vals)

    def unlink(self):
        # Prevent deletion if the user belongs to 'group_library_secretary'
        if self.env.user.has_group('my_library.group_library_secretary'):
            raise AccessError("You do not have permission to delete records.")
        return super(Author, self).unlink()