from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]


class CountryWithNeighbors(Country):
    neighbors: list[Country] = Field(
        description="List of neighboring countries"
    )


model = (
    ChatOllama(model="llama3.2:3b", temperature=0.1)
    .with_structured_output(CountryWithNeighbors)
)

system_message = """You are a helpful assistant that given information about \
a country and list of it's neighbors. You MUST return information for the \
neighbors in the same format as the country."""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", "Tell me about {country}"),
])

chain = prompt | model
country = chain.invoke({"country": "Uzbekistan"})
print(country)

# Output
"""
name='Uzbekistan' capital='Tashkent' languages=['Uzbek'] 
neighbors=[
    Country(name='Afghanistan', capital='Kabul', languages=['Dari', 'Pashto']), 
    Country(name='Kazakhstan', capital='Astana', languages=['Kazakh']), 
    Country(name='Kyrgyzstan', capital='Bishkek', languages=['Kyrgyz']), 
    Country(name='Tajikistan', capital='Dushanbe', languages=['Tajik']), 
    Country(name='Turkmenistan', capital='Ashgabat', languages=['Turkmen'])
]
"""