# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models
import requests

class JiraSettings(models.TransientModel):
    _name = 'jira.settings'
    _description = 'Jira Settings'

    jira_url = fields.Char(string='Jira URL')
    jira_user = fields.Char(string='Jira Username')
    jira_api_token = fields.Char(string='Jira API Token')

    @api.model
    def get_settings(self):
        settings = self.search([], limit=1)
        if settings:
            return settings
        else:
            return self.create({})

    @api.model
    def set_settings(self, url, username, api_token):
        settings = self.get_settings()
        settings.write({
            'url': url,
            'username': username,
            'api_token': api_token,
        })

    @api.env
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
