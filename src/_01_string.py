import click

@click.group()
def cli():
    pass


@cli.command(name="lowercase")
@click.argument("string")
def lowercase(string):
    print(string.lower())

@cli.command(name="uppercase")
@click.argument("string")
def uppercase(string):
    print(string.upper())

@cli.command(name="capitalize")
@click.argument("string")
def capitalize(string):
    print(string.title())

if __name__ == '__main__':
    cli()
