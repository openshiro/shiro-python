import unittest
from unittest.mock import MagicMock
from shiro.client import ShiroClient
from shiro.prompt import Prompt

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.client = ShiroClient(api_key="test_key")
        self.client.request = MagicMock()
        self.prompt_manager = Prompt(self.client)

    def test_list_prompts(self):
        self.prompt_manager.list()
        self.client.request.assert_called_with("GET", "prompts")

    def test_retrieve_prompt(self):
        prompt_id = "123"
        self.prompt_manager.retrieve(prompt_id)
        self.client.request.assert_called_with("GET", f"prompts/{prompt_id}")

if __name__ == '__main__':
    unittest.main()
