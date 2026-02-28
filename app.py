import click
from pathlib import Path


base = Path.home() /"Desktop"/"Katerly_Projects"

@click.group()
def katerly():
    
    """This is Katerly project management CLI"""
    pass

@katerly.command()
def welcome():
    
    click.echo("Welcome you have successfully run Katerly!")
    
@katerly.command()
@click.argument("name")
def init(name):
    project = base / name
    project.mkdir(parents=True,exist_ok=True)
    
@katerly.command()
def list():
    
    click.ls()
    

@katerly.command()
@click.argument("name")
def info(name):
    
    click.echo(click.ls(name))
    
    
@katerly.command()
@click.argument("name")
def remove(name):
    
    click.rm(name)

if __name__ == "__main__":
    
    katerly()