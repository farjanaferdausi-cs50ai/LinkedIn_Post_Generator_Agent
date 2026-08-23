<div align="center">

# 🔗 LinkedIn Post Generator Agent

**An AI agent built with LangChain and Google Gemini that turns a topic and a target language into a publish-ready, professional LinkedIn post.**

`Module 21` · `Ostad AI/ML Engineering Program` · `Batch 6`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/farjanaferdausi-cs50ai/linkedin-post-agent/blob/main/Module21_LinkedIn_Post_Agent.ipynb)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-886FBF?style=for-the-badge&logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge)

</div>

<br>

## 🧠 Why This Is an *Agent* — Not Just a Prompt

Most "AI post generators" are a single prompt wired to an LLM. This one goes a step further: it runs a **two-stage reflection pipeline**, a recognized agentic design pattern where the model reasons about and corrects its own output before returning it.

<div align="center">

| Stage | Role | What Happens |
|:---:|:---|:---|
| ✍️ **01 · Draft** | Content Strategist | Writes a first version of the post from the topic and language. |
| 🔎 **02 · Critique & Refine** | Strict Editor | Re-reads its *own* draft against a LinkedIn best-practices checklist — hook strength, formatting, tone, hashtags — and returns an improved final version. |

</div>

```
topic, language ──▶ [ Draft Chain ] ──▶ [ Critique & Refine Chain ] ──▶ final post
                       (LLM call 1)             (LLM call 2)
```

> That self-correction loop — **generate → critique → refine** — is what separates an agent from a plain "prompt → output" chain.

## Tech stack

| Layer | Choice |
|---|---|
| Orchestration | LangChain (LCEL: `prompt \| llm \| output_parser`) |
| LLM | Google Gemini (`gemini-3.6-flash`) via `langchain-google-genai` |
| Environment | Google Colab / Python 3.10+ |

## Project structure

```
linkedin-post-agent/
├── agent.py                              # Core agent logic (reusable module)
├── Module21_LinkedIn_Post_Agent.ipynb    # Notebook: setup, demo, multi-language tests
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

1. Get a **free** Gemini API key (no credit card required) from
   [Google AI Studio](https://aistudio.google.com/apikey).
2. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/farjanaferdausi-cs50ai/linkedin-post-agent.git
   cd linkedin-post-agent
   pip install -r requirements.txt
   ```
3. Set your API key:
   ```bash
   cp .env.example .env
   # then open .env and paste your key
   ```
   In **Google Colab**, instead add `GOOGLE_API_KEY` under the 🔑 Secrets
   panel in the left sidebar.

## Usage

```python
from agent import LinkedInPostAgent

agent = LinkedInPostAgent()
post = agent.generate(topic="AI in Healthcare", language="English")
print(post.final)
```

Or simply open `Module21_LinkedIn_Post_Agent.ipynb` in Google Colab and run
all cells top to bottom — it installs dependencies, asks for your API key,
writes and loads the agent, and walks through single-post, multi-language,
and draft-vs-refined demos.

## Example

**Input:** topic = `"Remote Work Productivity"`, language = `"Bengali"`
**Output:** a 2–4 paragraph LinkedIn post in Bengali, with a hook opening
line, short scannable paragraphs, a closing question, and 3–5 hashtags.

Run the notebook's demo cells to generate live examples — they're saved to
`generated_posts.md`.

## Possible extensions

- Give the agent a tool to fetch real trending hashtags before writing.
- Add a tone selector (formal / casual / thought-leader).
- Wrap it in a small Streamlit app for non-technical users.

## Author

**Farjana Ferdausi** — [GitHub](https://github.com/farjanaferdausi-cs50ai)
