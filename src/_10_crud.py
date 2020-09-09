import click,json

@click.group()
def cli():
    pass
@cli.command(name="create")
@click.option('--gender', default=False)
@click.option('--title', default=False)
@click.option('--first', default=False)
@click.option('--last', default=False)
@click.option('--street', default=False)
@click.option('--city', default=False)
@click.option('--state', default=False)
@click.option('--postcode', default=False)
@click.option('--email', default=False)
@click.option('--phone', default=False)
@click.option('--cell', default=False)


def create(gender,title,first,last,street,city,state,postcode,email,phone,cell):
    users = {
    "gender": gender,
    "name": {
        "title": title,
        "first": first,
        "last": last
    },
    "location": {
        "street": street,
        "city": city,
        "state": state,
        "postcode": postcode,
        "email": email,
        "phone": phone,
        "cell": cell
    }
    }
    # Serializing json  
    json_object = json.dumps(users, indent = 4) 
    
    # Writing to sample.json 
    with open("../users.json", "w") as outfile: 
        outfile.write(json_object) 


if __name__ == "__main__":
    cli()