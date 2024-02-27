class DeploymentManager:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        """Create a new deployment."""
        return self.client.request("POST", "deployments", data)

    def retrieve(self, deployment_id):
        """Retrieve a specific deployment by its ID."""
        return self.client.request("GET", f"deployments/{deployment_id}")

    def update(self, deployment_id, data):
        """Update a specific deployment."""
        return self.client.request("PATCH", f"deployments/{deployment_id}", data)

    def delete(self, deployment_id):
        """Delete a specific deployment."""
        return self.client.request("DELETE", f"deployments/{deployment_id}")

    def list(self):
        """List all deployments."""
        return self.client.request("GET", "deployments")

