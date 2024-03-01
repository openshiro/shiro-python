import unittest
from unittest.mock import MagicMock
from shiro.client import ShiroClient
from shiro.generate_completion import GenerateCompletionManager

class TestDeploymentManager(unittest.TestCase):
    def setUp(self):
        self.client = ShiroClient(api_key="test_key")
        self.client.request = MagicMock()
        self.generate_completion = GenerateCompletionManager(self.client)

    def test_create_deployment(self):
        data = {
                "environment": "PRODUCTION",
                "prompt_id": "prmt_123",
                "input_variables": { "review_text": "I loved the movie." }
        }
        self.generate_completion.create(data)
        self.client.request.assert_called_with("POST", "generate_completion", data)

if __name__ == '__main__':
    unittest.main()
