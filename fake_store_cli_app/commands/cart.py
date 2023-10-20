import click, json, requests
from fake_store_cli_app.utils.callbacks import validate_file_type
from fake_store_cli_app.utils.error_handler import cli_return_codes


@click.group()
@click.pass_context
def cart(ctx):
    '''
    Command to manage cart
    '''
    
@click.option("-o", "--output", type=click.Path(exists=True, dir_okay=False), callback=validate_file_type(["json"]) ,help="Output file to store the cart list.")
@cart.command("list")
@click.pass_context
def get_all_products(ctx, output: str):
    '''
    Sub-command to list all carts

    If output file is not specified, the cart list will be printed in the console.
    '''
    # Cart GET URL
    url = f"{ctx.obj['BASE_URL']}/carts"
    
    # Make GET request
    response = requests.get(url)
    if response.ok:
        if output:
            with open(output, "w") as json_file:
                json.dump(response.json(), json_file, indent=4)
        else:
            click.secho(f"0 - {cli_return_codes[0]}\n\Cart List: {json.dumps(response.json(), indent=4)}", fg="green")
    else:
        # API error message
        click.secho(f"API Error - {response.status_code}\nCannot get all carts.\n\nError Message: {response.text}", fg="yellow")
