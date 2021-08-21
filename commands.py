import discord
from discord.ext import commands
from datetime import datetime

# RESPONDE O HELLO
async def say_hello(self):
  if self.content == 'hello':
    await self.reply('Hello!') 


#Aqui dentro vamos colocar o Embed do bot, com sua descrição e comandos
async def reply_embed(self):
    if self.content.startswith('#'):
          # EMBEDED
      if 'help' in self.content:
        embed = discord.Embed(

        title="COMANDOS:", 
        description="", 
        colour=0x87CEEB,
        timestamp=datetime.utcnow()

        )
        embed.add_field(name="Prefixo:", value="#", inline=False)
        embed.add_field(name="Comandos:", value="help, mercado, ping", inline=False)
 
        await self.reply(embed = embed)

          # FIM EMBEDED

async def say_ping(self, cli):
    if 'ping' in self.content:
      await self.reply(f'Pong! {round(cli.latency * 1000)}ms')
        
        
        # ois = ['Oi', 'oi', 'OI', 'oI', 'Oi!']
        # if message.content == message.content:
        #   for o in ois:
        #     if message.content == o:
        #       await message.reply('Oi!')
        #     else:
        #       pass
        