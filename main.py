from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response


#Step 0: Load Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

#Step 1: Bot Setup

intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

#STEP 2: Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print ('(Message was empty becasue intents were not enavled probably)')
        return
    
    is_private = user_message[0] =='?'
    
    if is_private:
        user_message = user_message[1:]
    
    # Sends to user if private, else messages in channel
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
# Step 3: Handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    
#Step 4: Handling incoming messages
@client.event
async def on_message(message:Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message:str = message.content
    channel:str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
#Step 5: Main Entry Point
def main() -> None:
    client.run(token = TOKEN)
    
if __name__ == '__main__':
    main()