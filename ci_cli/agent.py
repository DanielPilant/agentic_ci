from langchain.agents import create_agent
from langchain.tools import tool

agent = create_agent(
    model="ollama:qwen3:8b",
    system_prompt="You are a helpful assistant, your task is to run unit tests and complexity analysis on the code provided.",
)    
