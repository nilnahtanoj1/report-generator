from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def get_competitors(company):
    """
    Research Competitors of Company
    """
    
    prompt = f"""
You are a research assistant. Discover and do background research on the top 3 competitors for {company}.

Present findings in a concise list of 3 competitors, with a short description of each one, including high level
financial and leadership information, as well as 1-2 key competitive differentiations between {company} and each
competitor. Keep the output short, and do not add additional filler, introductory fluff (such as "Here is a list
of the top 3 competitors, etc.), or AI footer fluff (such as "Do you need any additional information or help?")

"""

    try:
        client = OpenAI(api_key=api_key)
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
