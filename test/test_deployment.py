import unittest
from unittest.mock import patch
from shiro.deployment import Deployment

class TestDeployment(unittest.TestCase):
    @patch('shiro.client.Client.get')
    def test_list_deployments(self, mock_get):
        mock_get.return_value = {'deployments': [{'id': '1', 'name': 'Test Deployment'}]}
        deployments = Deployment.list()
        self.assertEqual(len(deployments['deployments']), 1)
        self.assertEqual(deployments['deployments'][0]['name'], 'Test Deployment')

    @patch('shiro.client.Client.get')
    def test_retrieve_deployment(self, mock_get):
        mock_get.return_value = {'id': '1', 'name': 'Test Deployment'}
        deployment = Deployment.retrieve('1')
        self.assertEqual(deployment['name'], 'Test Deployment')

    @patch('shiro.client.Client.post')
    def test_create_deployment(self, mock_post):
        mock_post.return_value = {'id': '1', 'name': 'New Deployment'}
        deployment = Deployment.create({'name': 'New Deployment'})
        self.assertEqual(deployment['name'], 'New Deployment')

    @patch('shiro.client.Client.patch')
    def test_update_deployment(self, mock_patch):
        mock_patch.return_value = {'id': '1', 'name': 'Updated Deployment'}
        deployment = Deployment.update('1', {'name': 'Updated Deployment'})
        self.assertEqual(deployment['name'], 'Updated Deployment')

    @patch('shiro.client.Client.delete')
    def test_delete_deployment(self, mock_delete):
        mock_delete.return_value = {'message': 'Deployment deleted'}
        response = Deployment.delete('1')
        self.assertEqual(response['message'], 'Deployment deleted')

if __name__ == '__main__':
    unittest.main()
