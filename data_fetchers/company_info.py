import requests
import yfinance as yf
import sys
import os
sys.path.insert(0, os.path.abspath('../Company Report Generator/utils'))
from resolve_ticker import _resolve_ticker

HEADERS = {
    "User-Agent": "Ricoh USA jonathan.lin@ricoh-usa.com"
}

def get_company_profile(company_name_or_ticker: str) -> dict:
    ticker = _resolve_ticker(company_name_or_ticker)
    
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        return {
            "name": info.get("longName", info.get("shortName", ticker)),
            "ticker": ticker,
            "industry": info.get("industry"),
            "sector": info.get("sector"),
            "website": info.get("website"),
            "description": info.get("longBusinessSummary"),
            "ceo": info.get("companyOfficers", [{}])[0].get("name"),
            "employees": info.get("fullTimeEmployees"),
            "market_cap": info.get("marketCap")
        }
        
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    from pprint import pprint
    result = get_company_profile("amazon")
    pprint(result)