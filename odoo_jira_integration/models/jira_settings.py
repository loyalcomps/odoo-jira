# -*- coding: utf-8 -*-

import requests
from odoo import models, fields, api
from jira import JIRA

from odoo.exceptions import ValidationError



class JiraSettings(models.TransientModel):
    _name = 'jira.settings'
    _description = 'Jira Settings'

    jira_url = fields.Char(
        string='Jira URL',
        required=True,
        help='Enter the URL of your Jira instance. Example: https://jira.example.com'
    )
    jira_user = fields.Char(
        string='Jira User',
        required=True,
        help='Enter the username for your Jira account'
    )
    jira_apikey = fields.Char(
        string='Jira API Key',
        required=True,
        help='Enter the API key for your Jira account'
    )
    message = fields.Char(
        string='Message',
        readonly=True,
        help='This field will display status messages related to Jira integration'
    )

    @api.model
    def create(self, vals):
        if self.search_count([]) > 0:
            raise ValidationError("You can only create one Jira Settings record. Please update the existing record instead.")
        return super(JiraSettings, self).create(vals)

    def jira_settings_test_connection(self):
        for rec in self:
            try:
                jira = JIRA(server=rec.jira_url, basic_auth=(rec.jira_user, rec.jira_apikey))
                jira.projects()
                rec.message = 'Connection successful'
            except Exception as e:
                rec.message = 'Connection failed: %s' % str(e)


    @api.model
    def jira_settings_save_settings(self):
        """
        Save the Jira settings
        """
        self.env['ir.config_parameter'].sudo().set_param('jira.url', self.jira_url)
        self.env['ir.config_parameter'].sudo().set_param('jira.user', self.jira_user)
        self.env['ir.config_parameter'].sudo().set_param('jira.apikey', self.jira_apikey)
        self.message = 'Settings saved successfully!'

    @api.model
    def jira_settings_get_settings(self):
        """
        Get the saved Jira settings
        """
        jira_url = self.env['ir.config_parameter'].sudo().get_param('jira.url')
        jira_user = self.env['ir.config_parameter'].sudo().get_param('jira.user')
        jira_apikey = self.env['ir.config_parameter'].sudo().get_param('jira.apikey')
        return {'jira_url': jira_url, 'jira_user': jira_user, 'jira_apikey': jira_apikey}
