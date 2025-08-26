import asyncio
import tempfile
import time
import discord
from discord.ext import commands, tasks
from albion_api import killBoard
import io
import os
from dotenv import load_dotenv
import numpy as np
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='3', intents=intents)
load_dotenv()
token = os.getenv("API_KEY")
print(token)
#token = open("venv\Resources\API.env", "r")
#token = token.read()

@bot.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(bot))

@bot.command()
async def kb_call(ctx):
    await ctx.send("Bot Activo")
    kb_loop.start(ctx)

@tasks.loop(minutes=1)
async def kb_loop(ctx):
    for i, kb_images in enumerate(range(5),1):
        embed = discord.Embed(
            title=killBoard(i).killer_name + " Killed " + killBoard(i).victim_name,
            description="Parcitipants: " + killBoard(i).participants_names,
            color=discord.Color.red()
        )
        embed_inv = discord.Embed(
            title="inventory",
            description="placeholder",
            color=discord.Color.red()
        )

        image = killBoard(i).kb_image()
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp:
            image.save(temp.name)
            temp_image = discord.File(temp.name, filename="image.png")
            embed.set_image(url="attachment://image.png")
            embed.set_author(name='Albion Killbot - Developed by Sentu', url="https://github.com/Sentu-Is",icon_url="attachment://albion_png.png")
            await ctx.send(embed=embed, file=temp_image)

        inventory = killBoard(i).kb_inventory()
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_inv:
            inventory.save(temp_inv.name)
            temporal_inventory = discord.File(temp_inv.name, filename="image.png")
            embed_inv.set_image(url="attachment://image.png")
            embed_inv.set_author(name='Albion Killbot - Developed by Sentu', url="https://github.com/Sentu-Is",icon_url="attachment://albion_png.png")
            await ctx.send(embed=embed_inv, file=temporal_inventory)



    await asyncio.sleep(65)
@kb_loop.before_loop
async def before_kb_loop():
    await bot.wait_until_ready()
bot.run(token)







