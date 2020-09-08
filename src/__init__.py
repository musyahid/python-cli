import click
from src._01_string import lowercase, uppercase, capitalize 
from src._02_reduce import add,subtract,multiply,divide
from src._03_statistic import mean,median,mode,fmean
from src._04_palindrome import palindrome

@click.group()
def cli():
    pass

#1
cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)

#2
cli.add_command(lowercase)
cli.add_command(uppercase)
cli.add_command(capitalize)

#3
cli.add_command(mean)
cli.add_command(median)
cli.add_command(mode)
cli.add_command(fmean)

#4
cli.add_command(palindrome)




if __name__ == "__main__":
    cli()