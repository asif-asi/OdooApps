odoo.define("pos_customisation.models", function (require) {
    "use strict";

    var models = require("point_of_sale.models");
    models.load_fields("res.partner", ["customer_type"]);
});
