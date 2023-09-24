# Hacksu-Lesson-Discord-Bot-Easy

## Intro

Discord, for those who are unfamilar, is a free text and voice chatting platform. You will need a Discord account in order to make and interact with a bot. You can create an account free at their [website](https://discord.com). You can either use Discord through the Desktop Application or through the browser. Additionally, you will need Python 3.8 installed. You can download Python from [here](https://python.org)

## Installing nextcord

In order to be able to code your bot, you will need to install the nextcord module. To do so, follow these steps.

1: Open up your computer's command line interface. For Windows, this is a program called Command Prompt (or Powershell if you would prefer). For Mac and Linux, this is called Terminal.
2: Execute the following command

````
pip install nextcord
````

If Python was installed correctly, you should see output that looks somewhat like (yours will probably look slightly different) to this:
![pip successful](https://i.imgur.com/fQpGOzT.png)
If you don't see this and/or you get an error stating "pip is not recognized as a command" then you will need to unistall and then reinstall Python. When you reinstall, make SURE that you check the box that says "Add Python to your PATH". If you do not, you will not be able to use the pip command to get nextcord.

## Creating a Server

Now that you are able to make a bot, you need to make a place for it to live. To get started, open up Discord and follow these steps:

1: Select the plus button at the bottom of your server list.

![add a server](https://i.imgur.com/xpYb4bU.png)

2: Select the "Create My Own" button.

![create my own](https://i.imgur.com/0j2pswe.png)

3: Name the server whatever you want, and then click "Create"

![name server](https://i.imgur.com/OdIlEhC.png)

You should now see a blank server in your server list!

![blank server](https://i.imgur.com/YBfzuF5.png)

## Now to create the bot

Last step before coding; we have to tell Discord to make the bot account for us. Go to the [Discord Developer Portal](https://discordapp.com/developers/applications) and follow these steps:

1: Select "New Application", and name your bot whatever you would like.

2: When the application is created, go to the "Bot" tab and select "Reset Token" or "Reveal Token"

3: Click on the "Copy" button that appears. This will copy the bot's Token to your clipboard, which is essentially the bot's username and password. Do not share this token with anyone else.

4: Create a text file and paste your bot's token into it for later. 

## Adding the bot to the server

Navigate back to your bot's Application page and follow these steps:

1: Select the OAuth2 tab

2: Under the URL generator tab, select "bot" in the scopes checklist

3: Select "Send Messages", "Read Message History", and "Add Reactions" in the bot permissions checklist that appears

4: Copy the URL it gives you, and paste it into your browser

5: From the list of servers, select the server you want to add the bot to, and then click "Authorize". If prompted, solve a CAPTCHA.

You should now see the bot in the member list, but it will say it is offline. To make it appear online, we have to actually code the bot's logic!

## Coding the bot

Now to write the bot. This lesson recommends using Python IDLE (which comes with your installation of Python) to code, but any IDE will work.

Create a new folder where you want your code to be, and then inside that folder create a new file called "bot.py".

The first step is to add the include statements. By default, Python can't access the nextcord module until we import it. Add `import nextcord` to the file. Additionally, we will also need the asyncio and datetime libraries, so add `import asyncio` and `import random` to the file.

Your file should now look like this:

````
import nextcord
import asyncio
import random
````

The next step is to set some variables which will describe the behavior of our bot, and then to create a nextcord bot object using these variables. 
Set the following variables below the import statements:

````
description = "my bot"
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)
````

These variables define some important information about our bot. The intents object describes which kind of events our bot will need to access. Setting intents.members and intents.message_content to True allows our bot to access the content of messages and see the members of a server.

The last line creates an object which serves as our bot. We pass a prefix, a short description of our bot, and the intents defined above to the Bot constructor, which tells nextcord how to configure our bot. The prefix is used to differentiate normal messages in the server, with messages directed towards our bot. 

First, we need to have the bot awaken and perform actions when it sees that someone has sent a message. To do this, we will create a function called `on_message`.

Add this below the bot variable:

````
@bot.event
async def on_message(self,message):
    await self.process_commands(message)
````

This block of code will be run everytime our bot sees a message. The bot checks the beginning of the message's text, and sees if it starts with the prefix we defined earlier. If it does, the `process_commands` function handles the rest of the message. This function is built into nextcord, so we don't have to worry about writing it ourselves.  

The `process_commands` function is going to look for functionality we add to the bot based on the user's input. For example, we can create a simple command `!ping` to which our bot will respond `pong`. In this case, each command is added using a decorator which adds the function below it to the bot object.

To add this command, add the following code:

````
@bot.command()               #  <- decorator
async def ping(ctx):         #  <- function
    await ctx.send("pong")
````

This command is very basic, as stated above. When the function gets called, the bot looks up what channel the command message was sent in, and then sends its own message to the same channel, making it look like the bot has responded! Before we can test this though, we have to have our bot log in!

## Adding the Bot's Token

At the end or your file, add the following lines of code

````
file = open("TOKEN.txt",'r')
TOKEN = file.read()
bot.run(TOKEN)
````

These lines of code will open up a file that contains the bot's token, and then connect the bot to Discord's servers. It is not super important to understand how all this code works. However, we need to create the `TOKEN.txt` file! Go to the folder you made earlier, and create a new file named TOKEN.txt. Inside this file, paste in your bot's token that you copied from your Discord Developer Page. If you have done so correctly, you can run your bot!

## Running the Bot and the Final Commands

Run your bot, go to the new server you made, and type `!ping`. Your bot should respond with `pong`.

To catch up, your code should look like this:

````
import nextcord
import asyncio
import random

description = "my bot"
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)
        
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
@bot.comand()
async def ping(ctx):
   await ctx.send("pong")
        
file = open("TOKEN.txt",'r')
TOKEN = file.read()
bot.run(TOKEN)
````

There are 3 more commands we want to add, the first of which is a Magic 8 Ball!

 Let's implement the function:

````
@bot.command()
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
````

In this function, we declare a list of a bunch of strings, each being a possible message that the bot can respond with. We then set `msg` equal to a random one using the `random.choice` function, and finally we send the random message back to the channel the command was called in. Launch your bot and give it a try!

Next up is a scan function. 

Discord bots can do more than just send messages - they can look at pretty much any data a normal user can. With this command, we are going print all the users who currently have their status as "online" in the server. Here is the code:

````
@bot.command()
async def scan(ctx):
    msg = "The list of all online members are:\n```"

    for member in ctx.guild.members:
        if(member.status == nextcord.Status.online):
            msg += str(member)+"\n"
    msg += "```"
    await ctx.send(msg)
````

This command is a big one! Let's walk through it. We first create a starting point for our message back to the user. Then, using a for loop, we get all of the members that are currently in the guild. For each member, we get their current status. If it is equal to being online, we turn them into a string and then add them to our message. Afterwards, we send the message back to the channel. If you run this in the new server you have created, you should see the bot list two names; itself and you. Try making yourself go onto Do Not Disturb and run the command again. The bot should only report itself now!

Our last command is a very simple one, but helps make our bot more accessible to new users. `!help` will have the bot print a message that details everything it can do. Luckily for us, most of the help command is already included as part of nextcord!

If you run the help command without doing anything extra, you should see something like this:

````
Basic example bot

​No Category:
  eightball 
  help      Shows this message
  ping      
  scan      

Type !help command for more info on a command.
You can also type !help category for more info on a category.
````

In order to add explanations for our commands we need to add a parameter to each of the `@bot.command()` decorators we added above our commands. For each command do something like this:

````
@bot.command(help="describe what your command does here")
````

This should tell nextcord to populate the help command with your custom message. If you run your bot again you should see your descriptions added to the help command!

````
Basic example bot

​No Category:
  eightball ask the 8ball a question
  help      Shows this message
  ping      pong!
  scan      see who is online!

Type !help command for more info on a command.
You can also type !help category for more info on a category.
````

We now have a bot that has 4 fun and unique commands! But we aren't done yet - let's also give our bot a cool personallity!

## Reacting to a message

We want our bot to be a cool bot, so we are gonna make it react to any cool message with the sunglasses emoji.

Go back up to the `on_message` command and add the following if statement to the function:

````
if("😎" in message.content):
    await message.add_reaction("😎")
````

Now, whenever our bot sees a message that contains 😎, it will react to that image with 😎.

## Unique Challenge

Our bot is finally done, but that doesn't mean we have exhausted everything it can do! Bots are limitless with what they can do, and you can do basically anything you want with them! As this week's Unique Bingo Challenge, read through the official nextcord documentation (found [here](https://docs.nextcord.dev/en/latest/api.html)), and implement a feature that wasn't used in this lesson! This can be something like posting an image, giving itself a nickname, anything you want! 
