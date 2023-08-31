odoo.define('geotagging_odoo.geo', function (require) {
  "use strict";

  odoo.define('geotagging_odoo.geolatlong', function (require) {
    "use strict";

    var rpc = require('web.rpc');

    function sendDataToServer(data) {
      return rpc.query({
        model: 'geotagging_odoo', // Replace with your model name
        method: 'write', // Specify the appropriate method name
        args: [[recordId], data], // Provide the record ID and the data to inject
      });
    }

    return {
      sendDataToServer: sendDataToServer,
    };
  });
});