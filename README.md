# 🧠 Text Summarizer

A simple AI-powered command-line tool that summarizes long-form text using OpenAI’s GPT models.

---

## ✨ Features

- 🔍 Summarizes large text files into short, readable summaries
- 🧠 Uses OpenAI GPT-3.5 or GPT-4 under the hood
- 🧪 Easy-to-use CLI
- 🔐 Secure API key handling via environment variable

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/caitlintorres/text-summarizer.git
cd text-summarizer
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install openai python-dotenv
```

4. **Set up your API key**

Create a `.env` file in the root of the project and add:

```env
OPENAI_API_KEY=your-api-key-here
```

> 💡 **Tip:** Make sure `.env` is in your `.gitignore` file so it won’t be pushed to GitHub.

---

## ▶️ Usage

1. Prepare a text file you want to summarize, for example: `example_text.txt`

2. Run the script from the command line:

```bash
python summarizer.py example_text.txt
```

3. You’ll see the summarized output printed in your terminal.

---

## 📁 File Structure

```
text-summarizer/
├── summarizer.py         # The main script
├── example_text.txt      # (Optional) A sample text file to summarize
├── .env                  # Your API key (not pushed to GitHub)
└── README.md             # Project instructions
```

---

## 🧠 How It Works

1. Reads a text file from disk
2. Sends it to OpenAI's GPT model with a summarization prompt
3. Receives and prints a short summary

---

## 📄 Example

**Input text (`example_text.txt`):**

```
Artificial intelligence (AI) refers to the simulation of human intelligence in machines...
It allows machines to learn from experience, adjust to new inputs, and perform human-like tasks.
```

**Run command:**
```bash
python summarizer.py example_text.txt
```

**Output:**
```
AI enables machines to simulate human intelligence, learn from experience, and perform tasks similar to humans.
```

---

## 💻 Full Script (`summarizer.py`)

Here’s the complete Python script:

```python
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
```

---

## ❓ FAQ

**Q: Can I use GPT-4 instead of GPT-3.5?**  
Yes! Just change the model name in `summarize_text()` to `"gpt-4"` (you need access to GPT-4 in your OpenAI account).

**Q: What if my text is very long?**  
The script supports input up to the model’s token limit. For very large files, consider chunking the input.

---

## 🧩 Future Improvements

- Web app version (Streamlit or Flask)
- PDF/DOCX input support
- Multiple summarization styles (bullet points, executive summary, etc.)
- File output option for saving summaries

---

## 📄 License

MIT License. You’re free to use and modify this project.

---

## 🙋 Contributing

Contributions are welcome! Open an issue or pull request to suggest improvements or new features.
