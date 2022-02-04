# -*- coding: utf-8 -*-
{
    'name': "Couta CRM",

    'summary': """
        Couta CRM""",

    'description': """
        Couta CRM
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'views/crm_cuota_menu.xml',
        'views/crm_cuota_report.xml',
        'views/crm_cuota.xml',
        'views/crm_lead.xml',
        'views/get_crm_cuota_report.xml',
    ],
}
