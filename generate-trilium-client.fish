#!/usr/bin/env fish
# Define the URL of the YAML file
set url https://raw.githubusercontent.com/zadam/trilium/master/src/etapi/etapi.openapi.yaml

# Download the YAML file using wget and save it as etapi.yaml
wget --output-document etapi.yaml $url 

# Check if virtualenv is installed
if not type -q virtualenv
    # If not, install it using pip
    pip install virtualenv
end

# Create a virtualenv called venv if it does not exist
if not test -d venv
    virtualenv venv
end

# Activate the virtualenv
source venv/bin/activate.fish

# Check if openapi-python-client is installed in the virtualenv
if not type -q openapi-python-client
    # If not, install it using pip
    pip install openapi-python-client
end

# Use openapi-python-client to generate a Python client from the YAML file
openapi-python-client generate --path etapi.yaml

# Use openapi-python-client to generate a Python client from the YAML file
openapi-python-client update --path etapi.yaml

# Deactivate the virtualenv
deactivate