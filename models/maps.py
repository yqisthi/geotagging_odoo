from odoo import api, fields, models, _


class Maps(models.Model):
    _name = "maps"
    _inherit = []
    _description = "Maps"

    name = fields.Char(String="Location")
    latitude = fields.Float(String="latitude", digits=(16, 5))
    longitude = fields.Float(String="longitude", digits=(16, 5))
