import requests
from discord_webhook import DiscordWebhook
import time
from playsound import playsound
import os

USERNAME = "ChangeUsername"
WEBHOOK_URL = "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"
SOUND_FILE = "notification.mp3"

def check_username_availability(username):
    params = {
        "birthday": "2006-09-21T07:00:00.000Z",
        "context": "Signup",
        "username": username
    }
    try:
        response = requests.get("https://auth.roblox.com/v1/usernames/validate", params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("code") == 0
    except requests.RequestException as e:
        print(f"Error checking username: {e}")
        return None

def send_discord_notification(username):
    webhook = DiscordWebhook(
        url=WEBHOOK_URL,
        content=f"@everyone Username `{username}` is now available on Roblox!"
    )
    try:
        response = webhook.execute()
        print("Discord notification sent with @everyone ping!")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

def play_notification_sound():
    try:
        if os.path.exists(SOUND_FILE):
            playsound(SOUND_FILE)
            print("Notification sound played!")
        else:
            print(f"Sound file {SOUND_FILE} not found.")
    except Exception as e:
        print(f"Error playing sound: {e}")

def main():
    print(f"Checking availability for username: {USERNAME}")
    
    while True:
        availability = check_username_availability(USERNAME)
        
        if availability is None:
            print("Failed to check username, retrying in 2 seconds...")
        elif availability:
            print(f"Username {USERNAME} is available!")
            send_discord_notification(USERNAME)
            play_notification_sound()
            break
        else:
            print(f"Username {USERNAME} is not available, checking again in 2 seconds...")
        
        time.sleep(2)

if __name__ == "__main__":
    main()