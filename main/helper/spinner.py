import itertools
import time
import click

def spinning_cursor():
    """Generator that yields a spinning cursor animation."""
    while True:
        for cursor in '|/-\\':
            yield cursor

def spinner():
    """Display a spinner in the CLI while a task is running."""
    spin = spinning_cursor()
    for _ in range(20):  # Adjust count as needed
        print(next(spin), end='\r', flush=True)
        time.sleep(0.1)
