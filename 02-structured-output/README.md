# Developing with LLMs

Developing a GenAI application involved choosing a framework or library to communicate with LLM and translate into programmable objects. Popular options are:

- LangChain
- Semantic Kernel
- LlamaIndex
- Haystack

We will use LangChain's Python SDK to interact with Ollama model.

## Structured output

Normally, models respond to questions in natural language. When building applications, developer needs object representation of that response to process it further. For that case, models can be instructed to output in structured format. 

Checkout `structured.py`. It starts off by importing LangChain modules for working with Ollama. Pydantic is well-established library that validates and forms the desired structure. The system message we pass to LLM "nudges" it to generate answers in expected format.

### Running the Python code

```console
# Init virtualenv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python structured.py
name='Uzbekistan ...
```

Note: I skipped an intro to LangChain, I hope it's generic usage is obvious from the example.

## Next

The [next course](../03-tools-and-agents/README.md) will show practical example of generating structured outputs that can be used in an application.


## References

- [Ollama with LangChain](https://python.langchain.com/docs/integrations/chat/ollama/)
- [Structured outputs in LangChain](https://python.langchain.com/docs/concepts/structured_outputs/)