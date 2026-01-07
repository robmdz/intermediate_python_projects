import typer

app = typer.Typer()

@app.command()
def view(path: str):
    with open(path, 'r') as md:
        content = md.read()
        print(content)
        
        

if __name__ == "__main__":
    app()