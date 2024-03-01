import os
import unittest
from shiro.client import ShiroClient
from shiro.prompt import Prompt
from test_helper import setup_vcr

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.client = ShiroClient(api_key=os.environ.get("SHIRO_API_KEY"))
        self.prompt_manager = Prompt(self.client)

    @setup_vcr().use_cassette('prompts_list.yml')
    def test_list_prompts(self):
        response = self.prompt_manager.list()
        self.assertTrue(isinstance(response, list), "Expected a list of prompts")
        self.assertTrue('id' in response[0], "Expected first prompt to have an 'id'")
        self.assertTrue('name' in response[0], "Expected first prompt to have a 'name'")
        # Add more assertions as needed based on the expected structure of a prompt

    @setup_vcr().use_cassette('prompt_retrieve.yml')
    def test_retrieve_prompt(self):
        prompt_id = os.environ.get("SHIRO_PROMPT_ID")  # Use actual prompt ID from environment variable
        response = self.prompt_manager.retrieve(prompt_id)
        self.assertEqual('<SHIRO_PROMPT_ID>', response['id'], "The prompt ID should match the requested one")
        self.assertTrue('name' in response, "Expected prompt to have a 'name'")
        self.assertTrue('body' in response, "Expected prompt to have a 'body'")
        # Add more assertions as needed based on the expected structure of a prompt

if __name__ == '__main__':
    unittest.main()
