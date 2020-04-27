# -*- coding: utf-8 -*-
{
    'name': "Clincal",

    'summary': """
        Clincal Managment System""",

    'description': """
        Clincal Managment System    """,

    'author': "Moaz",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'wizard/create_appointment.xml',
        'views/patient_view.xml',
        'data/patient_sequence.xml',
        'views/menu_view.xml',
        'views/appointment_view.xml',
        'views/templates.xml',
        'reports/patient_report.xml',
        'reports/patient_report_tempelete.xml',
        'security/hospital_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}