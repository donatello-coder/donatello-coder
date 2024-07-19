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

@bot.command()
async def eh(ctx):   
    # ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
    problems = os.listdir('problem')
    chosen_problem = random.choice(problems)
    if str(chosen_problem) == "Acid_Rain.jpg":
         mensaje = "Encourage the production and use of renewable energy instead of fossil fuels"
    if str(chosen_problem) == "Global warming.jpg":
         mensaje = "Las carreteras del mundo están saturadas de vehículos, la mayoría de los cuales usan diésel o gasolina. Caminar o ir en bicicleta en lugar de conducir reduce las emisiones de gases de efecto invernadero."
    if str(chosen_problem) == "Ocean acidification.jpg":
         mensaje = "Fight ocean acidification by reducing your carbon dioxide emissions at home, at the office, and on the road. Fight coastal acidification by limiting nutrient pollution at home, in your yard, and in your community."
    if str(chosen_problem) == "Polution.jpg":
         mensaje = "Specific means of pollution control might include refuse disposal systems such as sanitary landfills, emission control systems for automobiles, sedimentation tanks in sewerage systems, the electrostatic precipitation of impurities from industrial gas, or the practice of recycling."
    if str(chosen_problem) == "Waste disposal.jpg":
         mensaje = "Some of the various waste management types or methods include landfilling, incineration, recycling, composting, waste-to-energy, and source reduction. The method used in disposing of waste would depend on the type of waste."
    if str(chosen_problem) == "Water scarcity.jpg":
         mensaje = "Solutions to addressing water shortages include dams and reservoirs, rainwater harvesting, aqueducts, desalination, water reuse, and water conservation."

    with open(f'problem/{chosen_problem}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(mensaje, file=picture)

# client.run(TOKEN)
bot.run(TOKEN)
