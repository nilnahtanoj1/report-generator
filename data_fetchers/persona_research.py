from utils.google_search import search_google_news
from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def get_persona_info(company, name, role):
    search_results = search_google_news(f"{name} {role} {company} site:linkedin.com OR site:crunchbase.com OR site:twitter.com OR site:youtube.com OR site:podchaser.com")

    """
    Research Key Careabouts for a Customer's Business.
    """
    
    prompt = f"""
{search_results}

You are a research assistant. Use the given information to build a persona for {name} {role} who works at {company}. Include any
careabouts, business implications and likely decisions that the individual might consider, given their work history and initiatives.

Do not include any words or phrasing in the output that would imply that you are an AI or that you are unable to answer the questions.
If you cannot answer any particular question, simply skip it and move on.
"""

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a research assistant, whose job is to build a business profile about an individual."},
                {"role": "user", "content": prompt}
                ],
        
    )
        return response.choices[0].message.content
    
    except OpenAIError as e:
        return f"Error generating insight: {str(e)}"