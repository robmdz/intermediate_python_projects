import typer
from rich import print

app = typer.Typer()

@app.command()
def view(path: str):
    with open(path, 'r') as md:
        content = md.read()
        print(content)
        
        

if __name__ == "__main__":
    app()