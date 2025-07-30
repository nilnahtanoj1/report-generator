from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_research(company):
    """
    Research Key Careabouts for a Customer's Business.
    """
    
    prompt = f"""
You are a research assistant. Answer the following questions about {company}.

1. Top 5 things to know about {company} including top customers for each business unit.
2. How is the current geopolitical environment impacting {company}?
3. How does {company} compare with its competitors?
4. What are the key strenghts of {company}?
5. What challenges does {company} face, and what impact do these challenges have on their growth? What strategies are they using to mitigate these impacts? How effective are these strategies?
6. What competitive differentiation does {company} have?
7. Are there any recent initiatives or projects started by {company}?
8. What are the forecasts for future revenue growth?
9. How do these forecasts compare with their competitors?
10. What are some highlights from the last investor day presentation (if applicable)
11. Compare the last two 10Qs of {company} in table format.
12. Compare the latest 10Qs of the top 3 competitors with {company} in table format.
13. Summarize the differences in 5 key points.
14. Give a YOY comparison by business unit on revenue and margin for the last 3 years.
15. What digital transformation and operational efficiency initiatives are planned by {company} for the upcoming year?
16. What digital transformation and operational efficiency initiatives did {company} complete over the past 3 years?
17. Who is responsible for digital transformation, OE/EX/CX within {company}?

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
