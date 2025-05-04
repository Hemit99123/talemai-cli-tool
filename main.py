import click
import os

CONFIG_FILE = 'config.txt'

def read_db_url():
    if (os.path.exists(CONFIG_FILE) == True):
        with open(CONFIG_FILE, 'r') as file:
            return file.read().strip()
    return None

def write_db_url(url):
    with open(CONFIG_FILE, 'w') as file:
        file.write(url.strip())

@click.command()

# This is the update paramter variable
@click.option('--update', is_flag=True, help='Update the AstraDB URL.')

def main(update):
    """Talem AI CLI."""
    click.echo(click.style("Welcome to Talem AI CLI!", fg="blue"))

    current_url = read_db_url()
    collection_name = click.prompt("Enter collection name to update")

    if (update or not current_url):
        new_url = click.prompt('Enter new AstraDB URL')
        write_db_url(new_url)
        click.echo(click.style("AstraDB URL updated successfully.", fg="green"))
    else:
        click.echo(click.style(f"Using stored AstraDB URL", fg="yellow"))

if (__name__ == '__main__'):
    main()
