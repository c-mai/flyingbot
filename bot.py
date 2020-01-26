import discord
import os
import quickstart
import csv

from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if "!create" in message.content:
            date = message.content.split()[1]

            v = False
            with open('vlosheets.csv', 'r') as file:
                file.readline()
                for line in file:
                    data = line.split(',')
                    if(data[0] == date or data[0] == 'e'):
                        event = "- " + date + " " + data[1] + " - " + data[2] + " : " + data[3] 
                        await message.channel.send(event)
                        v = True
            
            if not v:
                await message.channel.send("There were no volunteer opportunities found for that date. Try creating a different event.")
            else:
                await message.channel.send("These opportunities were found for your date! \nReact a :thumbsup: to your favorite event to add to calendar.")

                

    
    async def on_raw_reaction_add(self, payload):
        if str(payload.emoji) == "👍":
            dm = await payload.member.create_dm()
            s = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
            date = s.content.split()[1]
            start = s.content.split()[2]
            end = s.content.split()[4]
            event = " ".join(s.content.split()[6:])

            def check(m):
                return m.channel == client.get_channel(dm.id) and m.author != client.user
                
            while True:
                await payload.member.dm_channel.send("You have chosen to participate in:\n" + s.content + "\nPlease provide a working Gmail.")
                email = await client.wait_for('message', check=check)
                if "@gmail.com" in email.content:
                    break

            
            quickstart.sendEvent(date, start, end, event, email.content)
            await payload.member.dm_channel.send("Please check your Google calendar; an event should be created! \nThank you for giving back to the community!")

           


client = MyClient()
client.run(token)
