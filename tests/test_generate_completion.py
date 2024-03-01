import os
import unittest
from shiro.client import ShiroClient
from shiro.generate_completion import GenerateCompletion
from test_helper import setup_vcr

class TestGenerateCompletion(unittest.TestCase):
    def setUp(self):
        self.client = ShiroClient(api_key=os.environ.get("SHIRO_API_KEY"))
        self.generate_completion = GenerateCompletion(self.client)

    @setup_vcr().use_cassette('generate_completion_create.yml')
    def test_create_generates_completion(self):
        data = {
            "deployment_id": os.environ.get('SHIRO_DEPLOYMENT_ID'),
            "environment": "PRODUCTION",
            "prompt_id": os.environ.get("SHIRO_PROMPT_ID"),
            "input_variables": {"review_text": "I loved the movie."}
        }
        response = self.generate_completion.create(data)
        self.assertTrue('content' in response, "Expected response to include 'content'")
        # Add more detailed assertions as needed based on the expected structure and content of the response

if __name__ == '__main__':
    unittest.main()
