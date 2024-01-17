# -*- coding: utf-8 -*-
{
    'name': "Dental_Care",

    'summary': "Dental care module for managing services, doctors, patients, and appointments",
    'description': "Custom module for dental care management in Odoo.",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/services_view.xml',
        'views/doctors_view.xml',
        'views/patients_view.xml',
        'views/appointments_view.xml',
        'views/views.xml',
        'security/ir.model.access.csv'
    ],

    'installable': True,
    'application': True,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'images': [
        'static/description/icon.png'
    ],
}

