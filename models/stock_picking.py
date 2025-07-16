from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shipping_method = fields.Selection([
        ('self_pickup', 'Self Pickup'),
        ('representative', 'By Representative'),
        ('courier', 'Courier Company'),
    ], string="Shipping Method")

    delivery_notes = fields.Text(string="Delivery Notes")
