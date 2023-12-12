from odoo import fields, models, api, _


class ResUsers(models.Model):
    """Add disable number pad boolean field in res users form"""

    _inherit = 'res.users'

    disable_numpad = fields.Boolean("Disable Numpad")
