from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool
from langchain.schema import  AIMessage, HumanMessage, SystemMessage
from langchain.tools import format_tool_to_openai_function
from pydantic import BaseModel, Field

from .ingress import qdrant

chat = ChatOpenAI(temperature=0)

system_prompt ='you find relevant research papers based on the users needs'

_get_system_prompt = lambda : SystemMessage(content=system_prompt)
    

tools = [
    Tool.from_function(
        func=qdrant.similarity_search,
        name="SimilarSearch",   
        description="usefull to find a paper similar to an exzerpt of another paper",
    ),
    Tool.from_function(),
]   


functions = [format_tool_to_openai_function(tool) for tool in tools]




