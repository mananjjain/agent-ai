from email.mime.text import MIMEText
from re import search

import speech_recognition as sr
import yfinance as yf
import pyttsx3
from dotenv import load_dotenv
from langchain_classic.agents import (
    initialize_agent,
    AgentType,
    tool,
    AgentExecutor,
    create_tool_calling_agent,
)
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
from datetime import date


load_dotenv()
llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
)
s = DuckDuckGoSearchRun()

print(llm.invoke("2+2"))


def speak(text):
    e = pyttsx3.init()
    e.say(text)
    e.runAndWait()


@tool
def time() -> str:
    """
    this function we sent you date and current news of the day this function will work if the input is does not have anything or if the asking anything of date

    """
    c = str(date.today())
    k = s.run(f"latest news of {c}")
    return f"date{c} ,news={k}"


@tool
def calculater(expression: str) -> str:
    """this funtion will return all the mathamatic problem
    for example-4*2=8
    """
    return str(eval(expression))


@tool
def searchh(text: str) -> str:
    "the is function will search  anything which is need to the user also provide best answer only by looking up to the internet except the date maths solveing and stock"
    k = s.run(text)
    return k


@tool
def stock(symbol: str) -> str:
    """
    Get current stock price.
    Example:
    RELIANCE.NS
    TCS.NS
    INFY.NS
    """
    stock = yf.Ticker(symbol)

    data = stock.history(period="1d")
    return data


prompt1 = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful AI assistant.

Use:
- calculater for math calculations
- time for date and news
- stock for stock prices and stock information

Always use the appropriate tool when needed.
""",
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
tools = [time, calculater, stock, searchh]
call = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt1)
ag = AgentExecutor(
    agent=call,
    tools=tools,
    verbose=True,
)


r = sr.Recognizer()
with sr.Microphone() as source:
    print("waitting for wakeup word")
    w = r.listen(
        source,
        timeout=10,
        phrase_time_limit=10,
    )
    wa = r.recognize_google(w).lower()
    if wa == "friday":
        speak("hi manan")
        print("hi manan")
        while True:
            with sr.Microphone() as source:
                print("listening....")
                a = r.listen(source, timeout=10, phrase_time_limit=10)
                t = r.recognize_google(a)
                speak(f"ok manan i will {t} on  and let you ")
                if t == "exit":
                    speak("by manan have a get day ")
                    break
            print("you said", t)
            rg = ag.invoke({"input": t})
            a = rg["output"]

            print(a)
            speak(a)
