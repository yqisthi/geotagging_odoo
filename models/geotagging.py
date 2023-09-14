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

    isnear = fields.Selection([
        ('far', 'Far'),
        ('medium', 'Medium'),
        ('near', 'Near')
    ], string="How Far from Office?", compute='_compute_isnear', store=True)

    lat = fields.Float(String="latitude", digits=(
        16, 5), related='location_id.latitude')
    lot = fields.Float(String="longitude", digits=(
        16, 5), related='location_id.longitude')

    @api.onchange('isnear')
    def compare(self):
        if self.isnear != "near":
            self.isreadonly = True
        else:
            self.isreadonly = False

    @api.depends('latitude', 'longitude', 'location_id.latitude', 'location_id.longitude')
    def _compute_isnear(self):
        for record in self:
            latitude_diff = abs(record.lat - record.latitude)
            longitude_diff = abs(record.lot - record.longitude)

            if latitude_diff <= 10 and longitude_diff <= 10:
                record.isnear = 'near'
            elif 10 < latitude_diff <= 50 or 10 < longitude_diff <= 50:
                record.isnear = 'medium'
            elif latitude_diff > 50 or longitude_diff > 50:
                record.isnear = 'far'

    def comparing(self):
        latitude_diff = abs(self.lat - self.latitude)
        longitude_diff = abs(self.lot - self.longitude)
        error_message = f"latitude: {self.latitude}, longitude: {self.longitude}, lat: {self.lat}, lot: {self.lot}, latitude diff: {latitude_diff}, longitude diff : {longitude_diff}"

        raise ValidationError(error_message)


    @api.onchange('location_id')
    def _onchange_location_id(self):
        if self.location_id:
            self.latitude = self.latitude
            self.longitude = self.longitude
