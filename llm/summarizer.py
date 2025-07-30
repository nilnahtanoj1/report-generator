from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_persona_insight(company, persona, overview, news, financials):
    """
    Generates a B2B sales insight report for a target persona at a given company.
    """
    
    prompt = f"""
You are a B2B sales strategist. Write a concise internal briefing to help an account executive understand how to engage {persona} at {company}.

Company Overview:
{overview.strip()}

Recent News:
{news.strip()}

Financial Summary:
{financials.strip()}

In your briefing, include:
1. What this persona at {company} likely cares about most right now.
2. Relevant challenges or strategic shifts they might be responding to.
3. How our offerings can align with their needs and priorities.

Keep the tone professional, clear, and actionable. Limit the response to 3-5 paragraphs.
"""

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a strategic B2B sales assistant."},
                {"role": "user", "content": prompt}
                ],
        
    )
        return response.choices[0].message.content
    
    except OpenAIError as e:
        return f"Error generating insight: {str(e)}"
