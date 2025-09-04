from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from agent_system.fetcher import fetch_stock
from agent_system.analyzer import analyze_stock
from agent_system.advisor import advisor

def run_agent(query):
    tools = [
        Tool(name="Stock Fetcher", func=fetch_stock, description="Fetch stock price"),
        Tool(name="Stock Analyzer", func=analyze_stock, description="Analyze stock trend"),
        Tool(name="Stock Advisor", func=advisor, description="Recommend Buy/Sell")
    ]
    
    llm = OpenAI(temperature=0)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    
    return agent.run(query)

