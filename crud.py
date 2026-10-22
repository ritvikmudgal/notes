import json
from datetime import datetime
import click
from pathlib import Path

@click.command()
@click.argument("title")
@click.option("--content", prompt=True, help="The content of the note")
@click.option("--tags", help="comma-separated list of tags")
def create(title: str, content: str, tags:str):
    """Create a new note"""
    notes_directory= Path("~/.notes").expanduser()
    notes_directory.mkdir(parents=True, exist_ok=True)
    note_name= f"{title}.txt"
    if (notes_directory / note_name).exists():
        click.echo(f"Note with '{title}' already exists.")
        exit(1)

    note_data= {
        "content":  content,
        "tags": tags.split(",") if tags else [],
        "Created_at": datetime.now().isoformat(),
    }
    with open(notes_directory / note_name, "a+" ) as file:
        json.dump(note_data, file)
    click.echo(f"Note '{title}' created. ")
        
    pass