from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
from utils.google_search import search_google_news

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_research(company, financial_data, search_results):

    """
    Research Key Careabouts for a Customer's Business.
    """
    
    prompt = f"""
You are a research assistant. The following information regarding {company}'s financials are as follows: {financial_data} 
The following is some background information for {company}: {search_results}

Answer the following questions about {company}.

Top 5 things to know about {company} including top customers for each business unit.
How is the current geopolitical environment impacting {company}?
How does {company} compare with its competitors?
What are the key strenghts of {company}?
What challenges does {company} face, and what impact do these challenges have on their growth? What strategies are they using to mitigate these impacts? How effective are these strategies?
What competitive differentiation does {company} have?
Are there any recent initiatives or projects started by {company}?
What are the forecasts for future revenue growth?
How do these forecasts compare with their competitors?
What are some highlights from the last investor day presentation (if applicable)
Compare the last two 10Qs of {company} in table format.
Compare the latest 10Qs of the top 3 competitors with {company} in table format.
Summarize the differences in 5 key points.
Give a YOY comparison by business unit on revenue and margin for the last 3 years.
What digital transformation and operational efficiency initiatives are planned by {company} for the upcoming year?
What digital transformation and operational efficiency initiatives did {company} complete over the past 3 years?
Who is responsible for digital transformation, OE/EX/CX within {company}?


Do not include any words or phrasing in the output that would imply that you are an AI or that you are unable to answer the questions.
If you cannot answer any particular question, simply skip it and move on.
"""

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a research assistant, whose job is to answer questions about a company."},
                {"role": "user", "content": prompt}
                ],
        
    )
        return response.choices[0].message.content
    
    except OpenAIError as e:
        return f"Error generating insight: {str(e)}"
