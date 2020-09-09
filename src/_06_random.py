import click
import random
import string

@click.group()
def cli():
    pass
@cli.command(name="rand")
@click.option('--length')
@click.option('--uppercase',default=False,is_flag=True,type=click.BOOL)
@click.option('--lowercase',default=False,is_flag=True,type=click.BOOL)

def rand(length, uppercase, lowercase):
    letters = string.ascii_letters
    print ( ''.join(random.choice(letters) for i in range(int(length))) )

    if lowercase == True:
        letters = string.ascii_lowercase
        print ( ''.join(random.choice(letters) for i in range(10)) )
    if uppercase == True:
        letters = string.ascii_uppercase
        print ( ''.join(random.choice(letters) for i in range(10)) )
        
if __name__ == "__main__":
    cli()