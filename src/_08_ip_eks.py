from requests import get
import click

@click.group()
def cli():
    pass
@cli.command(name="ip_eks")
def ip_eks():
    ip = get('https://api.ipify.org').text
    print(ip)

if __name__ == "__main__":
    cli()