# -*- coding: utf-8 -*-
{
    'name': "Point of Sale Customisation",
    'summary': """
        Customised point of sale customer search list with Customer Type, And
        added option to restrict pos number pad for specific Users""",
    "version": "14.0.1.0.0",
    'author': "Asif P",
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale', 'contacts'],
    'qweb': [
        'static/src/xml/Screens/ClientListScreen.xml'
    ],
    'data': [
        'views/res_users_view.xml',
        'views/res_partner_view.xml',
        'views/views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
}
