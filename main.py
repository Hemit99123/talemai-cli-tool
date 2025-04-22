import click

@click.group()
@click.option('--dbURL', prompt='AstraDB URL:',
              help='The DB url to make changes on.')

def main():
  click.echo(click.style("Welcome to Talem AI CLI!"), fg="blue")

if (__name__ == '__main__'):
  main()
