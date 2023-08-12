from odoo import api, fields, models, _

class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Char("latitude")
    longitude = fields.Char("longitude")
