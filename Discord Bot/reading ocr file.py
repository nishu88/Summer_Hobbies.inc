import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from PIL import ImageGrab,Image,ImageEnhance,ImageOps
from tesserocr import PyTessBaseAPI
import filecmp

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
##    await client.say("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="Keep Calm and Believe"))

@client.event
async def on_message(message):


    if message.content.lower().startswith('?go'):
        await client.send_message(message.channel, "Waiting")
    
        while True:
            data=" "
            await asyncio.sleep(0.5)

            if message.content.lower().startswith('?stop'):
                await client.send_message(message.channel, "Resting")
                break
            try:
                if not filecmp.cmp('freefall.txt','C:/Users/nishu88/Downloads/Blot/bin/Temp/temp.txt') :
                    
                    with open(r'C:/Users/nishu88/Downloads/Blot/bin/Temp/temp.txt') as f:
                        with open('freefall.txt', 'w')as f1:
                            for line in f:
                                f1.write(line)
                                data=data+line

                    print(data)        


                    
                            


                    
                    await client.send_message(message.channel, "?guess "+data)
                    
            except FileNotFoundError:
                continue

                    #print(s)









client.run('NDY0MDcyMjA0OTU1NDE4NjI0.Dh5o1g.npsAT1VO4Beo98dYsG9BhknUIX0')






    
