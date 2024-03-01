import os
import unittest
from shiro.client import ShiroClient
from shiro.deployment import Deployment
from test_helper import setup_vcr

class TestDeployment(unittest.TestCase):
    def setUp(self):
        # Use the actual API key from environment variables
        self.client = ShiroClient(api_key=os.environ.get("SHIRO_API_KEY"))
        self.deployment = Deployment(self.client)

    @setup_vcr().use_cassette('deployments_list.yml')
    def test_list_deployments(self):
        response = self.deployment.list()
        self.assertTrue('id' in response[0], "Expected first deployment to have an 'id'")
        self.assertTrue('name' in response[0], "Expected first deployment to have a 'name'")
        # Add more assertions as needed based on the expected structure of a deployment

    @setup_vcr().use_cassette('deployment_retrieve.yml')
    def test_retrieve_deployment(self):
        deployment_id = os.environ.get("SHIRO_DEPLOYMENT_ID")
        response = self.deployment.retrieve(deployment_id)
        self.assertEqual(deployment_id, response['id'], "The deployment ID should match the requested one")
        self.assertTrue('name' in response, "Expected deployment to have a 'name'")
        self.assertTrue('environment_type' in response, "Expected deployment to have 'environment_type'")

    @setup_vcr().use_cassette('deployment_update.yml')
    def test_update_deployment(self):
        deployment_id = os.environ.get("SHIRO_DEPLOYMENT_ID")
        new_name = "Updated Deployment Name"
        response = self.deployment.update(deployment_id, {"name": new_name})
        self.assertEqual(new_name, response["name"], "Expected the deployment's name to be updated")

if __name__ == '__main__':
    unittest.main()
