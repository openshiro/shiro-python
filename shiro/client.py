import requests

class Client:
    def __init__(self, api_key=None):
        if api_key is None:
            raise ValueError("API key not defined")
        self.api_key = api_key
        self.base_url = "https://openshiro.com/api/v1"

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get(self, path):
        response = requests.get(f"{self.base_url}/{path}", headers=self.get_headers())
        return response.json()

    def post(self, path, data):
        response = requests.post(f"{self.base_url}/{path}", json=data, headers=self.get_headers())
        return response.json()

    def patch(self, path, data):
        response = requests.patch(f"{self.base_url}/{path}", json=data, headers=self.get_headers())
        return response.json()

    def delete(self, path):
        response = requests.delete(f"{self.base_url}/{path}", headers=self.get_headers())
        return response.json()
