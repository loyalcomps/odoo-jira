# -*- coding: utf-8 -*-

from odoo import api, fields, models
from jira import JIRA


class JiraSettings(models.TransientModel):
    _name = 'jira.settings'
    _description = 'Jira Settings'

    jira_url = fields.Char(string='Jira URL', required=True, help='Example: https://jira.example.com')
    jira_user = fields.Char(string='Jira User', required=True, help='Example: jirauser')
    jira_api_key = fields.Char(string='Jira API Key', required=True, help='Example: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    message = fields.Char(string='Message')

    #function to test the connection with Jira
    @api.model
    def test_connection(self):
        jira_url = self.jira_url
        jira_user = self.jira_user
        jira_api_key = self.jira_api_key
        try:
            jira = JIRA(jira_url, basic_auth=(jira_user, jira_api_key))
            self.message = 'Connection Successful'
        except:
            self.message = 'Connection Failed'