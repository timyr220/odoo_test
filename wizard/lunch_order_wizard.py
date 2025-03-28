from odoo import models, fields

class LunchOrderWizard(models.TransientModel):
    _name = 'lunch.order.wizard'
    _description = 'Wizard to print lunch orders by date range'

    date_from = fields.Date(string='Date from', required=True, default=fields.Date.today)
    date_to = fields.Date(string='Date to', required=True, default=fields.Date.today)

    def print_report(self):
        return self.env.ref('lunch_recipe.lunch_order_report').report_action(self)
