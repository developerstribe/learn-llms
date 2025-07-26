from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
import sys
import json
from pprint import pprint


cuisine = sys.argv[1] if len(sys.argv) > 1 else "uzbek"

chatModel = ChatOllama(model="qwen3:4b")

# Load JSON data once
with open('data.json', 'r') as f:
    restaurant_data = json.load(f)

@tool
def get_restaurants(cuisine: str) -> list:
    """Get a list of restaurants based on the specified cuisine."""
    cuisine = cuisine.lower()
    if cuisine in restaurant_data:
        return list(restaurant_data[cuisine].keys())
    return [f"No restaurants found for cuisine: {cuisine}"]

@tool
def get_location(restaurant: str) -> str:
    """Get the location of a specified restaurant."""
    restaurant = restaurant.lower()
    for cuisine_data in restaurant_data.values():
        for rest_name, location in cuisine_data.items():
            if rest_name.lower() == restaurant:
                return location
    return "Location not found for this restaurant"

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

tools = [get_restaurants, get_location, add]
chatModel = chatModel.bind_tools(tools)
agent_executor = create_react_agent(chatModel, tools=tools)
result = agent_executor.invoke({"messages": [f"one of the {cuisine} cuisine restaurants and its location"]})
pprint(result)
