odoo.define("geotagging_odoo.geolocation", function (require) {
  "use strict";
  console.log("KONTOLL");

  navigator.geolocation.getCurrentPosition(function (position) {
    const { latitude, longitude } = position.coords;
    const coords = {
      latitude,
      longitude,
    };
    self
      ._rpc({
        model: "geotagging",
        method: "get_location",
        args: [[], coords],
      })
      .then(function (result) {
        window.location.reload();
      });
  });
}



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
});
