<div align="center">

# ↗️ LinkedIn Post Generator Agent 🤖

`Module 21` · `Ostad AI/ML Engineering Program` · `Batch 6`
**Author:** Farjana Ferdausi

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/farjanaferdausi-cs50ai/LinkedIn_Post_Generator_Agent/blob/main/LinkedIn_Post_Generator_Agent.ipynb)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-886FBF?style=for-the-badge&logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge)

</div>

---

## 📘 About This Notebook

- Provide a `topic` and a `language`, the agent returns a publish-ready LinkedIn post (2–4 paragraphs, hook, hashtags, call to action).
- This is an `agent`, not just a prompt.
- Instead of one LLM call, the agent runs a `two-stage reflection pipeline`:

1. **Draft** — the LLM writes a first version.
2. **Critique & refine** — the LLM reviews its **own** draft against a LinkedIn best-practices checklist and returns an improved final version.

```
topic, language ──▶ [ Draft Chain ] ──▶ [ Critique & Refine Chain ] ──▶ final post
                       (LLM call 1)            (LLM call 2)
```

> [!TIP]
> Self-correction loop is what turns a plain chain into agentic behavior.

## 🌐 1. Install Dependencies

Install the required packages: `langchain`, `langchain-core`, and `langchain-google-genai`.

## 🔑 2. Set My Gemini API Key

I created a **free** `API-key` from Google AI Studio and used it to connect the Gemini model with my project.

## 💠 3. Build the Agent

For this project, I created the main agent logic in a separate Python file called `agent.py`. This is standard practice in production ML engineering — notebooks are for demos and exploration, `.py` files hold the reusable logic.

I did this to keep the notebook simple and organized. The notebook is mainly used for testing and demonstrating the agent, while `agent.py` contains the reusable code for generating LinkedIn posts.

## 🌀 4. Try It Yourself

Now I can test the agent by changing the topic and language in the notebook. No code changes are needed — I just enter my choices in the Colab form and run the cell to generate a LinkedIn post.

## 🔍 5. See the Agent's Reasoning: Draft → Refined

This cell shows how the agent works in two steps. First, it creates a draft of the LinkedIn post, and then it improves and refines the draft. I show both steps in the demo video to explain how the agent generates the final post.

## 🌍 6. Multi-Language Demo

The agent can generate LinkedIn posts in different languages. In this project, I tested it with `English`, `Bengali`, and `Spanish`. The same agent is used for all three languages, and each post is generated only once.

## 💾 7. Save the Generated Posts

This step saves all the generated LinkedIn posts into a file called `generated_posts.md`. I use this file to keep the generated posts and also use them later for my own LinkedIn posts.

## 🎯 8. Conclusion

In this project, I built an AI agent using LangChain and Google Gemini that generates professional LinkedIn posts from just a topic and a target language. Rather than a single prompt-response call, I designed the agent around a two-stage reflection pattern — draft, then self-critique and refine — which gives it genuine multi-step reasoning instead of a one-shot generation.

**Possible extensions I would explore next:**
- A tool the agent can call to pull real trending hashtags before writing.
- A tone selector (formal / casual / thought-leader).
- Wrapping this in a small Streamlit app for non-technical users.

**Tech stack:** Python, LangChain (LCEL), Google Gemini API, Google Colab.

---

<sub>The sections below are standard repo housekeeping, kept separate from the notebook write-up above.</sub>

## 🛠️ Setup (Running Outside Colab)

1. Get a free Gemini API key (no credit card required) from [Google AI Studio](https://aistudio.google.com/apikey).
2. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/farjanaferdausi-cs50ai/LinkedIn_Post_Generator_Agent.git
   cd LinkedIn_Post_Generator_Agent
   pip install -r requirements.txt
   ```
3. Set your API key:
   ```bash
   cp .env.example .env
   # then open .env and paste your key
   ```

> [!TIP]
> Running this in Google Colab instead? Skip the `.env` file — add `GOOGLE_API_KEY` under the 🔑 **Secrets** panel in the left sidebar and it's picked up automatically.

## 📂 Project Structure

```
LinkedIn_Post_Generator_Agent/
├── agent.py                              # Core agent logic (reusable module)
├── LinkedIn_Post_Generator_Agent.ipynb   # Notebook: setup, demo, multi-language tests
├── requirements.txt                      # Python dependencies
├── .env.example                          # Template for your API key
├── .gitignore
└── README.md
```

> [!NOTE]
> Only `.env.example` is tracked in version control. The real `.env` file (with your actual key) stays local on your machine and is excluded by `.gitignore`.

---

<div align="center">

### ⭐ If this project helped you, consider starring the repo!

![GitHub stars](https://img.shields.io/github/stars/farjanaferdausi-cs50ai/LinkedIn_Post_Generator_Agent?style=for-the-badge&color=FFD700&logo=github&logoColor=white)
![GitHub followers](https://img.shields.io/github/followers/farjanaferdausi-cs50ai?style=for-the-badge&color=blueviolet&logo=github&logoColor=white)
![Made with love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-006A4E?style=for-the-badge)

**Farjana Ferdausi**

[![GitHub](https://img.shields.io/badge/GitHub-farjanaferdausi--cs50ai-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/farjanaferdausi-cs50ai)

Google Colab Link : https://colab.research.google.com/drive/1hRgCrohAH4q5gnTlE9Sib-Mqq_gRKi1a?usp=sharing

LinkedIn Link : https://www.linkedin.com/in/farjana-ferdausi

Medium Link : https://medium.com/@farjana.rafi1983

</div>
