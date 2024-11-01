# Automations with Hooks

This repository showcases various automation scripts and configurations utilizing Git hooks and tools like Pre-commit. It serves as a resource for implementing automated checks and enhancements to streamline your development workflow.

## Features

- **ESLint**: Automated JavaScript linting to maintain code quality.
- **Black**: Python code formatting to ensure code consistency.
- **Pytest**: Automated unit testing for reliable code delivery.

## Setup

1. Clone the repository.
2. Install Pre-commit: `pip install pre-commit`
3. Set up Pre-commit hooks: `pre-commit install`

## Usage

After setup, Pre-commit will run the following scripts before each commit:

- **Lint JS files** with ESLint.
- **Format Python files** with Black.
- **Run unit tests** with Pytest.

## Directory Structure

```plaintext
automations-with-hooks/
├── .pre-commit-config.yaml      # Config for Pre-commit hooks
├── pre-commit-scripts/          # Custom scripts for hooks
│   ├── check-eslint.sh
│   ├── check-format.sh
│   └── check-unit-tests.sh
└── src/                         # Example source files
```
