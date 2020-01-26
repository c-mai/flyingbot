import discord
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def v_search(month, day, year):
    return '01', '01', '1999'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if "!create" in message.content:
            await message.channel.send("Great! I have these volunteer opportunities on that date. \nReact a :thumbsup: to add to calendar: ")
            date = message.content.split()[1].split("-")
            month, day, year = date
            vlist = v_search(month, day, year)

            for x in vlist:
                await message.channel.send(x)
    
    async def on_raw_reaction_add(self, payload):
        if str(payload.emoji) == "👍":
           await payload.member.create_dm()
           s = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
           await payload.member.dm_channel.send("You have chosed to particpate:\n" + s.content)

client = MyClient()
client.run(token)
