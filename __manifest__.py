# -*- coding: utf-8 -*-
# Copyright 2024-Today EKBlocks.
# Part of EKBlocks. See LICENSE file for full copyright and licensing details.
{
    'name': "Manage Classes",
    'version': "2.0",
    'description': "This app for management center that help managers to manage the all type of documents, finance, pedagogy.",
    'summary': "Manage classes",
    'author': 'Ahmed kabbaj',
    # 'website': "https://www.ekblocks.com",
    # 'depends': ['mail', 'contacts', 'product', 'sale_management', 'bus',],
    'depends': ['base', 'mail'],
    'data': [
        # master
        # "data/master.xml",
        # data
        # Security
        'security/ir.model.access.csv',
        # Wizards
        # 'wizards/vehicle_damage_views.xml',
        # Views        
        'views/class_student_view.xml',
        'views/class_group_view.xml',
        
        # Reports
        # 'report/student_application_reports.xml',
        # 'report/student_receipt_reports.xml',
        # 'report/group_list_absent_report.xml',
        # Menus
        'views/class_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'tutoring_center/static/src/**/*',
            # 'tutoring_center/static/src/css/subscribe.css',
        ],
    },
    # 'images': ['static/description/cover.gif'],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 110,
    'currency': 'EUR',
}
