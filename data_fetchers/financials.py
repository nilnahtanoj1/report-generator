import requests
import yfinance as yf
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import sys
import os
sys.path.insert(0, os.path.abspath('../Company Report Generator/utils'))
from resolve_ticker import _resolve_ticker

HEADERS = {
    "User-Agent": "Ricoh USA jonathan.lin@ricoh-usa.com"
}

def get_financial_data(company_name_or_ticker):
    try:
        ticker = _resolve_ticker(company_name_or_ticker)
        yahoo_data = _get_yahoo_financials(ticker)
        sec_data = _get_sec_10q_summary(ticker)
        
        return {
            "ticker": ticker,
            "market_cap": yahoo_data.get("market_cap"),
            "revenue": yahoo_data.get("revenue"),
            "net_income": yahoo_data.get("net_income"),
            "eps": yahoo_data.get("eps"),
            "filing_date": sec_data.get("filing_date"),
            "filing_type": sec_data.get("filing_type"),
            "filing_summary": sec_data.get("filing_summary"),
            "filing_url": sec_data.get("url")
        }
    
    except Exception as e:
        return e
    


def _get_yahoo_financials(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    return {
        "market_cap": info.get("marketCap"),
        "revenue": info.get("totalRevenue"),
        "net_income": info.get("netIncomeToCommon"),
        "eps": info.get("trailingEps")
    }
    
def _get_sec_10q_summary(ticker):
    cik = _get_cik_from_ticker(ticker)
    if not cik:
        return {}
    
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    res = requests.get(url, headers=HEADERS)
    data = res.json()
    
    filings = data.get("filings", {}).get("recent", {})
    for i in range(len(filings.get("form", []))):
        form = filings["form"][i]
        if form in ("10-Q", "10-K"):
            accession = filings["accessionNumber"][i].replace("-", "")
            filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/index.json"
            filing_res = requests.get(filing_url, headers=HEADERS)
            
            if filing_res.status_code != 200:
                continue
            
            filing_json = filing_res.json()
            for doc in filing_json.get("directory", {}).get("item", []):
                if doc["name"].endswith(".htm") and "10" in doc["name"]:
                    doc_name = doc["name"]
                    html_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{doc_name}"
                    summary = _summarize_sec_html(html_url, cik, accession)
                    return {
                        "filing_type": form,
                        "filing_date": filings["filingDate"][i],
                        "url": html_url,
                        "summary": summary
                    }
                    
    return {}

def _get_cik_from_ticker(ticker):
    cik_url = "https://www.sec.gov/files/company_tickers.json"
    res = requests.get(cik_url, headers=HEADERS)
    data = res.json()
    
    for _, entry in data.items():
        if entry["ticker"].lower() == ticker.lower():
            return str(entry["cik_str"]).zfill(10)
    return None

def _get_income_statement_from_sec(cik, accession):
    summary_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/FilingSummary.xml"
    res = requests.get(summary_url, headers=HEADERS)
    if res.status_code != 200:
        return "FilingSummary.xml not found"
    
    root = ET.fromstring(res.content)
    reports = root.findall(".//Report")
    
    income_stmt_url = None
    for report in reports:
        title = report.find("ShortName").text.lower()
        if "operations" in title or "income" in title:
            html_file = report.find("HtmlFileName").text
            income_stmt_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{html_file}"
            break
        
        if not income_stmt_url:
            return "Income Statement not found in FilingSummary.xml"
        
        res = requests.get(income_stmt_url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")
        table = soup.find("table")
        if not table:
            return "Income Statement table not found"

        return table.get_text(separator=" ", strip=True)[:1000] + "..."

def _summarize_sec_html(url, cik, accession):
    return _get_income_statement_from_sec(cik, accession)

if __name__ == "__main__":
    from pprint import pprint
    result = get_financial_data("amazon")
    pprint(result)