odoo.define('pos_customisation.product_screen', function(require){
    "use strict";
    const components = {
        ProductScreen: require('point_of_sale.ProductScreen')
    };
    const { patch } = require('web.utils');
    var models = require('point_of_sale.models');
    models.load_fields('res.users','disable_numpad');
    patch(components.ProductScreen, 'product_screen', {
        mounted() {
            if (this.env.pos.user.disable_numpad) {
                $('.pads').hide();   // For hide the number pad only, use "$('.numpad').hide();"
            }else{
                $('.pads').show();   // For showing number pad only, use "$('.numpad').show();"
            }
        }
    });
});
