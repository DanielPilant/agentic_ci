import typer
from pathlib import Path
from .agent import agent
from rich.console import Console
from rich.markdown import Markdown

console = Console()
app = typer.Typer()


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
    console.print(Markdown(result["messages"][-1].text))
    
    

def main():
    """
    Main entry point for the CLI application.
    """
    app()
    
    
    
    


if __name__ == "__main__":
    main()
