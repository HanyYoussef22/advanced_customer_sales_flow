from odoo import models ,fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sector=fields.Selection(
        [
            ('public_sector', 'Public Sector'),
            ('private_sector', 'Private Sector'),
            ('government', 'Government'),
            ('education', 'Education'),
            ('healthcare', 'Healthcare'),
            ('other', 'Other')
        ],string="Sector",)

    loyalty_score = fields.Integer(string="Loyalty Score", default=0)

  account_manager_id = fields.Many2one(
         'res.users',
         string="Account Manager",
         domain=[('share', '=', False)],  # only regular users, not portal or public users (Internal User)
     )
