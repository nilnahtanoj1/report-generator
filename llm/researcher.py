from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_research(company, financial_data, search_results):

    """
    Research Key Careabouts for a Customer's Business.
    """
    
    prompt = f"""
You are a research assistant. The following information regarding {company}'s financials are as follows: {financial_data} 
The following is background information for {company}: {search_results}

Answer the following questions about {company}. Include general information known about the company where relevant.

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

If you cannot answer any particular question, simply skip it and move on. If you cannot answer any of the questions, simply do not respond.
Do not mention or say that you cannot answer a particular question. Do not justify why you cannot answer any particular question. Do your best
to answer the questions where possible.

Do not add any header or footer introductions or suggestions (such as 'I am an AI assistant'). The output should exclusively consist of the answers
to the questions above, and nothing more.
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
