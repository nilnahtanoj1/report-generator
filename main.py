#from data_fetchers.company_info import get_company_overview
#from data_fetchers.news import get_recent_news
#from data_fetchers.financials import get_financial_data
#from data_fetchers.competitors import get_competitors
from llm.summarizer import generate_persona_insight
from output.report_generator import generate_report
from llm.researcher import generate_research

def main(company_name, persona):
    # overview = get_company_overview(company_name)
    # news = get_recent_news(company_name)
    # financials = get_financial_data(company_name)
    # competitors = get_competitors(company_name)
    

    overview = generate_research(company_name)
    news = """📰 Recent News Highlights
Underwriting Profit Turns Positive in 2024

In 2024, American Family Insurance reversed losses from previous years, reporting a combined ratio of 96.6%, down from 110.8% in 2023. The company earned an underwriting profit of $603 million and total revenue increased to $20.0 billion, largely driven by premium rate increases and investment income. Direct written premiums rose 13.9% to $19.6 billion
PR Newswire+15newsroom.amfam.com+15newsroom.amfam.com+15
.
Moody’s Rating Downgrade with Stable Outlook

In May 2024, Moody’s downgraded American Family’s Insurance Financial Strength (IFS) rating from A1 to A2, citing recent net losses and higher capital strain. However, the outlook remains stable, with positive signs from improved underwriting and expense reductions
ReinsuranceNe.ws
.
Raising the Wage Floor

Effective January 1, 2025, American Family raised its minimum hourly pay to $25, its third increase since 2020. This move supports recruitment and retention across agency and customer-facing roles and is part of broader employee benefit improvements, including expanded parental leave
newsroom.amfam.com+1Carrier Management+1
.
New Partnership with Empathy Platform

On April 23, 2025, the company announced a collaboration between American Family Insurance Life Company and Empathy. It offers beneficiaries of life insurance policies complimentary access to grief, care, and administrative support services
newsroom.amfam.com
.
Disaster Relief and Community Aid

American Family responded to severe hailstorms and tornadoes by providing emergency assistance. In April 2025, it offered direct support to affected customers in Wisconsin and Missouri, through both financial aid and partnerships via the Dreams Foundation
newsroom.amfam.com
.
Spin-Off of PropTech Startup Fixle

Fixle, Inc. — a platform formerly incubated within American Family Insurance — was launched as an independent PropTech startup in February 2024. American Family Ventures remains a minority investor in the company, which offers streamlined home maintenance and management solutions
ReinsuranceNe.ws
PR Newswire
.
PGA TOUR Champions: New Format & Venue

The American Family Insurance Championship will adopt a team-style “scramble” format for the 2025 PGA TOUR Champions event and move to TPC Wisconsin in Madison. The three-day event takes place June 6–8 and features a $3M purse
AmFam Championship
.
Internal Practice Controversy

American Family has tied claims adjuster compensation—including performance ratings and job security—to the percentage of repairs sent to shops in its Direct Repair Program (DRP). Though internal pushback flagged compliance risks, the practice persisted into 2025
Reddit
."""
    financials = """Q1 2025 (Quarter Ended March 31, 2025)

    Net income: ~$74.2 million, or $0.71 per diluted share, up from $46.7 million (or $0.45 per share) a year ago
    Reddit+7newsroom.amfam.com+7newsroom.amfam.com+7
    SEC
    .

    The company returned over $290 million to shareholders through dividends and share repurchases in Q1
    SEC
    .

    Management noted significant excess capital as of March 31, 2025, supporting continuing returns and reinvestment in the business
    SEC
    .

📅 Q4 2024 (Full Year 2024 Highlights)

    Total revenue: $20.0 billion, up 17% from 2023.

    Direct written premiums: $19.6 billion, up 13.9%.

    Combined ratio (P&C): improved to 96.6%, reversing a loss-making trend from a combined ratio of 110.8% in 2023.

    Underwriting profit (P&C): $603 million, compared to an underwriting loss of $1.7 billion in 2023.

    Expense ratio: declined to 33.1%, roughly 3.9 points lower than the prior year.

    Net income (after tax): $2.5 billion, a turnaround from a net loss of nearly $900 million in 2023.

    Members’ equity: grew to $10.6 billion, compared to $8.0 billion at the end of 2023.

    Total group assets: rose to about $42.2 billion
    ycharts.com+5newsroom.amfam.com+5Carrier Management+5
    Carrier Management
    newsroom.amfam.com
    .

    Life insurance segment gain from operations: $129 million, down slightly from $150 million in 2023.

    Pretax investment income surged ~70% to $1.6 billion, including realized investment gains of $1.3 billion after a prior-year loss
    Carrier Management+1newsroom.amfam.com+1
    ."""
    competitors = """1. State Farm
Overview:

    Type: Mutual insurance company

    Founded: 1922

    Headquarters: Bloomington, Illinois

    Employees: ~58,000

    Annual Revenue (2024 est.): Over $104 billion

Why It Competes:

    Largest auto and home insurer in the U.S. by market share

    Massive network of ~19,000 exclusive agents

    Strong customer loyalty from brand recognition and wide agent footprint

Key Strengths:

    Broad product suite: Auto, homeowners, renters, life, health, banking

    Highly competitive pricing, especially in auto

    Substantial surplus capital to weather catastrophic loss years

    Technologically enhanced claims and underwriting systems

2. Allstate
Overview:

    Type: Publicly traded (NYSE: ALL)

    Founded: 1931

    Headquarters: Northbrook, Illinois

    Employees: ~53,000

    Annual Revenue (2024): $57.2 billion

Why It Competes:

    Strong national brand, especially in auto and homeowners insurance

    Diversified with Encompass, Esurance, and new digital offerings

Key Strengths:

    Rapid digital transformation and use of AI for pricing and claims

    Expanding direct-to-consumer models, reducing dependence on agents

    Strategic acquisitions in telematics and tech (e.g., Milewise)

    Aggressive cost-cutting and focus on higher-margin segments

3. Liberty Mutual
Overview:

    Type: Mutual insurance company

    Founded: 1912

    Headquarters: Boston, Massachusetts

    Employees: ~45,000

    Annual Revenue (2024 est.): $50–55 billion

Why It Competes:

    A top-tier personal and commercial lines insurer, with strong international presence

    Operates under multiple brands including Safeco, a direct competitor to American Family’s nonstandard and digital lines

Key Strengths:

    Major commercial insurance business alongside strong personal lines

    Strategic use of partners and independent agents

    Strong catastrophe management and reinsurance structuring

    Expanding global footprint (Latin America, Europe, Asia-Pacific)"""

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