import typer
from langchain.agents import create_agent
from langchain.tools import tool
app = typer.Typer()

from pathlib import Path

agent = create_agent(
    model="ollama:qwen3:8b",
    system_prompt="You are a helpful assistant, your task is to run unit tests and complexity analysis on the code provided.",
)    




@app.command()
def lines_counter(file_path: str = typer.Argument(help="Path to the file to count lines")):
    """
    Count the number of lines in a file.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            line_count = sum(1 for line in file)
            typer.echo(line_count)
    except:
        typer.echo("File path not found")


# command that sends a code file to an LLM model for testing and returns the results of the test
@app.command()
def code_tester(file_path: str = typer.Argument(help="Path to the file to test code")):
    
    """
    Test the code of the LLM. provides unit tests and code complexity with agentic LLM models.
    """
    typer.echo("Testing code generation with LLM...")
    code = Path(file_path).read_text(encoding="utf-8")
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": f"Please test the code in the file located at {file_path}, witch have the code {code}. Provide unit tests and analyze the code complexity."
        }]
    })
    typer.echo(result["messages"][-1].text)
    
    

def main():
    """
    Main entry point for the CLI application.
    """
    app()
    
    
    
    


if __name__ == "__main__":
    main()
