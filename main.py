from reddit_scraper import RedditScraper
from persona_generator import PersonaGenerator
import os
import re

def extract_username(url):
    match = re.search(r"reddit\.com/user/([^/]+)/?", url)
    return match.group(1) if match else None

if __name__ == "__main__":
    urls = input("Enter Reddit profile URLs (comma-separated), or press Enter for default users:\n").strip()

    if not urls:
        urls = [
            "https://www.reddit.com/user/kojied/",
            "https://www.reddit.com/user/Hungry-Move-6603/"
        ]
        print("Using default test users...")
    else:
        urls = [url.strip() for url in urls.split(",")]

    scraper = RedditScraper()
    generator = PersonaGenerator()

    os.makedirs("personas", exist_ok=True)

    for url in urls:
        username = extract_username(url)
        if not username:
            print(f"Invalid URL skipped: {url}")
            continue

        print(f"Scraping u/{username}...")
        data = scraper.get_user_data(username)

        print("Generating persona...")
        persona = generator.generate_persona(data)

        output_path = f"personas/{username}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(persona)

        print(f"✔ Persona saved to {output_path}\n")
