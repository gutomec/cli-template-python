import pytest
from typer.testing import CliRunner
from cli.main import app

@pytest.fixture
def cli_runner():
    return CliRunner()

@pytest.fixture
def cli_app():
    return app
