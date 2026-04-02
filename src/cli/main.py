import typer

app = typer.Typer(help="Production CLI template with Typer")

@app.command()
def hello(name: str = typer.Option("World", help="Name to greet")) -> None:
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()
