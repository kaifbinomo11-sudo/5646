#!/usr/bin/env python3
"""
Replit entry point.
- If TELEGRAM_BOT_TOKEN is set, delegates entirely to bot.main() which
  starts the Flask dashboard on port 5000 and runs the Telegram bot.
- If no token is set, starts only the dashboard in a keep-alive loop.
"""
import os
import time

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

if BOT_TOKEN:
    import bot as _bot
    _bot.main()
else:
    from dashboard import start_dashboard
    start_dashboard(port=5000)
    print("✅ Status dashboard running on port 5000")
    print("⚠️  TELEGRAM_BOT_TOKEN is not set — dashboard-only mode.")
    print("    Set the secret and restart to enable the Telegram bot.")
    while True:
        time.sleep(60)
