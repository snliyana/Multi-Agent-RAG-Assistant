import yfinance as yf

from langchain_core.tools import tool


@tool
def get_stock_info(ticker: str) -> str:
    """
    Get current stock market information for a company ticker symbol.

    Examples:
    AAPL for Apple
    MSFT for Microsoft
    NVDA for Nvidia
    GOOGL for Alphabet
    TSLA for Tesla
    """

    try:
        stock = yf.Ticker(ticker.upper())

        info = stock.info

        company_name = info.get("longName", ticker.upper())
        current_price = info.get("currentPrice")
        previous_close = info.get("previousClose")
        market_cap = info.get("marketCap")
        fifty_two_week_high = info.get("fiftyTwoWeekHigh")
        fifty_two_week_low = info.get("fiftyTwoWeekLow")
        currency = info.get("currency", "USD")

        return (
            f"Company: {company_name}\n"
            f"Ticker: {ticker.upper()}\n"
            f"Current Price: {current_price} {currency}\n"
            f"Previous Close: {previous_close} {currency}\n"
            f"Market Cap: {market_cap}\n"
            f"52 Week High: {fifty_two_week_high} {currency}\n"
            f"52 Week Low: {fifty_two_week_low} {currency}"
        )

    except Exception as e:
        return f"Unable to retrieve stock information: {str(e)}"