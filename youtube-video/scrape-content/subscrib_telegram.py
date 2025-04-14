from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import os

# Replace these with your values
api_id = '25185018'          # from my.telegram.org
api_hash = 'b9f0ea2a9390ab289b82629c93ce8b09'
phone_number = '+19404658685'  # your phone number with country code
channel_username = 'lilaoshibushinilaoshi'  # shortname from https://t.me/...

print('Starting Telegram client...')
client = TelegramClient('jc_session', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    print("Client not authorized. Sending code request...")
    client.send_code_request(phone_number)
    code = input('Enter the code you received: ')
    client.sign_in(phone_number, code)
else:
    print("Client already authorized.")



print( "Client created.")
# Start the client
# client.start(phone=phone_number)
# print("Client started.")

# Get the channel entity
channel = client.get_entity(channel_username)
print(f"Channel: {channel.title}")

# Fetch the latest 10 messages
history = client(GetHistoryRequest(
    peer=channel,
    limit=10,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0
))
print(f"Fetched {len(history.messages)} messages.")
for message in history.messages:
    print(f"\n🧾 {message.date}")
    print(f"📜 {message.message}")
