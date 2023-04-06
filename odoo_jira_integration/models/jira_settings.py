# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models
import requests

class JiraSettings(models.TransientModel):
    _name = 'jira.settings'
    _description = 'Jira Settings'


    jira_url = fields.Char(string='Jira URL', required=True, help='Example: https://jira.example.com')
    jira_user = fields.Char(string='Jira User', required=True, help='Example: jirauser')
    jira_api_key = fields.Char(string='Jira API Key', required=True, help='Example: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


    @api.model
    def get_settings(self):
        settings = self.search([], limit=1)
        if settings:
            return settings
        else:
            return self.create({})

    @api.model
    def set_settings(self, url, username, api_key):
        settings = self.get_settings()
        settings.write({
            'jira_url': url,
            'jira_user': username,
            'jira_api_key': api_key,
        })

    def check_connection(self):
        # Get the Jira URL, username, and API key from the current settings record
        jira_url = self.jira_url
        jira_user = self.jira_user
        jira_api_key = self.jira_api_key

        # Construct the Jira authentication headers using the API key
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(
                (jira_user + ':' + jira_api_key).encode('utf-8')).decode('utf-8'),
            'Content-Type': 'application/json'
        }

        # Make a test request to Jira to check the connection
        url = jira_url.rstrip('/') + '/rest/api/latest/myself'
        response = requests.get(url, headers=headers)

        # Check the response status code to determine if the connection was successful
        if response.status_code == 200:
            # Connection successful
            self.message = "Connection successful!"
        else:
            # Connection failed
            self.message = "Connection failed: " + response.reason


    def action_back(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'jira.settings',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'new',
        }



