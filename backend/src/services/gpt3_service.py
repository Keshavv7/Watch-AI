import openai

def generate_responses(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    
    return response.choices[0].text.strip()
