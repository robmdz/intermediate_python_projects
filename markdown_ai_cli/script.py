import typer
from rich import print
from rich.markdown import Markdown
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()

@app.command()
@tool
def open_file(path: str) -> none:
    with open(path, 'r') as md:
        content = Markdown(md.read())
        print(content)
    
@tool
def edit_file(path: str) -> none:
    with open(path, 'w') as md:
        content = Markdown(md.read())
        print(content)    
        
        
agent = create_agent(
    model = "gpt-4o",
    tools = [open_file, edit_file],
    system_prompt = "you are an assistant"
)
        
response = model.invoke()
response.usage_metadata

if __name__ == "__main__":
    app()