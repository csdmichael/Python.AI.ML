from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI # type: ignore
import os

#os.environ["SERPAPI_API_KEY"] = "" # get your Serp API key here: https://serpapi.com/

OpenAI.api_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("How much energy did wind turbines produce worldwide in 2022?")