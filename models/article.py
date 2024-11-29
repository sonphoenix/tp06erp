from odoo import fields, models

class Article(models.Model):
    _inherit = 'library.book'

    universite=fields.Char(string="universite")
    laboratoire=fields.Char(string="Laboratoire")
