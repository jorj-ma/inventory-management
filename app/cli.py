import click
import requests

API_URL = "http://127.0.0.1:5000/auth"

@click.group()
def cli():
    """Auth CLI for register and login"""
    pass

@cli.command()
@click.option("--username", required=True)
@click.option("--password", required=True)
@click.option("--role", default="viewer", help="Role: admin, staff, or viewer")
def register(username, password, role):
    """Register a new user"""
    response = requests.post(API_URL + "/register", json={
        "username": username,
        "password": password,
        "role": role
    })
    try:
        click.echo(response.json())
    except ValueError:
        click.echo(response.text)

@cli.command()
@click.option("--username", required=True)
@click.option("--password", required=True)
def login(username, password):
    """Login with existing user"""
    response = requests.post(API_URL + "/login", json={
        "username": username,
        "password": password
    })
    try:
        click.echo(response.json())
    except ValueError:
        click.echo(response.text)

if __name__ == "__main__":
    cli()
