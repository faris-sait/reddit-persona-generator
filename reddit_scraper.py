"""
Reddit Scraper Module

This module provides functionality to scrape Reddit user data including posts
and comments using the PRAW (Python Reddit API Wrapper) library.

Requirements:
- Reddit API credentials (client_id, client_secret)
- Environment variables stored in .env file
- PRAW library installed

Author: Mohammed Faris Sait
"""

import os
import praw
from dotenv import load_dotenv


class RedditScraper:

    def __init__(self):
        """
        Initialize the Reddit scraper with API credentials.

        Loads environment variables from .env file and creates an authenticated
        Reddit instance using PRAW.

        Environment Variables Required:
            REDDIT_CLIENT_ID: Reddit API client ID
            REDDIT_CLIENT_SECRET: Reddit API client secret
        """
        load_dotenv()
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="persona-analyzer by u/Amazing-Sample5287"
        )

    def get_user_data(self, username):

        user = self.reddit.redditor(username)

        # Scrape user's posts (submissions)
        posts = [
            f"Post Title: {post.title}\nPost Body: {post.selftext}\nURL: https://www.reddit.com{post.permalink}"
            for post in user.submissions.new(limit=20)
        ]

        # Scrape user's comments
        comments = [
            f"Comment: {comment.body}\nURL: https://www.reddit.com{comment.permalink}"
            for comment in user.comments.new(limit=50)
        ]

        return {
            "username": username,
            "posts": posts,
            "comments": comments
        }

