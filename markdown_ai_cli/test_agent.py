from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

agent = create_agent(
    model = "gpt-4o",
    system_prompt = "you are an assistant"
)
        
response = agent.invoke({"messages":[{"role": "user", "content": "what is the best country in the world"}]})

print(type(response))
print("---------------------")
print(type(response["messages"]))
print("---------------------")
print(response)
print("---------------------")
print(response["messages"][0])
print("---------------------")
print(type(response["messages"][0]))
print("---------------------")
print(response["messages"][0].content)
# print("---------------------")
# print(response["messages"][1].content)
# print("---------------------")
# print(response["messages"][-1])

#last_message = response["messages"][-1]

#print(last_message.content)