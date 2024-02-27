# Shiro Python Library

This is the official [Shiro API](https://openshiro.com/api/v1/docs) Python package maintained by [OpenShiro](https://openshiro.com).

## Documentation

See the [API docs](https://openshiro.com/api/v1/docs) and also this post on [Getting Started with the Shiro API](https://openshiro.com/docs/getting-started-with-the-shiro-api).

## Installation

## Usage

````
from shiro_client import ShiroClient

# Initialize the client with your API key
client = ShiroClient("your_api_key_here")

# List all deployments
deployments = client.deployments.list()

# Retrieve a specific deployment
deployment = client.deployments.retrieve("deployment_id")

# Update a deployment
update_data = {"name": "Updated Deployment Name"}
updated_deployment = client.deployments.update("deployment_id", update_data)
````

## Development

Run all tests

`python -m unittest discover tests`
