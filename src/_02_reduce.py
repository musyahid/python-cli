
import click
from functools import reduce

@click.group()
def cli():
    pass

@cli.command(name="add")
@click.argument("val",type=click.INT,nargs= -1)
def add(val) :
    print(reduce(lambda a,b : a+b,val))

@cli.command(name="subtract")
@click.argument("val",type=click.INT,nargs= -1)
def subtract(val) :
    print(reduce(lambda a,b : a-b,val))

@cli.command(name="multiply")
@click.argument("val",type=click.INT,nargs= -1)
def multiply(val):
    print(reduce(lambda a,b : a*b,val))

@cli.command(name="multiply")
@click.argument("val",type=click.INT,nargs= -1)
def multiply(val):
    print(reduce(lambda a,b : a*b,val))

@cli.command(name="divide")
@click.argument("val",type=click.INT,nargs= -1)
def divide(val):
    print(reduce(lambda a,b : a/b,val))

if __name__ == '__main__':
    cli()