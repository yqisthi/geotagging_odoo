from odoo import api, fields, models, _
from odoo import http
from odoo.http import request

class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Float("latitude")
    longitude = fields.Float("longitude")



