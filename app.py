import click
from pathlib import Path


base = Path.home() /"Desktop"/"Katerly_Projects"
reg_path = base / "registry.csv"


@click.group()
def katerly():
    
    """This is Katerly project management CLI"""
    if not base.exists():
        click.echo("Oops base directory not found!")
        
    if not reg_path.exists():
        click.echo("Oops base registry not found!")

@katerly.command()
def welcome():
    
    click.echo("Welcome you have successfully run Katerly!")
    
@katerly.command()
@click.argument("name")
def init(name):
    project_path = base / name
    project_path.mkdir(parents=True,exist_ok=True)
    
    with reg_path.open("r",encoding="utf-8") as registry:
        for line in registry:
            if line.split(",")[0]==name:
                click.echo("Folder/File with same name already exists!")
                return
                
        else:
            
            from datetime import datetime,timezone
            createdAt = datetime.now(timezone.utc).isoformat()
            
            row = f"{name},{project_path.resolve()},{createdAt}\n"
            
            with reg_path.open("a",encoding="utf-8") as registry:
                registry.write(row)
        
            click.echo(f"Directory{name} created and logged!")
            click.echo(f"Path: {project_path.resolve()}")
    
    
@katerly.command()
def list():
    
    if not reg_path.exists():
        click.echo("No file has yet been created")
        
    else:
        
        with reg_path.open("r",encoding="utf-8") as registry:
            
            
            for line in registry:
                
                click.echo(f"Name : {line.split(',')[0]}\nPath : {line.split(',')[1]}\nCreatedOn : {line.split(',')[2]}")
    
    

@katerly.command()
@click.argument("name")
def info(name):
    
    project_path = base / name
    
    if not project_path.exists():
        click.echo("No such Folder/File was found!")
        
    else:
        
        with reg_path.open("r",encoding="utf-8") as registry:
            
            for line in registry:
                
                if line.split(',')[0] == name:
                    click.echo(f"Name : {line.split(',')[0]}\nPath : {line.split(',')[1]}\nCreatedOn : {line.split(',')[2]}OnDisk : {project_path.exists()}\n")
    
    
@katerly.command()
@click.argument("name")
def remove(name):
    
    project_path = base / name
    
    if not project_path.exists():
        
        click.echo("No such Folder/File exists!")
        
    else:
        
        # Handling Folder deletion
        shutil.rmtree(project_path)
        
        # Handling deletion in Registry location
        # with reg_path.open("a",encoding="utf-8") as registry:
            
            
        
    

if __name__ == "__main__":
    
    katerly()
    