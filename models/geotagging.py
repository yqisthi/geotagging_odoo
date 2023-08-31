from odoo import api, fields, models, _
from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError


class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Float("latitude", digits=(16, 5))
    longitude = fields.Float("longitude", digits=(16, 5))

    location_id = fields.Many2one('maps', String='location')

    isreadonly = fields.Boolean(String="is readonly?", compute='compare')

    lat = fields.Float(String="latitude", digits=(
        16, 5), related='location_id.latitude')
    lot = fields.Float(String="longitude", digits=(
        16, 5), related='location_id.longitude')

    def comparison(self):
        if self.latitude > self.lat:
            raise ValidationError(
                "Latitude asli lebih besar dari pada latitude palsu")
        else:
            raise ValidationError(
                "Latitude asli lebih kecil dari pada latitude palsu")

    @api.depends('lat')
    def compare(self):
        if self.lat > self.latitude and self.lot > self.longitude:
            self.isreadonly = True
        else:
            self.isreadonly = False
