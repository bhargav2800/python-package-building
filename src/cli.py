import click
from src.services.airflow_service import AirflowService
from src.config import ConfigManager


@click.group()
def cli():
    """AWS Airflow SDK CLI tool."""
    pass


@cli.command(name="init")
def init():
    """Initialize or reset the environment."""
    try:
        session_token, server_hostname = AirflowService.authenticate_user()

        if session_token and server_hostname:
            ConfigManager.set_config_value('SESSION_TOKEN', session_token)
            ConfigManager.set_config_value('SERVER_HOSTNAME', server_hostname)
            click.echo("Authentication successful ...")
            click.echo(f"SESSION_TOKEN : {session_token}")
            click.echo(f"SERVER_HOSTNAME : {server_hostname}")
            click.echo("Token stored securely.")
        else:
            click.echo("Authentication failed.")
    except Exception as e:
        click.echo(f"Error during authentication: {str(e)}")


@cli.command(name="fetchDags")
def fetch_dags():
    """Fetch DAGs from the Airflow service."""
    try:
        session_token = ConfigManager.get_config_value('SESSION_TOKEN')
        server_hostname = ConfigManager.get_config_value('SERVER_HOSTNAME')

        if not session_token or not server_hostname:
            click.echo("Session token or server hostname not found. Please run `aws-airflow-sdk init` first.")
            return

        dags = AirflowService.fetch_dags(server_hostname, session_token)
        click.echo("DAGs fetched successfully ...")
        click.echo(f"SESSION_TOKEN : {session_token}")
        click.echo(f"SERVER_HOSTNAME : {server_hostname}")
        click.echo(dags)

    except Exception as e:
        click.echo(f"Error during fetchDags: {str(e)}")


if __name__ == "__main__":
    cli()
