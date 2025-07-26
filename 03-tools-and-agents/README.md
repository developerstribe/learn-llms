# Tools and agents

Now we are coming to the real meat and potatoes - instructing LLMs with tools. We look at two examples: building tools and attaching them to an agent that uses them.

## Setup

For preparing a Python environment, [uv](https://github.com/astral-sh/uv) is quickly becoming *the* tool (no pun intended).

```console
cd 03-tools-and-agents
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Be sure to pull `qwen3:4b` Ollama model too. That model capable of "thinking" and uses tools.

```console
ollama pull qwen3:4b
```

## Tools

When you look at anatomy of tools, they are like regular functions. A tool encompasses an operation that LLM might find relevant to user's input. The latest models are tool aware - checkout the [Ollama models](https://ollama.com/library?sort=newest) and see which ones support them.

To showcase, imagine an application that returns a restaurant and its location based on desired cuisine.

```console
16:20 $ python tools.py 
< logs >
Selected restaurant: Anjir
< logs >
Location for Anjir: 101 Uzbek St, Tashkent
```

In the source code, `tools.py`, choosing a restaurant and getting its location is mocked by two functions that are identified by model, which we then execute separately. IRL, each can be replaced by an IO operation (looking up nearest and highly rated restaurants using Google search, then finding its location coordinates with another map API) for legitimate use case.

Note the logs too - they show LLM's thinking process. Not all models support that, but they still can be tool aware. 

### Challenge
Try running `tools.py` with `llama3.2:3b` model.

## Agents

Agents are the climax of GenAI applications. Based on DAG, they orchestrate using the right tools - independently or via a defined workflow. Paired with thinking models, they form an assistant that's capable more than generating text - they can perform operations and make outbound requests.

In tools example above, we instructed a model to perform two operations. With agents, we can leave it up to an agent to do that. Let's try LangGraph provided ReAct agent for that. Excerpt from IBM[1]:

> What is a ReAct agent?
>
> A ReAct agent is an AI agent that uses the “reasoning and acting” (ReAct) framework to combine chain of thought (CoT) reasoning with external tool use. > The ReAct framework enhances the ability of a large language model (LLM) to handle complex tasks and decision-making in agentic workflows.

### Challenge

Run the `agent.py` script and see the result.

### References

[1] https://www.ibm.com/think/topics/react-agent