import click
import socket

@click.group()
def cli():
    pass
@cli.command(name="ip_private")
def ip_private():
    hostname = socket.gethostname()  
    print(socket.gethostbyname(hostname))

if __name__ == "__main__":
    cli()