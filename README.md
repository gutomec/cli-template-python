# cli-template-python

Production-grade CLI template using Typer and Poetry.

## Features

- **Typer Framework**: Modern async-first Python CLI framework
- **Poetry**: Professional package and dependency management
- **Type Hints**: Full type safety with Python type hints
- **Testing**: pytest configuration with async support
- **Code Quality**: mypy, pylint, and black pre-configured
- **CI/CD**: GitHub Actions for test and lint workflows
- **Documentation**: Comprehensive guides and examples
- **Publishing**: Ready for PyPI publishing

## Quick Start

### Prerequisites

- Python 3.10+
- Poetry 1.0+

### Installation & Development

```bash
# Install dependencies with Poetry
poetry install

# Run CLI command
poetry run cli-template hello

# Run tests
pytest

# Run with coverage
pytest --cov

# Type checking
mypy src

# Linting
ruff check src tests

# Format code
black src tests
```

## Project Structure

```
cli-template-python/
├── src/
│   └── cli/
│       ├── __init__.py       # Package initialization
│       ├── main.py           # Main CLI entry point
│       ├── commands/         # Command modules
│       │   ├── __init__.py
│       │   ├── hello.py      # Example command
│       │   └── config.py     # Another example
│       └── utils/            # Shared utilities
│           ├── __init__.py
│           └── helpers.py    # Helper functions
├── tests/
│   ├── test_main.py          # Main tests
│   ├── test_commands/        # Command tests
│   │   ├── test_hello.py
│   │   └── test_config.py
│   └── conftest.py           # pytest fixtures
├── .github/
│   └── workflows/            # GitHub Actions CI/CD
│       ├── test.yml          # Test workflow
│       └── lint.yml          # Linting workflow
├── pyproject.toml            # Poetry configuration
├── poetry.lock               # Locked dependencies
└── README.md                 # This file
```

## Available Commands

### `hello`

Simple greeting command demonstrating CLI functionality.

```bash
poetry run cli-template hello --name "Your Name"
# Output: Hello, Your Name!
```

### Development Scripts (via Poetry)

| Command | Purpose |
|---------|---------|
| `poetry install` | Install all dependencies |
| `poetry run cli-template hello` | Run the CLI |
| `pytest` | Run all tests |
| `pytest --cov` | Generate coverage reports |
| `mypy src` | Type checking |
| `ruff check src tests` | Code linting |
| `black src tests` | Code formatting |
| `poetry add package` | Add production dependency |
| `poetry add --group dev package` | Add dev dependency |

## Testing

Tests use pytest with async support via pytest-asyncio.

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with verbose output
poetry run pytest -v

# Run specific test file
poetry run pytest tests/test_main.py

# Run with coverage report
poetry run pytest --cov=src

# Watch mode (requires pytest-watch)
poetry run pytest-watch
```

### Test Structure

- `tests/conftest.py` - pytest fixtures and shared configuration
- `tests/test_main.py` - Tests for main CLI
- `tests/test_commands/` - Tests for individual commands

## CI/CD Workflows

### `test.yml`
- Runs on: Windows, macOS, Linux
- Python versions: 3.10, 3.11, 3.12
- Coverage reporting with pytest-cov

### `lint.yml`
- mypy for type checking
- ruff for linting
- black for formatting checks

## Async Commands

Typer supports async commands out of the box:

```python
import typer

async def async_command():
    """An async command."""
    print("Running async task...")
    await some_async_operation()

app = typer.Typer()
app.command()(async_command)
```

## Publishing to PyPI

### One-time Setup

1. Create PyPI account at https://pypi.org
2. Configure OIDC for GitHub Actions
3. Set up repository secrets in GitHub

### Publishing

```bash
# Update version in pyproject.toml
poetry version patch  # or minor/major

# Commit and tag
git add pyproject.toml
git commit -m "Bump version to X.Y.Z"
git tag vX.Y.Z
git push origin main --tags

# GitHub Actions will publish to PyPI automatically
```

## Extending the Template

### Adding New Commands

1. Create new module in `src/cli/commands/`
2. Import and add to `src/cli/main.py`
3. Write tests in `tests/test_commands/`
4. Update documentation

Example:

```python
# src/cli/commands/hello.py
import typer

def hello(name: str = typer.Option("World")) -> None:
    """Say hello."""
    typer.echo(f"Hello, {name}!")
```

### Adding Dependencies

```bash
# Production dependency
poetry add new-package

# Development dependency
poetry add --group dev new-package
```

## Troubleshooting

### Import errors with Typer

- Check pyproject.toml has correct dependencies
- Run `poetry install`
- Verify Python version: `python --version` (should be 3.10+)

### Test failures

- Check conftest.py for fixture issues
- Verify async/await usage is correct
- Run with `-v` flag for verbose output

### Type checking errors

- Run `mypy src` to see all type issues
- Add type hints to functions
- Use `# type: ignore` sparingly for legitimate cases

## Best Practices

- Use type hints for all functions
- Write tests for all commands
- Keep commands focused and modular
- Use async when appropriate
- Follow black formatting
- Document public APIs
- Handle exceptions gracefully

## Dependencies

### Core
- **typer** - Modern CLI framework
- **pydantic** - Data validation

### Development
- **pytest** - Testing framework
- **pytest-cov** - Coverage reporting
- **mypy** - Type checker
- **ruff** - Fast Python linter
- **black** - Code formatter

## License

MIT - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Install dev dependencies: `poetry install`
4. Make your changes
5. Run tests: `pytest`
6. Run linting: `ruff check .` and `mypy src`
7. Format code: `black .`
8. Submit a pull request

## Resources

- [Typer Documentation](https://typer.tiangolo.com)
- [Poetry Guide](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org)
- [Python Type Hints](https://peps.python.org/pep-0484/)
- [asyncio Guide](https://docs.python.org/3/library/asyncio.html)
