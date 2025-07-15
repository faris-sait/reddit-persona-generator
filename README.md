# Reddit User Persona Generator

A Python application that scrapes Reddit user profiles and generates comprehensive user personas using AI analysis. This project analyzes users' posts and comments to create detailed psychological and behavioral profiles.

## 🎯 Project Overview

This tool takes Reddit profile URLs as input, scrapes the user's public posts and comments, and generates structured user personas that include demographics, motivations, behavioral patterns, personality traits, and cited sources.

## 💡 Bonus Concept
Inspired by this project, I also conceptualized a business tool that scrapes customer reviews from e-commerce apps and provides clear sentiment insights using Gemini LLM.

## 📋 Features

- **Reddit Data Scraping**: Extracts posts and comments from Reddit user profiles
- **AI-Powered Analysis**: Uses Google's Generative AI (Gemini) for persona generation
- **Structured Output**: Generates personas in a consistent, readable format
- **Source Citations**: Provides quotes from posts/comments supporting each persona characteristic
- **Multiple User Support**: Process multiple Reddit profiles in a single run

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **PRAW**: Python Reddit API Wrapper for Reddit data scraping
- **Google Generative AI**: Gemini AI model for persona generation
- **python-dotenv**: Environment variable management

## 📦 Installation

1. **Clone the repository** (or download the files)
   ```bash
   git clone <your-repo-url>
   cd reddit-persona-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root with the following variables:
   ```env
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   GEMINI_API_KEY=your_gemini_api_key
   ```

## 🔑 API Setup

### Reddit API
1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Choose "script" as the app type
4. Note down the Client ID and Client Secret

### Google Generative AI API
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key for use in your `.env` file

## 🚀 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Input Reddit profile URLs**
   - Enter comma-separated URLs when prompted
   - Or press Enter to use default test users (kojied, Hungry-Move-6603)
   - Example format: `https://www.reddit.com/user/username/`

3. **View results**
   - Personas are saved in the `personas/` directory
   - Each user gets a separate `.txt` file named `{username}.txt`

## 📁 Project Structure

```
reddit-persona-generator/
├── main.py                 # Main entry point
├── reddit_scraper.py       # Reddit data scraping logic
├── persona_generator.py    # AI persona generation logic
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── personas/              # Output directory (auto-created)
│   ├── kojied.txt
│   └── Hungry-Move-6603.txt
└── README.md              # This file
```

## 📊 Generated Persona Format

Each persona includes:

- **👤 User Info**: Demographics, occupation, location, user tier
- **💡 Motivations**: Learning, expression, socializing, problem-solving (rated 1-5)
- **📈 Behavior & Habits**: Posting patterns, preferred subreddits, tone
- **😤 Frustrations**: Pain points and complaints
- **🧠 Personality**: MBTI-style personality assessment
- **🎯 Goals & Needs**: What the user seeks to achieve
- **🔍 Source Highlights**: Direct quotes with citations

## 🎯 Example Usage

```python
# For programmatic usage
from reddit_scraper import RedditScraper
from persona_generator import PersonaGenerator

scraper = RedditScraper()
generator = PersonaGenerator()

# Get user data
data = scraper.get_user_data("kojied")

# Generate persona
persona = generator.generate_persona(data)

# Save to file
with open("kojied_persona.txt", "w") as f:
    f.write(persona)
```
## EXAMPLE OUTPUT FILES
Sample personas are stored in the personas/ folder. Example files include:
kojied.txt,
Hungry-Move-6603.txt,
spez.txt

## ⚠️ Important Notes

- **Rate Limits**: Reddit API has rate limits. Avoid excessive requests
- **Privacy**: Only analyzes publicly available Reddit data
- **API Keys**: Keep your API keys secure and never commit them to version control
- **Data Usage**: Respect Reddit's terms of service and user privacy

## 🔒 Privacy & Ethics

This tool only accesses publicly available Reddit data. It does not:
- Access private messages or restricted content
- Store personal data beyond the generated personas
- Violate Reddit's terms of service

## 🐛 Troubleshooting

**Common Issues:**

1. **API Key Errors**: Ensure your `.env` file is properly configured
2. **User Not Found**: Check that the Reddit username exists and is public
3. **Rate Limiting**: If you encounter rate limits, wait before making more requests
4. **Import Errors**: Ensure all dependencies are installed: `pip install -r requirements.txt`

## 📝 Assignment Requirements Compliance

This project fulfills all requirements from the BeyondChats internship assignment:

- ✅ Takes Reddit profile URLs as input
- ✅ Scrapes comments and posts from Reddit users
- ✅ Builds comprehensive user personas
- ✅ Outputs personas to text files
- ✅ Cites sources for each persona characteristic
- ✅ Uses LLMs (Google Generative AI) for analysis
- ✅ Follows PEP-8 guidelines
- ✅ Includes executable Python script
- ✅ Provides clear setup and execution instructions
- ✅ Processes both sample users (kojied, Hungry-Move-6603)

## 👤 Author
Mohammed Faris Sait
Created for BeyondChats AI/LLM Engineer Intern Assignment

