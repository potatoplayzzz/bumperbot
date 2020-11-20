import discord
import time
from discord.ext import commands



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        while True:
            channel = client.get_channel(778764343491297298)
            await channel.send('@here BUMP THE SERVER PLEASE')
            time.sleep(7200)
            
           

        
    
    

client = MyClient()
client.run('Nzc4OTQxOTAzNzI1OTIwMjk4.X7ZULQ.qWaw7h81ne4siATlyQJqZbw7RZE')