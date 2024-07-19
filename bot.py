import discord
import os
import random
from bot_logic import random_hero
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    # To avoid eternal cycle
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send("bye(:")
    elif message.content.startswith('/random_hero_academy_character'):
        await message.channel.send(random_hero())
    else:
        await message.channel.send("I can't answer that")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def meme(ctx):   
    # ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
    imagenes = os.listdir('images')
    with open(f'images/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

# client.run(TOKEN)
bot.run(TOKEN)
