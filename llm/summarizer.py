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
Company Overview:
{overview}

Recent News:
{news}

Financial Summary:
{financials}

You are a sales strategist assistant. Write a concise battlecard to help an account executive understand how to engage {persona} at {company} using the provided information.

In the battlecard, include:
1. What this persona at {company} likely cares about most right now.
2. Relevant challenges or strategic shifts they might be responding to.
3. How our offerings at Ricoh can align with their needs and priorities.

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
