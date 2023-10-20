import click, json, requests
from fake_store_cli_app.utils.callbacks import validate_file_type
from fake_store_cli_app.utils.error_handler import cli_return_codes, CustomCliException


@click.group()
@click.pass_context
def products(ctx):
    '''
    Command to manage products
    '''

@click.option("-d", "--data", help="Product details in JSON format.")
@click.option("-f", "--file", type=click.Path(exists=True, dir_okay=False), callback=validate_file_type(["json"]) ,help="JSON file contains the product details.")
@products.command("create")
@click.pass_context
def add_new_product(ctx, data: str, file: str):
    '''
    Sub-command to add a new product
    '''
    # Product POST URL
    url = f"{ctx.obj['BASE_URL']}/products"

    # Prepare payload
    product_payload = {}
    if data:
        product_payload = json.loads(data)
    elif file:
        product_payload = json.load(open(file, "r"))
    else:
        raise CustomCliException(3, "JSON payload has to be passed by providing one of the following options: -d, -f")
    
    # Make POST request
    response = requests.post(url, json=product_payload)
    if response.ok:
        # Success message
        click.secho(f"0 - {cli_return_codes[0]}\nNew product has been added successfully.\n\nProduct Info: {json.dumps(response.json(), indent=4)}", fg="green")
    else:
        # API error message
        click.secho(f"API Error - {response.status_code}\nCannot add new product.\n\nError Message: {response.text}", fg="yellow")
    
@click.option("-o", "--output", type=click.Path(exists=True, dir_okay=False), callback=validate_file_type(["json"]) ,help="Output file to store the product list.")
@products.command("list")
@click.pass_context
def get_all_products(ctx, output: str):
    '''
    Sub-command to list all products

    If output file is not specified, the product list will be printed in the console.
    '''
    # Product GET URL
    url = f"{ctx.obj['BASE_URL']}/products"
    
    # Make GET request
    response = requests.get(url)
    if response.ok:
        if output:
            with open(output, "w") as json_file:
                json.dump(response.json(), json_file, indent=4)
        else:
            click.secho(f"0 - {cli_return_codes[0]}\n\nProduct List: {json.dumps(response.json(), indent=4)}", fg="green")
    else:
        # API error message
        click.secho(f"API Error - {response.status_code}\nCannot get all products.\n\nError Message: {response.text}", fg="yellow")
