from data_fetchers.company_info import get_company_overview
from data_fetchers.news import get_recent_news
from data_fetchers.financials import get_financial_data
from data_fetchers.competitors import get_competitors
from llm.summarizer import generate_persona_insight
from output.report_generator import generate_report

def main(company_name, persona):
    overview = get_company_overview(company_name)
    news = get_recent_news(company_name)
    financials = get_financial_data(company_name)
    competitors = get_competitors(company_name)
    insights = generate_persona_insight(company_name, persona, overview, news, financials)
    
    report = generate_report(
        company_name=company_name,
        persona=persona,
        overview=overview,
        news=news,
        financials=financials,
        competitors=competitors,
        insights=insights
    )
    print("Report Saved")
    
if __name__ == "__main__":
    company = input("Enter company name: ")
    persona = input("Enter target persona: ")
    main(company, persona)