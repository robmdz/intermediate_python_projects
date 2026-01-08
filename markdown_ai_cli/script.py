import typer
from rich import print
from rich.markdown import Markdown

app = typer.Typer()

@app.command()
def view(path: str):
    with open(path, 'r') as md:
        content = Markdown(md.read())
        print(content)
        
        

if __name__ == "__main__":
    app()