# Automations with Hooks

This repository showcases various automation scripts and configurations utilizing Git hooks and tools like Pre-commit. It serves as a resource for implementing automated checks and enhancements to streamline your development workflow.

## Features

- **ESLint**: Automated JavaScript linting to maintain code quality.
- **Black**: Python code formatting to ensure code consistency.
- **Pytest**: Automated unit testing for reliable code delivery.
- **Infrastructure Diagrams**: Automated generation and validation of AWS architecture diagrams using Python diagrams library.
- **Security Checks**: Detect AWS credentials and private keys before committing.

## Setup

1. Clone the repository.
2. Install Pre-commit: `pip install pre-commit`
3. Install Python dependencies: `pip install -r requirements.txt`
4. Install Graphviz (required for diagrams): `brew install graphviz` (macOS) or `apt-get install graphviz` (Linux)
5. Set up Pre-commit hooks: `pre-commit install`

## Usage

After setup, Pre-commit will run the following scripts before each commit:

- **Lint JS files** with ESLint.
- **Format Python files** with Black.
- **Run unit tests** with Pytest.
- **Validate infrastructure diagrams** by executing diagram generation scripts.
- **Security checks** for AWS credentials and private keys.

## Directory Structure

```plaintext
automations-with-hooks/
├── .pre-commit-config.yaml      # Config for Pre-commit hooks
├── requirements.txt             # Python dependencies
├── pre-commit-scripts/          # Custom scripts for hooks
│   ├── check-eslint.sh
│   ├── check-format.sh
│   ├── check-unit-tests.sh
│   └── check-diagrams.sh
├── diagrams/                    # Infrastructure diagram scripts
│   └── infrastructure_diagram.py
└── src/                         # Example source files
```

## Infrastructure Diagrams

The `diagrams/` directory contains Python scripts that generate AWS architecture diagrams. These diagrams are automatically validated during pre-commit to ensure they can be generated without errors.

### Manual Diagram Generation
```bash
python3 diagrams/infrastructure_diagram.py
```

### Auto-Generate from Terraform
If you have Terraform code in your repository, diagrams can be auto-generated from your Terraform state:

```bash
# Initialize and apply Terraform first
cd terraform
terraform init
terraform apply

# Generate diagram from state
cd ..
python3 diagrams/auto_generate_from_terraform.py
```

The auto-generation script will:
1. Parse your Terraform state (`terraform show -json`)
2. Extract AWS resources (ECS, RDS, S3, etc.)
3. Generate a diagram Python script
4. Execute it to create the visual diagram

This happens automatically during pre-commit when `.tf` files are modified.
