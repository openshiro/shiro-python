from shiro.client import Client

class Deployment:
    def __init__(self):
        self.client = Client()

    @classmethod
    def list(cls):
        response = cls.client.get("/deployments")
        return response.json()

    @classmethod
    def retrieve(cls, deployment_id):
        response = cls.client.get(f"/deployments/{deployment_id}")
        return response.json()

    @classmethod
    def create(cls, name, **kwargs):
        payload = {'name': name}
        payload.update(kwargs)
        response = cls.client.post("/deployments", body=payload)
        return response.json()

    @classmethod
    def update(cls, deployment_id, **kwargs):
        response = cls.client.patch(f"/deployments/{deployment_id}", body=kwargs)
        return response.json()

    @classmethod
    def delete(cls, deployment_id):
        response = cls.client.delete(f"/deployments/{deployment_id}")
        return response
