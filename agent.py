"""
agent.py

An AI agent, built with LangChain & Google Gemini, that turns a
(topic, language) pair into a publish-ready LinkedIn post.

--------------------------------------------------------------------
WHY THIS COUNTS AS AN "AGENT" AND NOT JUST A SINGLE PROMPT
--------------------------------------------------------------------
A single prompt -> LLM -> output call is just a "chain." This project
instead uses a two-stage REFLECTION pattern, which is a recognized
agentic design used in real production systems:

    Stage 1 (DRAFT)    : the LLM writes a first version of the post.
    Stage 2 (CRITIQUE) : the LLM re-reads its OWN draft against a
                          checklist of LinkedIn best practices and
                          returns an improved final version.

The agent is, in effect, reasoning about and correcting its own work
before handing it back to the user - that self-correction loop is
what separates an "agent" from a plain prompt-response call.

Author: Farjana Ferdausi
Module: Ostad AI/ML Engineering Program - Module 21
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI


# A default model. gemini-3.6-flash is on Google's free tier
# and is the current stable/GA workhorse Flash model.
# Note on model lifecycles: Google regularly retires older model IDs
# (e.g. gemini-2.5-flash was retired for new users shortly after this
# project started). If generate() ever raises a 404 / "model not found"
# error, check the current model list at https://ai.google.dev/gemini-api/docs/models
# and update this ONE line - no other code needs to change, which is the
# whole point of keeping the model name in a single constant.
# Model 'gemini-3.6-flash' uses fixed sampling defaults; temperature will be ignored
DEFAULT_MODEL = "gemini-3.6-flash"


@dataclass
class LinkedInPost:
    """
    A small container that holds everything about one generated post.

    Keeping the draft AND the final version (instead of just the final
    text) makes it easy to show, in the demo video, exactly what the
    'critique' stage changed - this is good evidence that the agent is
    really doing multi-step reasoning, not just calling the API once.
    """
    topic: str
    language: str
    draft: str
    final: str


class LinkedInPostAgent:
    """
    Usage
    -----
    >>> agent = LinkedInPostAgent()
    >>> post = agent.generate(topic="AI in Healthcare", language="English")
    >>> print(post.final)
    """

    def __init__(self, model_name: str = DEFAULT_MODEL, temperature: float = 0.7):
        if not os.environ.get("GOOGLE_API_KEY"):
            raise ValueError(
                "GOOGLE_API_KEY is not set. Get a free key from "
                "https://aistudio.google.com/apikey and set it as an "
                "environment variable (see README.md) before creating the agent."
            )

        # ChatGoogleGenerativeAI reads the GOOGLE_API_KEY environment variable
        # automatically - this is intentional. Passing the key as an explicit
        # keyword argument is possible too, but the parameter name has changed
        # between langchain-google-genai versions; the env var is the one
        # interface Google and LangChain both guarantee stays stable.
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
        )

        # Build both stages of the pipeline once, at start-up, so that
        # generate() just re-uses them instead of rebuilding on every call.
        self.draft_chain: Runnable = self._build_draft_chain()
        self.critique_chain: Runnable = self._build_critique_chain()

    # ------------------------------------------------------------------
    # Stage 1: DRAFT
    # ------------------------------------------------------------------
    def _build_draft_chain(self) -> Runnable:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a senior LinkedIn content strategist who writes "
                    "concise, professional, engaging posts. "
                    "You ALWAYS write the post entirely in the language the "
                    "user asks for - never default to English unless English "
                    "is the language requested.",
                ),
                (
                    "human",
                    "Write a LinkedIn post about: {topic}\n"
                    "Language: {language}\n\n"
                    "Requirements:\n"
                    "- 2 to 4 short paragraphs\n"
                    "- Open with a strong hook (first line must earn a click on "
                    '"see more")\n'
                    "- Use short paragraphs and line breaks, the way real "
                    "LinkedIn posts are formatted\n"
                    "- Close with a call to action or a question that invites "
                    "comments\n"
                    "- End with 3 to 5 relevant hashtags\n"
                    "- Plain text only - no markdown symbols like ** or ##",
                ),
            ]
        )
        return prompt | self.llm | StrOutputParser()

    # ------------------------------------------------------------------
    # Stage 2: CRITIQUE & REFINE
    # ------------------------------------------------------------------
    def _build_critique_chain(self) -> Runnable:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a strict LinkedIn editor. You improve drafts "
                    "without changing their language or their core message. "
                    "Reply with ONLY the improved post - no notes, no "
                    "preamble, no explanations.",
                ),
                (
                    "human",
                    "Topic: {topic}\n"
                    "Language: {language}\n"
                    "Draft post:\n{draft}\n\n"
                    "Review the draft against this checklist, then return the "
                    "improved final version:\n"
                    "1. Is the opening line strong enough to stop someone "
                    "mid-scroll?\n"
                    "2. Is it broken into short, easy-to-scan paragraphs?\n"
                    "3. Does it sound like a real professional, not a robot?\n"
                    "4. Are the hashtags relevant and limited to 3-5?",
                ),
            ]
        )
        return prompt | self.llm | StrOutputParser()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def generate(self, topic: str, language: str = "English") -> LinkedInPost:
        """Run the full draft -> critique -> refine pipeline once."""
        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")
        if not language or not language.strip():
            raise ValueError("Language cannot be empty.")

        draft = self.draft_chain.invoke({"topic": topic, "language": language})
        final = self.critique_chain.invoke(
            {"topic": topic, "language": language, "draft": draft}
        )

        return LinkedInPost(topic=topic, language=language, draft=draft, final=final)
