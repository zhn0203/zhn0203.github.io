import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_summary(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You summarize key information from user queries."},
            {"role": "user", "content": f"Summarize this topic: {prompt}"}
        ]
    )
    return completion.choices[0].message['content']
