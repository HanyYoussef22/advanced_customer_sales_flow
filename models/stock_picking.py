from odoo import models, fields , api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shipping_method = fields.Selection([
        ('self_pickup', 'Self Pickup'),
        ('representative', 'By Representative'),
        ('courier', 'Courier Company'),
    ], string="Shipping Method")

    delivery_notes = fields.Text(string="Delivery Notes")

    @api.onchange('shipping_method')
    def _onchange_delivery_method(self):
        if self.shipping_method == 'self_pickup':
            self.delivery_notes = "Customer will pick up the order from our store."
        elif self.shipping_method == 'representative':
            self.delivery_notes = "Our representative will deliver the order."
        elif self.shipping_method == 'courier':
            self.delivery_notes = "A courier company will handle the delivery."