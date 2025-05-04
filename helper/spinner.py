import click
import itertools
import sys
import time

def spinner():
    spinner = itertools.cycle("|/-\\")
    click.echo(click.style("Loading... ", fg="yellow"), nl=False)

    for _ in range(20):  # simulate work
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")

if __name__ == "__main__":
    main()