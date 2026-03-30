import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_cultural_note(transcript):
    prompt = f"Extract cultural references and provide a brief cultural note based on the following transcript:\n\n{transcript}\n\nCultural Note:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    transcript = input("Paste a short transcript: ")
    cultural_note = generate_cultural_note(transcript)
    print("\n Cultural Note:")
    print(cultural_note)
