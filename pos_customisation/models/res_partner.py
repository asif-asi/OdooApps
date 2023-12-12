
from odoo import fields, models


class ResPartner(models.Model):
    """Add Customer Type selection field in partner form"""

    _inherit = "res.partner"

    customer_type = fields.Selection([
        ('potential', 'Potential'),
        ('loyal', 'Loyal'),
        ('impulse', 'Impulse')
    ], string="Customer Type")
