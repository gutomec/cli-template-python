def test_hello(cli_runner, cli_app):
    result = cli_runner.invoke(cli_app, ["hello"])
    assert result.exit_code == 0
    assert "Hello" in result.stdout
