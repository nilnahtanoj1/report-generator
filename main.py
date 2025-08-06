from data_fetchers.news import get_recent_news
from data_fetchers.financials import get_financial_data
from data_fetchers.competitors import get_competitors
from llm.researcher import generate_research
from llm.summarizer import generate_persona_insight
from output.report_generator import generate_report
from utils.google_search import search_google_news


def main(company_name, persona):

    search_results = search_google_news(f"Recent news {company_name}")
    return
    news = get_recent_news(company_name, search_results)
    financials = get_financial_data(company_name)
    competitors = get_competitors(company_name)
    overview = generate_research(company_name, financials, search_results)
    insights = generate_persona_insight(company_name, persona, overview, news, financials)
    
    company_data = {
        "company_name": company_name,
        "persona": persona,
        "overview": overview,
        "news": news,
        "financials": financials,
        "competitors": competitors,
        "insights": insights
    }

    generate_report(company_data)
    
if __name__ == "__main__":
    company = input("Enter company name: ")
    persona = input("Enter target persona: ")
    main(company, persona)