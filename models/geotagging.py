from odoo import api, fields, models, _
from odoo import http
from odoo.http import request

class Geotagging(models.Model):
    _name = "geotagging"
    _inherit = []
    _description = "Geotagging"

    latitude = fields.Float("latitude")
    longitude = fields.Float("longitude")

    class GeolocationController(http.Controller):
        @http.route('/web_geolocation', type='http', auth='user', website=True)
        def web_geolocation(self, **kwargs):
            return """
                <script type="text/javascript">
                    $(document).ready(function() {
                        if ("geolocation" in navigator) {
                            navigator.geolocation.getCurrentPosition(function(position) {
                                var latitude = position.coords.latitude;
                                var longitude = position.coords.longitude;

                                $('input[name="latitude"]').val(latitude);
                                $('input[name="longitude"]').val(longitude);

                                console.log("latitude");
                                console.log(longitude);
                            });
                        } else {
                            console.log("Geolocation is not available.");
                        }
                    });
                </script>
            """
