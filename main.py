import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Load environment variables from .env file
load_dotenv()

# Access the constants
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

source_channel = 'upwrk_jobs'  # Replace with source channel username
destination_channel = 'your channel username' # Replace with destination channel username

# Create a new client instance
client = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    # Message received from source channel
    # Forward it to destination channel
    message_text = event.message
    # print(message_text)
    await client.send_message(destination_channel, message_text)

print("Bot is now running...")
with client:
    client.run_until_disconnected()