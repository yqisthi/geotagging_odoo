from odoo import api, fields, models, _
from odoo import http
from odoo.http import request


class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Float(
        string='Longitude', digits=(16, 5))
    longitude = fields.Float(string='Longitude', digits=(16, 5))

    @api.model
    def _geo_localize(self):
        geo_obj = self.env['base.geocoder']
        geo_obj.ip('me')
