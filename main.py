import discord
import os
import requests
import json
import random
import discord. utils
from discord.ext import commands
import typing
##
activity = discord.Activity(type=discord.ActivityType.watching, name="|help")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="|", intents=intents, activity=activity,
                   status=discord.Status.online)

bot.remove_command('help')
##
client = discord.Client()
sad_words = ["sad", "unhappy", "depressed", "dispair", "angry", "miserable","die", "depressed", "suicidal","lonely" ]

starter_encouragements = ["Cheer up", "Hang in there", "U Great", "Die nicely"]




def get_Quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


async def get_Wallpaper():
    photo = requests.get("")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('-inspire'):
        quote = get_Quote()
        await message.channel.send(quote)
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    if msg.startswith("$new"):
        starter_encouragements.append(msg.split("$new", 1)[1])
        await message.channel.send("It worked")
    if msg.startswith("-HopOn"):
        x = "@The Naughty Brazil Zone"
        await message.channel.send("@everyone" + " League Now")
    if msg.startswith("-noone"):
        await message.channel.send("🍰 You have given one cake to" + client.users.index(0) + " 🍰")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Fuck U {member.name}, welcome to my Discord server!'
    )






client.run('ODY0MjA1MjU0ODQ4MjgyNjM0.GfTFc9._S1AuS77m1eRlY-SGSCBPoB6OAcxHCse6NWL0o')
