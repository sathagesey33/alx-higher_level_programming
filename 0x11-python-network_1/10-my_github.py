#!/usr/bin/python3
"""
Module: github_id
Uses the GitHub API to display the user ID using Basic
Authentication with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info['id']
        print(f"User ID: {user_id}")
    else:
        print("Failed to fetch user ID. Check your credentials.")
