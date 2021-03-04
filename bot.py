import discord
from discord.ext import commands
import redis

bot = commands.Bot(command_prefix="none")

client = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8")


@bot.event
async def on_ready():
    print("Ready")


@bot.event
async def on_message(message):
# If you want to filter by a specific server uncomment this
#    if(message.guild.id != 349243932447604736): 
#        return
    msg = message.content

    if msg:

        client.lpush("messages", msg)

        print("[PUSHED] " + msg)


bot.run("", bot=False)
