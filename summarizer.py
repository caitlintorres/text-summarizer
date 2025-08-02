import openai
import os
from dotenv import load_dotenv
import argparse

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes long text into concise summaries."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        temperature=0.5,
        max_tokens=500
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    parser = argparse.ArgumentParser(description="Summarize text using OpenAI")
    parser.add_argument("input_file", help="Path to text file containing the input")
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        long_text = f.read()

    summary = summarize_text(long_text)
    print("\n--- Summary ---\n")
    print(summary)

if __name__ == "__main__":
    main()
