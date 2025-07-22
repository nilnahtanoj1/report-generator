import requests
import yfinance

HEADERS = {
    "User-Agent": "Ricoh USA jonathan.lin@ricoh-usa.com"
}
def _resolve_ticker(company_name: str) -> str | None:
    if not company_name or not isinstance(company_name, str):
        return None
    
    company_name = company_name.strip()
    if not company_name:
        return None
    
    base_url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {
        "q": company_name,
        "quotesCount": 1,
        "newsCount": 0
    }
    
    try:
        response = requests.get(base_url, params=params, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            return None
        
        data = response.json()
        
        quotes = data.get("quotes", [])
        if not quotes:
            return None
        
        ticker = quotes[0].get("symbol")
        return ticker
    
    except Exception as e:
        print(e)