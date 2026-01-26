## Contributing

We welcome contributions! Here are some ways you can help:

### Quick Wins
- Add more example files for different languages
- Improve documentation with examples
- Add more diagram templates

### Reporting Issues
- Use the issue templates provided
- Include reproduction steps
- Share your environment details

### Pull Requests
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run pre-commit hooks: `pre-commit run --all-files`
5. Submit a PR with clear description

### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/automations-with-hooks.git
cd automations-with-hooks

# Install dependencies
pip install pre-commit
pip install -r requirements.txt
brew install graphviz  # macOS

# Install hooks
pre-commit install

# Test your changes
pre-commit run --all-files
```

### Code Style
- Python: Follow PEP 8 (enforced by Black)
- JavaScript: Follow ESLint rules
- Commit messages: Use conventional commits format

### Ideas for Contributions
Check out the [GitHub Issues](https://github.com/mtzanida/automations-with-hooks/issues) for a list of potential enhancements and features to work on.
