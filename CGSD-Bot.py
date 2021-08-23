import discord
import os
from datetime import datetime
from keep_alive import keep_alive
from commands import *

class MyClient(discord.Client):

    async def on_ready(self):
        print('---------------------------------------------------')
        print(f'Conectado como {self.user.name}, id = {self.user.id}')
        print('---------------------------------------------------')

    async def on_message(self, message):
        # Para o bot não se auto responder
        if message.author.id == self.user.id:
            return

        if message.content == message.content:
          await say_hi(message)
          await reply_embed(message, client)


client = MyClient()
my_secret = os.environ['token']
client.run(my_secret)