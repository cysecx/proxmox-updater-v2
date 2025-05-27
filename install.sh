#!/bin/bash

echo "Running Proxmox Updater Setup..."

# If you want to install dependencies in a virtualenv:
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete!"
