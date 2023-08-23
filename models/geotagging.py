from odoo import api, fields, models, _
import requests
from odoo.exceptions import UserError, ValidationError


class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Char("latitude")
    longitude = fields.Char("longitude")
    ip_address_field = fields.Char("IP Address")

    @api.model
    def get_coordinates_by_ip(self, ip_address):
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            latitude = data['lat']
            longitude = data['lon']
            return {'latitude': latitude, 'longitude': longitude}
        else:
            return {'latitude': None, 'longitude': None}

    # this metode is works!
    def action_get_coordinates_by_ip(self):
        for partner in self:
            ip_address = partner.ip_address_field  # Replace with the actual field name
            coordinates = partner.get_coordinates_by_ip(ip_address)
            partner.latitude = coordinates['latitude']
            partner.longitude = coordinates['longitude']
            raise ValidationError(_("Latitude: %s, Longitude: %s") % (
                partner.latitude, partner.longitude))

    # trigger when ip_address_field is changed
    @api.onchange('ip_address_field')
    def fill_coordinates_on_ip_change(self):
        if self.ip_address_field:
            coordinates = self.get_coordinates_by_ip(self.ip_address_field)
            self.latitude = coordinates['latitude']
            self.longitude = coordinates['longitude']
