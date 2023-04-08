# -*- coding: utf-8 -*-
{
    'name': 'Odoo Jira Integration',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'Integrate Odoo and Jira for better project management',
    'description': """
        This module integrates Odoo and Jira to provide seamless project management.
        """,
    'author': 'Shamnas Koyani',
    'company': 'Loyal IT Solutions Pvt Ltd',
    'website': 'https://www.loyalitsolutions.com',
    'license': 'AGPL-3',
    'application': True,
    'sequence': -100,
    'depends': ['base', 'project'],
    'data': [
        'views/jira_settings_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': {
        'test':['tests/*.*']
    },
    'installable': True,
    'auto_install': False,
    'custom_tags': {
        'test': ['+views/jira_settings.xml', '+tests/*' ],
    },
}
