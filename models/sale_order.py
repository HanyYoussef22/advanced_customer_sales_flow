from odoo import models, fields ,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_type = fields.Selection([
         ('new', 'New'),
         ('renewal', 'Renewal'),
         ('upgrade', 'Upgrade'),
    ], string='Order Type')

    delivery_deadline = fields.Date(string='Delivery Deadline')

