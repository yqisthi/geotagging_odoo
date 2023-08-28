from odoo import api, fields, models, _
from odoo import http
from odoo.http import request

class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Float("latitude")
    longitude = fields.Float("longitude")


    def get_location_xml(self):
        return

    def get_location(self, coords):        
        self.latitude = coords.get('latitude')
        self.longitude = coords.get('longitude')
        return
