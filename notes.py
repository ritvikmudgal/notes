from click import Path
import os
import click
import crud
from pathlib import Path
from config import load_config, DEFAULT_NOTES_DIR

@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context):
    """A simple note taking application"""
    config= load_config()
    notes_directory= config.get("notes_dir", str(DEFAULT_NOTES_DIR))
    if not os.path.exists(notes_directory):
        os.makedirs(notes_directory)


