import typer
from rich import print
from rich.markdown import Markdown
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os
from dotenv import load_dotenv
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()
    
@tool(description = "Showing a specific file")
async def open_file(path: str) -> None:
    with open(path, 'r') as file:
        content = Markdown(file.read())
        print(content)
    
@tool(description = "rewriting a specific file, or creating and adding information to the file")
async def edit_file(path: str) -> None:
    with open(path, 'w') as file:
        content = file.read()
        print(content) 
        
@tool(description = "To create a new empty file")
async def create_file(path: str) -> None:
    with open(path, 'w') as file:
        pass  
        
        
agent = create_agent(
    model = "gpt-4o",
    tools = [open_file, edit_file, create_file],
    system_prompt = "you are an assistant"
)

@app.command()
def call_agent(message: str) -> None:
    user_message = ""
    print("Hi, I'm CLITY your CLI notes assistant")
    while user_message != "EXIT":
        user_message = input("Typing your requirements: ")
        
        response = agent.invoke({"messages":[{"role": "user", "content": f"{user_message}"}]})
        
        print(response["messages"][-1].content)
        
        if  user_message == "EXIT":
            print("see you later, friend!")
            break
        

if __name__ == "__main__":
    app()