import unittest
from unittest.mock import MagicMock
from shiro.client import ShiroClient
from shiro.deployment import DeploymentManager

class TestDeploymentManager(unittest.TestCase):
    def setUp(self):
        self.client = ShiroClient(api_key="test_key")
        self.client.request = MagicMock()
        self.deployment_manager = DeploymentManager(self.client)

    def test_create_deployment(self):
        data = {"name": "Test Deployment"}
        self.deployment_manager.create(data)
        self.client.request.assert_called_with("POST", "deployments", data)

    def test_retrieve_deployment(self):
        deployment_id = "123"
        self.deployment_manager.retrieve(deployment_id)
        self.client.request.assert_called_with("GET", f"deployments/{deployment_id}")

    def test_update_deployment(self):
        deployment_id = "123"
        data = {"name": "Updated Deployment"}
        self.deployment_manager.update(deployment_id, data)
        self.client.request.assert_called_with("PATCH", f"deployments/{deployment_id}", data)

    def test_delete_deployment(self):
        deployment_id = "123"
        self.deployment_manager.delete(deployment_id)
        self.client.request.assert_called_with("DELETE", f"deployments/{deployment_id}")

    def test_list_deployments(self):
        self.deployment_manager.list()
        self.client.request.assert_called_with("GET", "deployments")

if __name__ == '__main__':
    unittest.main()

