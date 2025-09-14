# tools.py
from langchain.tools import Tool
from langchain.utilities import DuckDuckGoSearchAPIWrapper
# from langchain.utilities import SerpAPIWrapper  # Optional alternative

def calculator_tool() -> Tool:
    """
    Calculator tool that evaluates Python expressions.
    """
    def calculate(expr: str) -> str:
        try:
            # Warning: eval can be unsafe if inputs are untrusted
            result = eval(expr)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    return Tool(
        name="Calculator",
        func=calculate,
        description="Use this tool to perform mathematical calculations. Input should be a valid Python expression."
    )

def search_tool() -> Tool:
    """
    Search tool using DuckDuckGo.
    """
    search = DuckDuckGoSearchAPIWrapper()

    def search_query(query: str) -> str:
        results = search.run(query)
        return results

    return Tool(
        name="Search",
        func=search_query,
        description="Use this tool to search the web for answers to questions. Input should be a search query."
    )

def get_tools(use_search: bool = True) -> list:
    """
    Return a list of LangChain tool objects.
    """
    tools = [calculator_tool()]
    if use_search:
        tools.append(search_tool())
    return tools
