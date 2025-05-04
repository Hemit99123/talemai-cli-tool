import click
from helper.creditionals import read_db_config, write_db_config
from helper.store_vectors import store_vectors

@click.command()

# This is the update paramter variable
@click.option('--update', is_flag=True, help='Update the AstraDB URL.')

def main(update):
    click.echo(click.style("Welcome to Talem AI CLI!", fg="blue"))

    db_config = read_db_config()
    collection_name = click.prompt("Enter collection name to update")
    namespace = click.prompt("Enter namespace to update")
    pdf_url = click.prompt("Enter PDF url")


    if (update or not db_config):
        new_api_endpoint = click.prompt('Enter new AstraDB URL')
        new_namespace = click.prompt('Enter new AstraDB Namespace')

        write_db_config(new_api_endpoint, new_namespace)
        click.echo(click.style("AstraDB URL updated successfully.", fg="green"))
    else:
        click.echo(click.style("Using stored AstraDB URL", fg="yellow"))
        store_vectors(pdf_url,collection_name,namespace)
        click.echo(click.style("Stored vector embeddings ✅", fg="green"))
    
if (__name__ == '__main__'):
    main()