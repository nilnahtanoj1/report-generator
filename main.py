#from data_fetchers.company_info import get_company_overview
#from data_fetchers.news import get_recent_news
#from data_fetchers.financials import get_financial_data
#from data_fetchers.competitors import get_competitors
from llm.summarizer import generate_persona_insight
from output.report_generator import generate_report

def main(company_name, persona):
    # overview = get_company_overview(company_name)
    # news = get_recent_news(company_name)
    # financials = get_financial_data(company_name)
    # competitors = get_competitors(company_name)
    

    overview = """🏢 Company Overview

    Name: Amazon.com, Inc.

    Founded: July 5, 1994

    Founder: Jeff Bezos

    Headquarters: Seattle, Washington, USA (though recently expanding to other HQs like Arlington, Virginia)

    CEO (as of 2025): Andy Jassy (since July 2021, following Jeff Bezos)

📦 Core Business Segments

    E-Commerce

        Started as an online bookstore.

        Now sells everything from electronics and clothing to groceries and furniture.

        Operates retail websites for several countries and sells globally.

    Amazon Web Services (AWS)

        Launched in 2006.

        Cloud computing platform — offers storage, servers, databases, machine learning, and more.

        One of Amazon’s most profitable divisions.

    Amazon Prime

        Subscription service ($/month or annually).

        Offers free/fast shipping, Prime Video, Prime Music, and other perks.

        Over 200 million members globally.

    Digital Media & Devices

        Products like Kindle, Echo (Alexa), Fire TV, and tablets.

        Develops original content via Amazon Studios for Prime Video.

    Logistics & Fulfillment

        Owns and operates warehouses, delivery trucks, aircraft, and drones.

        Has built a massive last-mile delivery network that rivals traditional carriers.

    Physical Stores

        Owns Whole Foods Market (acquired in 2017).

        Amazon Go (checkout-free stores) and Amazon Fresh (grocery).

    Advertising

        Offers targeted ads based on shopping and browsing behavior.

        Fast-growing revenue stream, often compared with Google and Meta ads.

🌍 Global Reach

    Operates marketplaces in over a dozen countries.

    Ships to over 100 countries worldwide.

    Faces strong local competition in places like China and India.

💰 Financial Highlights (as of late 2024)

    Market Cap: Over $1.7 trillion (fluctuates with market).

    Employees: ~1.5 million.

    Revenue: Over $500 billion annually.

    Profit Drivers: AWS, Advertising, and Prime.

🔍 Controversies & Criticisms

    Labor practices and warehouse working conditions.

    Antitrust investigations in the U.S. and EU.

    Environmental impact and sustainability challenges.

    Market dominance affecting small businesses.

🧭 Mission Statement

    "To be Earth’s most customer-centric company, where customers can find and discover anything they might want to buy online.""

"""
    news = """1. Q2 2025 Earnings Preview

    Amazon is set to release its Q2 2025 earnings on July 31, with investor attention on whether last quarter’s strong performance was repeatable. Analysts anticipate earnings per share of $1.33 and ~9.5–10% revenue growth, projecting revenue around $162 billion and ~17% growth in AWS revenue
    Business Insider+15Reuters+15Reddit+15
    Business Insider+3MarketWatch+3Investors.com+3
    .

    Competitor tension in AI and cloud services is mounting, as AWS faces pressure from Google and Microsoft
    Business Insider+2Reuters+2MarketWatch+2
    .

2. Digital Advertising Shake-Up

    Amazon abruptly halted its spending on Google Shopping ads globally as of July 2025, sending ripples through the advertising ecosystem
    WebProNews
    .

3. Pricing Transparency Probe

    Senator Maggie Hassan has sent a letter to Amazon's CEO requesting internal data on grocery price hikes tied to tariffs, especially regarding impacts on SNAP shoppers. Amazon disputes the data used in the report and will respond by August 20 .

4. Robotics Surge in UK Warehouses

    Amazon plans to reach robot-to-human parity in its UK warehouses within three years, supported by a £40 billion investment. The shift is expected to automate repetitive tasks while reskilling workers .

5. Seller Feedback System Revamp

    Starting July 29, Amazon will no longer require written customer feedback for sellers—moving to a “star-only” rating system to streamline reviews .

6. New Logistics Hub in Little Rock

    On July 29, Amazon broke ground on a 930,000-ft² logistics facility in Arkansas, expected to create over 1,000 full-time jobs .

7. AI Licensing Deal with The New York Times

    Amazon signed a multi-year deal worth $20–25 million per year with The New York Times to license its content for AI training and integration into services like Alexa—marking a first for both the publisher and Amazon .

8. Prime Day 2025 Recap

    Amazon’s July Prime Day (July 8–11) was its biggest-ever, generating record U.S. e‑commerce spend: $7.9 billion on day one, and estimated $23.8 billion total for the four-day event .

    Independent sellers, powered by exclusive launches like Alexa+, performed exceptionally well—reporting substantial visibility and sales growth """


    financials = """Q1 2025 Results (Reported May 1, 2025)

    Net sales: $155.67 billion (+9% YoY), slightly beating expectations
    Reddit+7Business Insider+7Financial Times+7

    Earnings per share (EPS): $1.59, outperforming consensus estimates
    Business Insider

    Operating income: $18.41 billion — well above forecasts, driven by retail strength, AWS, and advertising
    Reddit+2Business Insider+2Reddit+2

    Advertising revenue: grew ~19%, contributing meaningfully to margins

    AWS revenue growth: ~17% YoY, slightly below expectations

🔮 Q2 2025 Guidance (Expected on July 31, 2025)

    Projected net sales: $159 billion–$164 billion, up ~7–11% YoY vs. Q2 2024

    Projected operating income: $13 billion–$17.5 billion, below analyst consensus (~$17.7 billion)

📈 Analyst Expectations & Market Sentiment

    Revenue consensus: ~$162 billion (≈ +9% YoY)

    EPS estimate: ~$1.33

    AWS growth: around 17% YoY, remaining a key profit engine (~60% of company profit)

    Analyst targets: Price targets range from $265 up to $300+, citing AWS/Cloud, Prime momentum, ad growth, and AI investments

🧾 2024 Full-Year Financial Highlights

    Total revenue: $638 billion (+11% vs. prior year)

        North America: $387 billion (+10%)

        International: $143 billion (+9%)

        AWS: $108 billion (+19%)

    Operating income: $68.6 billion (10.8% margin vs. 6.4% prior year)

    Free Cash Flow (adjusted): $36.2 billion (slightly improved over 2023)

⚠️ Key Drivers & Risks

    Tariff-related headwinds: Amazon cited trade war uncertainty, particularly U.S.–China tariffs, as a risk to e-commerce profitability. Some sellers stockpiled inventory or negotiated discounts to mitigate impacts

    Capital expenditures: Amazon plans $100 billion of investment in 2025, particularly in AI-related infrastructure and Project Kuiper satellite ambitions

    AWS margin pressure: Operating margin is expected to decline in Q2 as AWS invests for scale; anticipated margin range ~28–39%, consensus ~37% for full year """
    
    competitors = "competitors"

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