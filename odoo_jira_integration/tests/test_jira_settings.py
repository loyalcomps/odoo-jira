from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestJiraSettings(TransactionCase):

    def setUp(self):
        super().setUp()

        self.JiraSettings = self.env['jira.settings']

    def test_jira_settings(self):
        """Test Jira Settings"""

        # Create Jira Settings record
        jira_settings = self.JiraSettings.create({
            'jira_url': 'https://jira.example.com',
            'jira_api_key': 'my_api_key'
        })

        # Check that Jira Settings record was created successfully
        self.assertTrue(jira_settings.id)

        # Update Jira Settings record
        jira_settings.write({'jira_url': 'https://jira2.example.com'})

        # Check that Jira Settings record was updated successfully
        self.assertEqual(jira_settings.jira_url, 'https://jira2.example.com')

        # Test validation error when creating Jira Settings record without required fields
        with self.assertRaises(ValidationError):
            self.JiraSettings.create({})

        # Test validation error when creating Jira Settings record with invalid URL
        with self.assertRaises(ValidationError):
            self.JiraSettings.create({
                'jira_url': 'invalid_url'
            })
