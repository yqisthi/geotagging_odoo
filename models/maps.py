from odoo import api, fields, models, _


class Maps(models.Model):
    _name = "maps"
    _inherit = []
    _description = "Maps"

    location = fields.Char("Location")
