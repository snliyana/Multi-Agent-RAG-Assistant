from backend.app.tools.finance_tools import get_stock_info


result = get_stock_info.invoke(
    {
        "ticker": "NVDA"
    }
)


print("\n--- FINANCE TOOL RESULT ---")
print(result)