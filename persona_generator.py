"""
Persona Generator Module

This module uses Google's Generative AI (Gemini) to analyze Reddit user data
and generate comprehensive user personas based on their posts and comments.

Requirements:
- Google Generative AI API key
- Environment variables stored in .env file
- google-generativeai library installed

Author: Mohammed Faris Sait
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv


class PersonaGenerator:
    def __init__(self):
        """
        Initialize the persona generator with Google Generative AI.

        Loads environment variables from .env file and configures the
        Google Generative AI client with API key.

        Environment Variables Required:
            GEMINI_API_KEY: Google Generative AI API key
        """
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

    def generate_persona(self, data):
        """
        Generate a structured user persona from Reddit user data.

        Args:
            data (dict): Dictionary containing user data with keys:
                - username (str): Reddit username
                - posts (list): List of user's posts
                - comments (list): List of user's comments

        Returns:
            str: Formatted persona text with structured sections including:
                - User Info (demographics, traits)
                - Motivations (learning, expression, socializing, problem-solving)
                - Behavior & Habits
                - Frustrations
                - Personality (MBTI-style assessment)
                - Goals & Needs
                - Source Highlights (cited quotes)

        Example:
            >>> generator = PersonaGenerator()
            >>> data = {"username": "kojied", "posts": [...], "comments": [...]}
            >>> persona = generator.generate_persona(data)
            >>> print(persona)
            👤 USER INFO
            - Reddit Username: u/kojied
            ...
        """
        username = data["username"]
        text_blob = "\n\n".join(data["posts"] + data["comments"])

        prompt = f"""
You are an expert UX researcher and LLM assistant. Based on the Reddit user's public posts and comments, create a structured user persona. Follow this exact format.

---

👤 USER INFO
- Reddit Username: u/{username}
- Age: (Guess or say Unknown)
- Occupation: (Guess or say Not specified)
- Status: (Single, Married, Unknown, etc.)
- Location: (Inferred from language, culture, currency, etc.)
- Tier: (Power User, Lurker, Curious Learner, etc.)
- Archetype: (The Explorer, The Builder, etc.)
- Traits: (Adjectives like Analytical, Tech-savvy, Introverted, etc.)

💡 MOTIVATIONS
Rate the following motivations on a scale from 1 to 5 based on their presence in the user's posts/comments:

- Learning
- Expression
- Socializing
- Problem-solving

Use this format:
- Learning: 5/5
- Expression: 4/5
...

📈 BEHAVIOUR & HABITS
- Bullet points that summarize user posting style, tone, frequency, preferred subreddits, etc.

😤 FRUSTRATIONS
- Bullet points that highlight complaints, dislikes, or pain points

🧠 PERSONALITY
|       Axis       |   Tendency    |
|------------------|---------------|
| Introvert  — 🟢  |  Extrovert    |
| Intuition  — 🟢  |  Sensing      |
| Feeling    — 🟢  |  Thinking     |
| Perceiving — 🟢  |  Judging      |

🎯 GOALS & NEEDS
- Bullet points describing what the user seems to want or achieve via Reddit

🔍 SOURCE HIGHLIGHTS
- Provide 2–3 direct quotes from posts/comments
- Mention whether it came from a Post or Comment
- Format: *"Quote here..."* → Post

---

DATA (Reddit Posts + Comments):

{text_blob}

---

📢 IMPORTANT: Format your output in plain text **exactly** as above. No markdown, no JSON, no commentary.
        """

        response = self.model.generate_content(prompt)
        return response.text


