import click

@click.group()
def cli():
    pass
@cli.command(name="palindrome")
@click.argument("text",type=click.STRING)
def palindrome(text):
    print("String :", text)
    if text == text[::-1] :
        print('Is palindrome? Yes')
    else :
        print('Is palindrome? No')


if __name__ == "__main__":
    cli()