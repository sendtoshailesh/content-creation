# Social Media API Setup Guide

Step-by-step instructions for configuring credentials for each social platform. All credentials are stored in `.env` (never committed to git).

## Reddit (Free)

**MCP Server**: `reddit-mcp-server` (npm, MIT license, 85 stars)
**Cost**: Free — Reddit API has no usage fees
**Rate limit**: 60 requests/minute (authenticated), ~10/min (anonymous)

### Steps

1. Go to [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **"create another app..."** at the bottom
3. Fill in:
   - **Name**: `content-pipeline` (or any name)
   - **App type**: Select **"script"**
   - **Description**: Optional
   - **About URL**: Leave blank
   - **Redirect URI**: `http://localhost:8080` (required but not used for script apps)
4. Click **"create app"**
5. Copy the **client ID** (string under the app name) and **client secret**
6. Add to `.env`:

```bash
REDDIT_CLIENT_ID=your-14-char-client-id
REDDIT_CLIENT_SECRET=your-27-char-client-secret
REDDIT_USERNAME=your-reddit-username
REDDIT_PASSWORD=your-reddit-password
```

### Testing

```bash
# Anonymous mode (no credentials needed — read-only)
npx reddit-mcp-server

# Authenticated mode (read + write)
REDDIT_CLIENT_ID=... REDDIT_CLIENT_SECRET=... npx reddit-mcp-server
```

### Safe Mode

Reddit MCP server has built-in spam protection (on by default):
- **standard** (default): 2s delay between writes, last 10 items duplicate check
- **strict**: 5s delay, last 20 items check
- **off**: No protection (not recommended)

---

## LinkedIn (Free Tier via Unipile)

**MCP Server**: `mcp-linkedin` (npm, MIT license)
**Cost**: Free tier available — Unipile provides a LinkedIn API wrapper
**Auth**: Unipile handles LinkedIn OAuth internally

### Steps

1. Sign up at [unipile.com](https://www.unipile.com/)
2. In the Unipile dashboard, click **"Connect Account"** and link your LinkedIn account
3. Go to **Settings** in the dashboard
4. Copy your **API Key** and **DSN** (format: `apiXX.unipile.com:XXXXX`)
5. Add to `.env`:

```bash
UNIPILE_API_KEY=your-unipile-api-key
UNIPILE_DSN=apiXX.unipile.com:XXXXX
```

### Features

- **Dry-run by default** — preview posts before publishing
- Media attachments (images, video)
- Company @mentions (auto-resolved)
- Auto-likes posts after publishing
- 3 tools: `linkedin_publish`, `linkedin_comment`, `linkedin_react`

### Testing

The `linkedin_publish` tool defaults to `dry_run: true`, so calling it always previews first. Call with `dry_run: false` only after reviewing the preview.

---

## X/Twitter (Free Tier)

**MCP Server**: Custom Python server (`scripts/mcp-social-publisher/server.py`)
**Cost**: Free tier — 1,500 tweets/month, 1 app environment
**Rate limit**: 50 tweets/24h (free), 300 requests/15min (basic)

### Steps

1. Go to [developer.x.com/en/portal/dashboard](https://developer.x.com/en/portal/dashboard)
2. Sign up for a **Free** developer account (or Basic at $100/mo for higher limits)
3. Create a new **Project** and **App**
4. In the app settings, go to **"Keys and tokens"**
5. Generate:
   - **API Key** and **API Key Secret** (Consumer keys)
   - **Access Token** and **Access Token Secret** (under Authentication Tokens)
6. Ensure the app has **Read and Write** permissions (Settings → User authentication settings)
7. Add to `.env`:

```bash
TWITTER_API_KEY=your-api-key
TWITTER_API_SECRET=your-api-key-secret
TWITTER_ACCESS_TOKEN=your-access-token
TWITTER_ACCESS_SECRET=your-access-token-secret
```

### Thread Support

The custom MCP server parses numbered tweet patterns (e.g., `1/ First tweet`) from `content/x-twitter-thread.md` and posts them as a linked thread (each tweet replies to the previous).

### Testing

```bash
# Preview (default — dry_run=True)
# Call post_to_twitter via MCP — returns preview without posting

# Delete test tweets via X/Twitter web UI after testing
```

---

## YouTube Data API v3 (Free)

**MCP Server**: Custom Python server (`scripts/mcp-social-publisher/server.py`)
**Cost**: Free — 10,000 quota units/day (metadata update ~50 units)
**Scope**: Metadata updates only (title, description, tags). Does NOT upload videos.

### Steps

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project (or select existing)
3. Enable **YouTube Data API v3**:
   - Go to APIs & Services → Library
   - Search "YouTube Data API v3" → Enable
4. Create OAuth 2.0 credentials:
   - Go to APIs & Services → Credentials
   - Click **"Create Credentials"** → **"OAuth client ID"**
   - Application type: **Desktop app**
   - Copy the **Client ID** and **Client Secret**
5. Configure the OAuth consent screen:
   - Go to APIs & Services → OAuth consent screen
   - Set to **External** (or Internal for Workspace)
   - Add your email as a test user
6. Add to `.env`:

```bash
YOUTUBE_CLIENT_ID=your-client-id.apps.googleusercontent.com
YOUTUBE_CLIENT_SECRET=your-client-secret
```

### One-Time Auth Flow

YouTube requires a one-time browser-based OAuth flow to generate a refresh token:

```bash
python scripts/mcp-social-publisher/youtube_auth.py
```

This opens a browser, asks you to log in, and saves the token to `.youtube-token.json` (gitignored). The token auto-refreshes after that.

### Testing

```bash
# Preview metadata changes (dry_run=True by default)
# Call update_youtube_metadata via MCP with a video_id
```

---

## Alternative: Multi-Platform SaaS (Paid)

If you prefer a single API key covering all platforms (except Reddit), consider:

### PostEverywhere ($19-79/mo)

- **Platforms**: Instagram, TikTok, YouTube, LinkedIn, Facebook, X, Threads, Pinterest
- **MCP**: `@posteverywhere/mcp` (npm)
- **Setup**: Sign up at [posteverywhere.ai/signup](https://app.posteverywhere.ai/signup) (7-day free trial)
- **Config**: Single `POSTEVERYWHERE_API_KEY` in `.env`
- **Note**: Does NOT support Reddit — still need `reddit-mcp-server`

### PostFast (Paid, free tier available)

- **Platforms**: 11 platforms including BlueSky, Telegram, Google Business
- **MCP**: `postfast-mcp` (npm)
- **Setup**: Sign up at [postfa.st](https://app.postfa.st/dashboard)
- **Config**: Single `POSTFAST_API_KEY` in `.env`
- **Note**: Does NOT support Reddit

To switch to a SaaS approach, replace the `linkedin` and `social-publisher` entries in `.vscode/mcp.json` with the single SaaS MCP server.
