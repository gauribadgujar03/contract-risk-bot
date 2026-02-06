import openai

openai.api_key = "YOUR_API_KEY"

def explain_clause(clause):
    prompt = f"""
    Explain the following legal clause in simple business language
    and mention potential risks:

    Clause:
    {clause}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
