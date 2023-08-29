odoo.define("geotagging_odoo.geolocation", function (require) {
  "use strict";
  console.log("KONTOLL");

  var FormController = require("web.FormController");

  var ExtendFormController = FormController.include({
    saveRecord: function () {
      var res = this._super.apply(this, arguments);
      self = this;
      if (this.modelName == "geotagging") {
        console.log("HELLOO");
        navigator.geolocation.getCurrentPosition(function (position) {
          const { latitude, longitude } = position.coords;
          const coords = {
            latitude,
            longitude,
          };
          console.log(coords);
          self
            ._rpc({
              model: "geotagging",
              method: "get_location",
              args: [[], coords],
            })
            .then(function (result) {
              // window.location.reload();
            });
        });
      }

      return res;
    },
  });
});

// var geolocation = Widget.extend({
//   custom_button_js: function () {
//     alert("KONTOL");
//     console.log("MMEEMEME");
//   },
// });
// return geolocation;

//   _get_location: function (ev) {
//     var self = this;
//     if (navigator.geolocation) {
//       navigator.geolocation.getCurrentPosition(function (position) {
//         const { latitude, longitude } = position.coords;
//         const coords = {
//           latitude,
//           longitude,
//         };
//         self
//           ._rpc({
//             model: "geotagging",
//             method: "get_location",
//             args: [[], coords],
//           })
//           .then(function (result) {
//             window.location.reload();
//           });
//       });
//     }
//   },
// });
