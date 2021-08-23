import discord
from discord.ext import commands
from datetime import datetime

#Aqui dentro vamos colocar o Embed do bot, com sua descrição e comandos
async def reply_embed(self, cli):
    if self.content.startswith(';'):
          # EMBEDED
      if 'help' in self.content:
        embed = discord.Embed(
        title="COMANDOS:", 
        description="", 
        colour=0x4D1648,
        timestamp=datetime.utcnow()
        )
        embed.add_field(name="Prefixo:", value=";", inline=False)
        embed.add_field(name="Comandos:", value="help, ping, mercado", inline=False)
 
        await self.reply(embed = embed)
      else:
        pass







          # FIM EMBEDED

      if 'ping' in self.content:
        await self.reply(f'Pong! {round(cli.latency * 1000)}ms')
        

      if 'mercado' in self.content:
        embed = discord.Embed(

        title="COMANDOS MERCADO:", 
        description="Aqui você poderá comprar tags entre outras coisas dentro do servidor", 
        colour=0x000000,
        timestamp=datetime.utcnow()

        )
        embed.add_field(name="Prefixo:", value=";", inline=False)
        embed.add_field(name="Disponíveis pra a compra:", value="Tripulante Bronze, Tripulane Prata, Tripulante Ouro, Tripulante Diamante.", inline=False)
        embed.add_field(name="Comandos:", value="comprar(tag que você deseja comprar)",
        inline=False)
        embed.add_field(name='Exemplo:', value='comprar(Tripulante Bronze)')
 
        await self.reply(embed = embed)

      else:
        pass


# RESPONDE O Oi
async def say_hi(self):
  ois = ['Oi', 'oi', 'OI', 'oI', 'Oi!']
  if self.content == self.content:
    for o in ois:
      if self.content == o:
        await self.reply('Oi!')

      else:
        pass
        