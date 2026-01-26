#!/bin/bash
# Note: This script was created with assistance from Kiro CLI

# Run static diagram scripts
python3 diagrams/infrastructure_diagram.py

# Auto-generate from Terraform if available
if [ -d "terraform" ]; then
    echo "Checking for Terraform state..."
    python3 diagrams/auto_generate_from_terraform.py
fi
