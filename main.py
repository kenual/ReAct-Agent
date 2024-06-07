from llama_index.core import set_global_handler
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec

set_global_handler("simple")

llm = Ollama(model="phi3", request_timeout=60)
agent = ReActAgent.from_tools(
    DuckDuckGoSearchToolSpec().to_tool_list(), llm=llm, verbose=True)

if __name__ == "__main__":
    while True:
        user_input = input('Enter query> ')
        if user_input.lower() in ['', 'exit', 'quit']:
            break
        
        response = agent.chat("user_input")
        print(response)
