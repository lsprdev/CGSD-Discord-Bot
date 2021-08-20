import discord

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        

    async def on_message(self, message):
        
        if message.author == self.user:
            return

        if message.content == 'Hi':
            await message.channel.send('Hi, how are you?')

client = MyClient()
client.run('Put your bot token here')
