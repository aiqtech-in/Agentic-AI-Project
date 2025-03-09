from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tool = TavilySearchResults(max_results=2)
    return [tool]   #add extra tool if needed as comma separated entries

def create_tool_node(tools):
    """
    Create and return tool node for the graph
    """
    return ToolNode(tools=tools)


