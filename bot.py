# bot.py
import os
import discord
import json

from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='?', status=discord.Status.idle, intents=intents)

guild = discord.Object(GUILD)

##Console Event, shows successfull start
@bot.event
async def on_ready():           
    print(bot.user.name,"with BotUserID", bot.user.id, "logged in!")
    print('---------------------')
    print('Started!')

##A Basic / Command
@bot.tree.command(name = "WolkiReaper", description="Basic / Command")   
async def toast(interaction: discord.Interaction):
    await interaction.response.send_message("WolkiReaper!")



bot.run(TOKEN)