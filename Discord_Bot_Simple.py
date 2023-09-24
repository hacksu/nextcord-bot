import nextcord
import random
import asyncio
from nextcord.ext import commands

description = "Basic example bot"
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

@bot.event
async def on_message(message):
    if("😎" in message.content):
        await message.add_reaction("😎")
    await bot.process_commands(message)

#WHEN READY
@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name = "My First Bot!"))
    print("Successfully set Bot's game status")

@bot.command(help="pong!")
async def ping(ctx):
    await ctx.send("pong")

@bot.command(help="ask the 8ball a question")
async def eightball(ctx):
    RESPONSES = [
        "Yes",
        "No",
        "Maybe",
        "That's up to you",
        "Ask again later",
        #Add more here!
        ]
    msg = random.choice(RESPONSES)
    await ctx.send(msg)

@bot.command(help="see who is online!")
async def scan(ctx):
    msg = "The list of all online members are:\n```"

    for member in ctx.guild.members:
        if(member.status == nextcord.Status.online):
            msg += str(member)+"\n"
    msg += "```"
    await ctx.send(msg)

# @bot.command()
# async def help(message):
#     await message.channel.send("""I have the following commands:```
# /help - shows this message
# /ping - pong!
# /8ball - ask the 8Ball a question
# /scan - see who is online!
# ```""")
          

print("Starting Bot")
file = open("../test/bot_token.txt",'r')#change this to the path of your token
TOKEN = file.read()
#print(TOKEN)
bot.run(TOKEN)
