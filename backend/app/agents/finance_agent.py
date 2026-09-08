from langchain_groq import ChatGroq
from langchain.agents import create_agent

from backend.app.tools.finance_tools import get_stock_info


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


finance_agent = create_agent(
    model=llm,
    tools=[get_stock_info],
    system_prompt="""
You are a finance and stock market specialist.

When the user asks about stock prices, market capitalization,
52-week highs or lows, or other company stock information,
use the get_stock_info tool.

Do not guess current financial data.

If the user gives a company name instead of a ticker symbol,
determine the appropriate ticker when you are confident.

After receiving tool data, explain it clearly and concisely.

Do not present the response as personalized financial advice.
"""
)