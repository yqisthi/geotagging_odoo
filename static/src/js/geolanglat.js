odoo.define('geolanglat', function (require) {
  navigator.geolocation.getCurrentPosition(function (position) {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;

    var rpc = require('web.rpc');

    rpc.query({
      model: 'geotagging',
      method: 'write',
      args: [[1], { 'latitude': lat, 'longitude': lng }],
    }).then(function (result) {
      console.log(result);
    });
  });
});