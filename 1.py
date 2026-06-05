from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool


load_dotenv()

llm = ChatOllama(model="qwen3", temperature=0)

# tools = load_tools(["llm-math", "ddg-search"], llm=llm)

# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
#     handle_parsing_errors=True,
# )

# print(
#     agent.run(
#         "Tom M. Mitchell is an American computer scientist \
# and the Founders University Professor at Carnegie Mellon University (CMU)\
# what book did he write?"
#     )
# )
a = create_python_agent(llm=llm, tool=PythonREPLTool(), verbose=True)
customer_list = [
    ["Harrison", "Chase"],
    ["Lang", "Chain"],
    ["Dolly", "Too"],
    ["Elle", "Elem"],
    ["Geoff", "Fusion"],
    ["Trance", "Former"],
    ["Jen", "Ayai"],
]
print(
    a.run(
        f"given list of customers{customer_list},sort the list last name wise and return the sorted list"
    )
)
