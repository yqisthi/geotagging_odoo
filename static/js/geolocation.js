odoo.define("geotagging_odoo.geolocation", function (require) {
  "use strict";
  console.log("LOADED asdf");

  var FormController = require("web.FormController");
  var rpc = require("web.rpc");

  FormController.include({
    saveRecord: function () {
      console.log("Saved!");
      var self = this;
      return this._super.apply(this, arguments).then(function () {
        var recordID = self.model.get(self.handle, { raw: true }).res_id;

        if (recordID) {
          navigator.geolocation.getCurrentPosition(function (position) {
            const { latitude, longitude } = position.coords;
            const coords = {
              latitude,
              longitude,
            };
            console.log(coords);
            rpc
              .query({
                model: "geotagging", // Replace with your actual model name
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

// var ExtendFormController = FormController.include({
//   saveRecord: function () {
//     var res = this._super.apply(this, arguments);
//     self = this;
//     if (this.modelName == "geotagging") {
//       console.log("HELLOO");
//       navigator.geolocation.getCurrentPosition(function (position) {
//         const { latitude, longitude } = position.coords;
//         const coords = {
//           latitude,
//           longitude,
//         };
//         console.log(coords);
//         self
//           ._rpc({
//             model: "geotagging",
//             method: "get_location",
//             args: [[], coords],
//           })
//           .then(function (result) {
//             // window.location.reload();
//           });
//       });
//     }

//     return res;
//   },
// });
