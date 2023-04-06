# -*- coding: utf-8 -*-

from odoo import api, fields, models


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
