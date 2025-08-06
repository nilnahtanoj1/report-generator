from data_fetchers.news import get_recent_news
from data_fetchers.financials import get_financial_data
from data_fetchers.competitors import get_competitors
from llm.researcher import generate_research
from llm.summarizer import generate_persona_insight
from output.report_generator import generate_report
from utils.google_search import search_google_news
from data_fetchers.persona_research import get_persona_info


def main(company, name, role):

    search_results = search_google_news(f"Recent news {company}")
    persona = get_persona_info(company, name, role)
    news = get_recent_news(company, search_results)
    financials = get_financial_data(company)
    competitors = get_competitors(company)
    overview = generate_research(company, financials, search_results)
    insights = generate_persona_insight(company, persona, overview, news, financials)
    
    company_data = {
        "company_name": company,
        "persona": name,
        "overview": overview,
        "news": news,
        "financials": financials,
        "competitors": competitors,
        "insights": insights
    }

    generate_report(company_data)
    
if __name__ == "__main__":
    company = input("Enter company name: ")
    name = input("Enter target name: ")
    role = input("Enter target role: ")
    main(company, name, role)