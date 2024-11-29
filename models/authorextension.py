from odoo import models, fields

class AuthorExtension(models.Model):
    _inherit = 'library.author'

    photo = fields.Binary(string='Photo')  
