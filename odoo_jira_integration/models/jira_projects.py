from jira import JIRA, JIRAError
from odoo import models, fields, api
import logging
import re

_logger = logging.getLogger(__name__)

class ProjectProject(models.Model):
    _inherit = 'project.project'
    key = fields.Char(string='Jira Key', size=10)


    def create_jira_project(self, jira_url, jira_user, jira_apikey):
        jira = JIRA(server=jira_url, basic_auth=(jira_user, jira_apikey))       
        project_name = self.name
        project_key = ''.join([word[0] for word in project_name.split()]).upper()[:10]
        assignee = None
        ptype = 'software'
        template_name = None

        try:
            result = jira.create_project(key=project_key, name=project_name, assignee=assignee, ptype=ptype, template_name=template_name)
            if not result:
                _logger.warning(f'Failed to create JIRA project with key "{project_key}"')
            else:
                _logger.info(f'Successfully created JIRA project with key "{project_key}"')
        except JIRAError as e:
            _logger.error(f'JIRA error while creating project with key "{project_key}": {e.text}')
            _logger.error(f'JIRA error : {str(e)}')



    def write(self, vals):
        res = super(ProjectProject, self).write(vals)
        _logger.info(f'vals: {vals}')
        if vals.get('subtask_project_id'):
            # get Jira settings from database
            jira_settings = self.env['jira.settings'].sudo().search([], limit=1)
            if jira_settings:
                jira_url = jira_settings.jira_url
                jira_user = jira_settings.jira_user
                jira_apikey = jira_settings.jira_apikey
                self.create_jira_project(jira_url, jira_user, jira_apikey)
            else:
                _logger.warning('JIRA settings not found, skipping JIRA project creation')
        return res
