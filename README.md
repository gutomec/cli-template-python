# cli-template-python

Production CLI template using Typer and Poetry.

## Quick Start

```bash
poetry install
poetry run cli-template hello
pytest
```

## Commands

- `hello` - Example hello command

## Development

```bash
poetry install
poetry run cli-template hello      # Run CLI
pytest                             # Run tests
pytest --cov                       # Coverage
mypy src                           # Type checking
black src tests                    # Format
ruff check src tests               # Lint
```

## Publishing

```bash
poetry publish
```

## License

MIT
