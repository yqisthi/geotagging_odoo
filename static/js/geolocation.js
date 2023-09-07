odoo.define("geotagging_odoo.geolocation", function (require) {
  "use strict";
  // Print out console if javascript file works
  console.log("LOADED");

  // Get Odoo View Controller and rpc
  var FormController = require("web.FormController");
  var rpc = require("web.rpc");

  // Odoo View Controller
  FormController.include({
    // Function executed on save
    saveRecord: function () {
      console.log("Saved!");
      var self = this;
      return this._super.apply(this, arguments).then(function () {
        // Get Current Record
        var recordID = self.model.get(self.handle, { raw: true }).res_id;

        // If record obtained, browser ask user for coordinates using GPS
        if (recordID) {
          navigator.geolocation.getCurrentPosition(function (position) {
            const { latitude, longitude } = position.coords;
            const coords = {
              latitude,
              longitude,
            };
            // Write record
            rpc
              .query({
                model: "geotagging",
                method: "write",
                args: [
                  [recordID],
                  { latitude: coords.latitude, longitude: coords.longitude },
                ],
              })
              .then(function () {
                // Success callback if needed
              })
              .catch(function (error) {
                // Error handling if needed
                console.error(error);
              });
          });
        }
      });
    },
  });

  return FormController;
});
