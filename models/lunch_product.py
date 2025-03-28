from odoo import models, fields

class LunchProduct(models.Model):
    _inherit = 'lunch.product'

    ingredient_line_ids = fields.One2many(
        'lunch.ingredient.line',
        'parent_id',
        string='Ingredients'
    )
