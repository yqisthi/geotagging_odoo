function successCallback(position) {
  const { accuracy, latitude, longitude, altitude, heading, speed } =
    position.coords;

  // Use Odoo JavaScript API to set field values
  odoo.define("geotagging_odoo.geolocation", function (require) {
    "use strict";

    var FormController = require("web.FormController");
    var formController = new FormController();
    var model = "geotagging"; // Replace with your actual model name

    formController.widget = {};
    formController.widget.fields = {};

    console.log("latitude");
    console.log("longitude");

    // Set field values
    formController.widget.fields["latitude"] = latitude;
    formController.widget.fields["longitude"] = longitude;

    // Save the record
    formController.widget.saveRecord(model, null);
  });
}
