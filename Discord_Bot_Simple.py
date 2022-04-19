import nextcord
import asyncio
import random


class MyClient(nextcord.Client):

    
    #ON MESSAGE
    async def on_message(self,message):
        if(message.content.startswith("/")):
            await self.process_commands(message)

        if("😎" in message.content):
            await message.add_reaction("😎")


    #PROCESS COMMANDS
    async def process_commands(self,message):
        command = message.content.split()[0].lower()
        #Command List Here
        if(command == "/ping"):
            await self.pong(message)
        elif(command == "/8ball"):
            await self.eightBall(message)
        elif(command == "/scan"):
            await self.scan(message)
        elif(command == "/help"):
            await self.help(message)


    async def pong(self,message):
        await message.channel.send("pong")

    async def eightBall(self,message):
        RESPONSES = [
            "Yes",
            "No",
            "Maybe",
            "That's up to you",
            "Ask again later",
            #Add more here!
            ]
        msg = random.choice(RESPONSES)
        await message.channel.send(msg)

    async def scan(self,message):
        msg = "The list of all online members are:\n```"

        for member in message.guild.members:
            if(member.status == nextcord.Status.online):
                msg += str(member)+"\n"
        msg += "```"
        await message.channel.send(msg)

    async def help(self,message):
        await message.channel.send("""I have the following commands:```
/help - shows this message
/ping - pong!
/8ball - ask the 8Ball a question
/scan - see who is online!
```""")
          

    #WHEN READY
    async def on_ready(self):
        await self.change_presence(activity=nextcord.Game(name = "My First Bot!"))
        print("Successfully set Bot's game status")



print("Starting Bot")
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
#print(TOKEN)
bot.run(TOKEN)
