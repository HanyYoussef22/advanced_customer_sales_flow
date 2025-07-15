from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    job_title = fields.Char(string="Job Title")

    performance_rating = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ], string="Performance Rating")


