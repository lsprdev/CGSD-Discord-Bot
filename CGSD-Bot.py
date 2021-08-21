import discord
import os
from datetime import datetime
from keep_alive import keep_alive

class MyClient(discord.Client):
    async def on_ready(self):
        print('----------------')
        print(f'Logged in as {self.user}, id = {self.user.id}')
        print('----------------')

    async def on_message(self, message):
        # Para o bot não se auto responder
        if message.author.id == self.user.id:
            return


        #Aqui dentro vamos colocar o Embed do bot, com sua descrição e comandos
        if message.content.startswith('$'):
          # EMBEDED

          if 'help' in message.content:

            embed = discord.Embed(

              title="COMANDOS:", 
              description="", 
              colour=0x87CEEB,
              timestamp=datetime.utcnow()

            )
            embed.add_field(name="Prefixo:", value="$", inline=False)
            embed.add_field(name="Comandos:", value="help, mercado, ping", inline=False)
 
            await message.reply(embed = embed)

          # FIM EMBEDED


          if 'ping' in message.content:
            await message.reply(f'Pong! {round(client.latency * 1000)}ms')
        
        
        ois = ['Oi', 'oi', 'OI', 'oI', 'Oi!']
        if message.content == message.content:
          for o in ois:
            if message.content == o:
              await message.reply('Oi!')
            else:
              pass
        

keep_alive()

client = MyClient()
my_secret = os.environ['token']
client.run(my_secret)