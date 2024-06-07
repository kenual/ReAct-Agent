from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.tools.wikipedia import WikipediaToolSpec

llm = Ollama(model="phi3", request_timeout=60)
agent = ReActAgent.from_tools(WikipediaToolSpec().to_tool_list(), llm=llm, verbose=True)

response = agent.chat("What is LlamaIndex?")
print(response)