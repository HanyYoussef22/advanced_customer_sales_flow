from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sector = fields.Selection(
        [
            ('public_sector', 'Public Sector'),
            ('private_sector', 'Private Sector'),
            ('government', 'Government'),
            ('education', 'Education'),
            ('healthcare', 'Healthcare'),
            ('other', 'Other')
        ],
        string="Sector"
    )

    loyalty_score = fields.Integer(string="Loyalty Score", default=0)

    loyalty_level = fields.Selection([
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ], compute="_compute_loyalty_level", store=True)

    account_manager_id = fields.Many2one(
        'res.users',
        string="Account Manager",
        domain=[('share', '=', False)],  # Only internal users
    )

    @api.constrains('loyalty_score')
    def _check_loyalty_score(self):
        for record in self:
            if record.loyalty_score < 0:
                raise ValidationError("Loyalty score must be positive!")

    @api.onchange('sector')
    def _onchange_sector(self):
        if self.sector == 'government':
            self.loyalty_score = 100
        elif self.sector == 'healthcare':
            self.loyalty_score = 50
        else:
            self.loyalty_score = 10

    @api.depends('loyalty_score')
    def _compute_loyalty_level(self):
        for partner in self:
            if partner.loyalty_score >= 100:
                partner.loyalty_level = 'gold'
            elif partner.loyalty_score >= 50:
                partner.loyalty_level = 'silver'
            else:
                partner.loyalty_level = 'bronze'