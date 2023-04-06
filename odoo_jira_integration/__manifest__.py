# -*- coding: utf-8 -*-
{
    'name': 'Odoo Jira Integration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integrate Odoo and Jira for better project management',
    'description': """
        This module integrates Odoo and Jira to provide seamless project management.
        """,
    'author': 'Shamnas Koyani',
    'company': 'Loyal IT Solutions Pvt Ltd',
    'depends': ['base', 'project'],
    'data': [
        'views/my_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}