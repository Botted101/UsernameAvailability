Roblox Username Checker
A Python script to check if a Roblox username is available, monitor it periodically, and notify via Discord webhook with an @everyone
ping and a sound alert when available.
 Setup and Usage
  Install Dependencies:
   pip install requests discord-webhook playsound

  Configuration of Script (IMPORTANT):
   Open roblox_username_checker.py and configure the following:

  USERNAME: Set to the Roblox username you want to check.
   USERNAME = "your-desired-username"

  WEBHOOK_URL: Replace with your Discord webhook URL (create one in your Discord server settings).
   WEBHOOK_URL = "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"

  time.sleep(2): Controls how often the script checks the username (in seconds). Default is 2 seconds. Setting it too low may cause rate-limiting by the Roblox API.
   time.sleep(Number-Here)

Run the Program:
 Once everything is configured, run the script:
 python roblox_username_checker.py

Notes
 The script will check the username every 2 seconds (or as set by time.sleep) if unavailable.

 When the username becomes available, it sends a Discord notification with an @everyone
 ping and plays a sound (notification.mp3).


