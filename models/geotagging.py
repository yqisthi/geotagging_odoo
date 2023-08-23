from odoo import api, fields, models, _
# import geocoder


class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Char("latitude")
    longitude = fields.Char("longitude")

    # @api.model
    # def update_coordinates(self):
    #     # Fetch coordinates using geocoder or other methods
    #     location = geocoder.ip('me')

    #     if location.latlng:
    #         latitude, longitude = location.latlng
    #         self.write({'latitude': latitude, 'longitude': longitude})
