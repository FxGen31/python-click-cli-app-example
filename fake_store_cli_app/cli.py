import click
from fake_store_cli_app.commands.cart import cart
from fake_store_cli_app.commands.products import products
from fake_store_cli_app.utils.error_handler import error_logger

BASE_URL = "https://fakestoreapi.com"

@click.group()
@click.pass_context
def entry_point(ctx):
    '''A CLI app to wrap Fake Store API'''
    ctx.ensure_object(dict)

    # Global context
    ctx.obj["BASE_URL"] = BASE_URL

# Add commands
entry_point.add_command(products)
entry_point.add_command(cart)

# Catch all the command exceptions in the CLI app
def safe_entry_point():
    try:
        entry_point()
    except Exception as e:
        click.secho(error_logger(e), err=True, fg="red")

if __name__ == "__main__":
    safe_entry_point(prog_name="fakecli")