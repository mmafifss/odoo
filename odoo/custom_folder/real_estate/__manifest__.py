# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': "Manage Properties and Real Estate Offers",
    'description': """
        Modul latihan Odoo 17: Manajemen Properti Real Estate.
    """,
    'author': "Developer",
    'category': 'Real Estate',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
