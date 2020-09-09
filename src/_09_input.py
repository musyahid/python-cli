import click
import socket

@click.group()
def cli():
    pass

@cli.command(name="sum_prompt")
@click.option('--number', prompt='Input Angka (1) ',type=click.INT)
def sum_prompt(number):
    angka = number
    total = int(number)
    i = 1
    while  angka != '':
        i+=1
        angka = input(f"Input angka ({i}) : ")
        if angka !='':
            total += int(angka)
        
    print("Hasil:",total)

if __name__ == "__main__":
    cli()