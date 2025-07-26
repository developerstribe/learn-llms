from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
import sys
import json
from pprint import pprint

cuisine = sys.argv[1] if len(sys.argv) > 1 else "uzbek"

chat = ChatOllama(model="qwen3:4b")

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
chat = chat.bind_tools(tools)
result = chat.invoke(f"{cuisine} cuisine restaurants")
pprint(f"🤖 Finding restaurants: {result}")
pick = ''
for tool_call in result.tool_calls:
    selected_tool = {t.name: t for t in tools}[tool_call["name"].lower()]
    tool_result = selected_tool.invoke(tool_call)
    pick = tool_result.content[0]

pprint(f"🍴 Selected restaurant: {pick}")
result = chat.invoke(f"how do I find {pick}")
pprint(f"🤖 Finding location for restaurant: {result}")
for tool_call in result.tool_calls:
    selected_tool = {t.name: t for t in tools}[tool_call["name"].lower()]
    tool_result = selected_tool.invoke(tool_call)
    location = tool_result.content

pprint(f"📍 Location for {pick}: {location}")

