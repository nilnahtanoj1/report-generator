import openai

def generate_persona_insight(company, persona, overview, news, financials):
    prompt = f"""
You are a B2B sales strategist. Your task is to write a short internal briefing for targeting {persona} at {company}.

Company Overview:
{overview}

Recent News:
{news}

Financial Summary:
{financials}

Write an analysis outlining:
1. What the {persona} at {company} cares about.
2. What recent changes or challenges they might be facing.
3. How our products and services can align with their goals.
"""

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    
    return response['choices'][0]['message']['content']