# Contributing to Brain Vault

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct
- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/brain-vault.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Follow the setup instructions in [SETUP.md](./SETUP.md)

## Development Workflow

### Frontend Development
- Use React best practices
- Follow the component structure in `frontend/src/`
- Use Tailwind CSS for styling
- Run linter before committing: `npm run lint`

### Backend Development
- Follow PEP 8 style guide
- Use type hints in Python functions
- Organize code in appropriate modules
- Add docstrings to functions and classes

## Commit Guidelines

Use clear, descriptive commit messages:
```
feat: Add new feature description
fix: Fix bug description
docs: Update documentation
style: Format code
refactor: Refactor code
test: Add tests
```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Create a descriptive PR title and description
5. Link related issues

## Testing

### Frontend
```bash
cd frontend
npm run test
```

### Backend
```bash
cd backend
pytest
```

## Code Style

### Frontend
- Use ESLint configuration
- Format with Prettier
- Follow React naming conventions

### Backend
- Use Black for formatting
- Use isort for imports
- Follow PEP 8

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Update API.md for new endpoints
- Add comments for complex logic

## Questions?

- Open an issue for bugs
- Start a discussion for features
- Check existing issues before creating new ones

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
