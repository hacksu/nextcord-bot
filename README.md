# Hacksu-Lesson-Discord-Bot-Easy
## Intro
Discord, for those who are unfamilar, is a free text and voice chatting platform. You will need a Discord account in order to make and interact with a bot. You can create an account free at their [website](https://discord.com). You can either use Discord through the Desktop Application or through the browser. Additionally, you will need Python 3.8 installed. You can download Python from [here](https://python.org)
## Installing discord.py
In order to be able to code your bot, you will need to install the Discord.py module. To do so, follow these steps.

1: Open up your computer's command line interface. For Windows, this is a program called Command Prompt (or Powershell if you would prefer). For Mac and Linux, this is called Terminal. 
2: Execute the following command
```
pip install discord
```
If Python was installed correctly, you should see output that looks somewhat like (yours will probably look slightly different) to this:
![pip successful](https://i.imgur.com/fQpGOzT.png)
If you don't see this and/or you get an error stating "pip is not recognized as a command" then you will need to unistall and then reinstall Python. When you reinstall, make SURE that you check the box that says "Add Python to your PATH". If you do not, you will not be able to use the pip command to get Discord.py.
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

1: Select "New Application". This tutorial is going to make a bot that tells the time, so when prompted, name your application "Time Bot".

2: When the application is created, go to the "Bot" tab and select "Add Bot" and then "Yes, do it!"

3: Click on the "Copy" button that appears. This will copy the bot's Token to your clipboard, which is essentially the bot's username and password. Do not share this token with anyone else. 

## Adding the bot to the server
Navigate back to your bot's Application page and follow these steps:

1: Go to the OAuth2 tab

2: From the checklist, select "bot"

3: Copy the URL it gives you, and paste it into your browser

4: From the list of servers, select the server you want to add the bot to, and then click "Authorize". If prompted, solve a CAPTCHA.

You should now see the bot in the member list, but it will say it is offline. To make it appear online, we have to actually code the bot's logic!
## Coding the bot
Now to write the bot. This lesson recommends using Python IDLE (which comes with your installation of Python) to code, but any IDE will work.

Create a new folder where you want your code to be, and then inside that folder create a new file called "bot.py".

The first step is to add the include statements. By default, Python can't access the Discord.py module until we import it. Add ```import discord``` to the file. Additionally, we will also need the asyncio and datetime libraries, so add ```import asyncio``` and ```import random``` to the file.

Your file should now look like this:
```
import discord
import asyncio
import random
```

The next step is to create a class that inherits from the discord.Client class. Creating an inherited class allows us to make our own personal bot by adding our own features. Don't worry if you don't know exactly what an inherited class means, it isn't neccessary to creating your bot.
Type ```class MyClient(discord.Client):``` to your file, and then hit enter. Make sure your cursor is also tabbed over after you hit enter.

This class is where we are going to add all of our bot's functionality. First, we need to have the bot awaken and perform actions when it sees that someone has sent a message. To do this, we will create a function called ```on_message```.

Add this inside your class
```
async def on_message(self,message):
    if(message.content.startswith("/")):
        await self.process_commands(message)
```

This block of code will be run everytime our bot sees a message. The bot checks the beginning of the message's text, and sees if it starts with a slash. If it does, it calls the ```process_commands``` function. This function doesn't exist yet though - lets make it!

The ```process_commands``` function is going to be where we determine which command the user tried to execute. It's basically going to be a long multiway if statement that checks for various keywords. Our bot is going to have 4 functions, so lets add them in!
```
async def process_commands(self,message):
    command = message.content.split()[0].lower()
    #Command List Here
```
The first line of the function takes the first word from what the user said. If the user typed ```/hello blah blah blah```, ```command``` will become equal to "/hello".
Below ```#Command List Here``` is where our multiway if statement is going. For right now, just add
```
if(command == "/ping"):
    await self.pong(message)
```
Now, when the user types ```/ping```, the ```ping``` function is ran. However, we if we launched the bot right now, calling this command would error our bot, since it doesn't have a function named ```ping```. Lets add our first and simplest command, /ping!

```/ping``` will make the bot respond with "pong". It's a very basic command and is generally used as a tester, but it will make a great first command for our bot!

To add this command, add the following code:
```
async def pong(self,message):
    await message.channel.send("pong")
```
This command is very basic, as stated above. When the function gets called, the bot looks up what channel the command message was sent in, and then sends its own message to the same channel, making it look like the bot has responded! Before we can test this though, we have to have our bot log in!
## Adding the Bot's Token
At the end or your file, add the following lines of code
```
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
bot.run(TOKEN)
```
These lines of code will create a new instance of your bot, open up a file that contains the bot's token, and then connect the bot to Discord's servers. Again, it is not super important to understand how all this code works. However, we need to create the ```TOKEN.txt``` file! Go to the folder you made earlier, and create a new file named TOKEN.txt. Inside this file, paste in your bot's token that you copied from your Discord Developer Page. If you have done correctly, you can run your bot!
## Running the Bot and the Final Commands
Run your bot, go to the new server you made, and type ```/ping```. Your bot should respond with ```pong```.

To catch up, your code should look like this:
```
import discord
import asyncio
import random


class MyClient(discord.Client):

    async def on_message(self,message):
        if(message.content.startswith("/")):
            await self.process_commands(message)
            
    async def process_commands(self,message):
        command = message.content.split()[0].lower()
        #Command List Here
        if(command == "/ping"):
            await self.pong(message)
            
    async def pong(self,message):
        await message.channel.send("pong")
        
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
bot.run(TOKEN)
```

There are 3 more commands we want to add, the first of which is a Magic 8 Ball!
Return to the ```process_commands``` messgae, and add this code underneath the ```/ping``` section
```
elif(command == "/8ball"):
    await self.eightBall(message)
```
This will now cause the ```eightBall``` command to be run whenever ```/8ball``` is typed. Let's go implement the function!
```
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
```
In this function, we declare a list of a bunch of strings, each being a possible message that the bot can respond with. We then set ```msg``` equal to a random one using the ```random.choice``` function, and finally we send the random message back to the channel the command was called in. Launch your bot and give it a try!

Next up is a scan function. Add this underneath the 8ball section in ```process_commands```
```
elif(command == "/scan"):
    await self.scan(message)
```
Discord bots can do more than just send messages - they can look at pretty much any data a normal user can. With this command, we are going print all the users who currently have their status as "online" in the server. Here is the code:
```
async def scan(self,message):
        msg = "The list of all online members are:\n```"

        for member in message.guild.members:
            if(member.status == discord.Status.online):
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
```
This command is a big one! Let's walk through it. We first create a starting point for our message back to the user. Then, using a for loop, we get all of the members that are currently in the guild. For each member, we get their current status. If it is equal to being online, we turn them into a string and then add them to our message. Afterwards, we send the message back to the channel. If you run this in the new server you have created, you should see the bot list two names; itself and you. Try making yourself go onto Do Not Disturb and run the command again. The bot should only report itself now!

Our last command is a very simple one, but helps make our bot more accessible to new users. ```/help``` will have the bot print a message that details everything it can do. Like the ```/pong``` command, it doesn't need anything fancy, just a message to send.

Add this to the multiway if statement:
```
elif(command == "/help"):
    await self.help(message)
```
And add this function
```
async def help(self,message):
    await message.channel.send("""I have the following commands:```
/help - shows this message
/ping - pong!
/8ball - ask the 8Ball a question
/scan - see who is online!
```""")
```
We now have a bot that has 4 fun and unique commands! But we aren't done yet - let's also give our bot a cool personallity!
## Reacting to a message
We want our bot to be a cool bot, so we are gonna make it react to any cool message with the sunglasses emoji.

Go back up to the ```on_message``` command. Below the first if statement, add this next one:
```
if("😎" in message.content):
    await message.add_reaction("😎")
```
Now, whenever our bot sees a message that contains 😎, it will react to that image with 😎.

## Unique Challenge
Our bot is finally done, but that doesn't mean we have exhausted everything it can do! Bots are limitless with what they can do, and you can do basically anything you want with them! As this week's Unique Bingo Challenge, read through the official Discord.py documentation (found [here](https://discordpy.readthedocs.io/en/latest/api.html)), and implement a feature that wasn't used in this lesson! This can be something like posting an image, giving itself a nickname, anything you want! Show a leader your bot in action and the new code you made, and you can check off that unique feature section on your Bingo Card!
