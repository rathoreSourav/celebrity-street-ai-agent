import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_funny_line(celeb, activity, location):
    prompt = (
        f"{celeb} is {activity} {location}. Write a short, funny Hindi one-liner for a viral Instagram reel. "
        "Make it sound like something a street-smart person would say. Keep it under 20 words."
    )

    try:
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
            max_tokens=60
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return "Arre bhai, content toh AI bhi thak gaya banate banate!"
