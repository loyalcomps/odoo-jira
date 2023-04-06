from odoo import http
from odoo.http import request
import requests

class JiraSettingsController(http.Controller):

    @http.route('/jira/check_connection', type='http', auth='user', website=True)
    def check_connection(self):
        # Get the jira settings from the database
        settings = request.env['jira.settings'].sudo().search([], limit=1)

        # Make a request to the Jira API to check the connection
        url = settings.jira_url + '/rest/api/2/myself'
        response = requests.get(url, auth=(settings.jira_user, settings.jira_password))

        # Set a message based on the response
        if response.status_code == 200:
            message = 'Connection successful!'
        else:
            message = 'Connection failed.'

        # Return a response with the message
        return request.render('odoo_jira_integration.jira_settings_message', {'message': message})
    
    @http.route('/jira/settings/view', type='http', auth='user', website=True)
    def view_jira_settings(self, **kwargs):
        jira_settings = request.env['jira.settings'].view_saved_jira_settings()
        return request.render('odoo_jira_integration.jira_settings_view_form', {
            'jira_settings': jira_settings,
        })

