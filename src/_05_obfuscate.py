import click
from functools import reduce

@click.group()
def cli():
    pass
@cli.command(name="obfuscate")
@click.argument("text",type=click.STRING)
def obfuscate(text):
    text = list(text)
    print((list(map(lambda c: f"&#{ord(c)};",text))))

if __name__ == "__main__":
    cli()