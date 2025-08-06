from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
from utils.google_search import search_google_news

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_recent_news(company, search_results):

    """
    Research Competitors of Company
    """
    
    prompt = f"""
You are a research assistant. Here are some google results for recent news related to {company}: {search_results}

Present findings in a concise list of 3-5 recent news or events that are relevant or directly related to {company}. Briefly summarize each
event and its implications towards the business and outlook of {company}. Keep the output short, and do not add additional filler, introductory fluff (such as "Here is a list
of the top 3 competitors, etc.), or AI footer fluff (such as "Do you need any additional information or help?")

"""

    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a research assistant, whose job is to uncover competitor information."},
                {"role": "user", "content": prompt}
                ],
        
    )
        return response.choices[0].message.content
    
    except OpenAIError as e:
        return f"Error generating insight: {str(e)}"
