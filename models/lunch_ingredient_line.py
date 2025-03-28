from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LunchIngredientLine(models.Model):
    _name = 'lunch.ingredient.line'
    _description = 'Lunch Ingredient Line'

    parent_id = fields.Many2one('lunch.product', string='Product', required=True, ondelete='cascade')
    ingredient_name = fields.Char(string='Ingredient Name', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    uom = fields.Selection([
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
    ], string='Unit of Measure', default='kg', required=True)

    @api.constrains('quantity')
    def _check_quantity(self):
        for line in self:
            if line.quantity <= 0:
                raise ValidationError("Quantity must be greater than 0.")
