#!/usr/bin/env python3
"""
One-time OAuth flow for YouTube Data API v3.

Run this once to authorize the app and generate a refresh token.
The token is saved to .youtube-token.json in the workspace root.

Usage:
  python scripts/mcp-social-publisher/youtube_auth.py
"""

import json
import os
import sys
from pathlib import Path

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    print("Missing dependency. Run: pip install google-auth-oauthlib")
    sys.exit(1)

from dotenv import load_dotenv

WORKSPACE = Path(__file__).resolve().parent.parent.parent
load_dotenv(WORKSPACE / ".env")

SCOPES = ["https://www.googleapis.com/auth/youtube"]
TOKEN_PATH = WORKSPACE / ".youtube-token.json"


def main():
    client_id = os.environ.get("YOUTUBE_CLIENT_ID", "")
    client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        print("Set YOUTUBE_CLIENT_ID and YOUTUBE_CLIENT_SECRET in .env first.")
        print("See docs/social-api-setup.md for instructions.")
        sys.exit(1)

    # Build client config from env vars (no client_secrets.json file needed)
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    }

    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=8080, open_browser=True)

    token_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": creds.scopes,
    }

    TOKEN_PATH.write_text(json.dumps(token_data, indent=2))
    print(f"\nToken saved to {TOKEN_PATH}")
    print("You can now use the update_youtube_metadata MCP tool.")


if __name__ == "__main__":
    main()
