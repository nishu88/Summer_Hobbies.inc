import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from PIL import ImageGrab,Image,ImageEnhance,ImageOps
from tesserocr import PyTessBaseAPI


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

        img = ImageGrab.grab(bbox=(0,300,350,700))



        #LOCO and qureka

        img = img.convert("L")
        img=ImageOps.invert(img)     #L0C0
        brighter = ImageEnhance.Brightness(img)
        ##img = brighter.enhance(2.5)  #3
##        contrast = ImageEnhance.Contrast(img)
##        img = contrast.enhance(100)
##
##        sharper = ImageEnhance.Sharpness(img)
##        img = sharper.enhance(100)
        img = brighter.enhance(3)



        thresh = 200
        fn = lambda x : 255 if x > thresh else 0
        img= img.convert('L').point(fn, mode='1')



        #BRAINBAAZI AND SWOO

        ##img = img.convert("L")



        img.save('blah.png')

        s=[]

        with PyTessBaseAPI(path=r'C:\Tesseract-OCR\tessdata') as api:
            api.SetImageFile('blah.png')
            s=api.GetUTF8Text()    
            s=s.replace('\n\n','\n')
            s=s.replace('\n ',' ')
            if s[0]==' ':
                s=s[1:]

            
            await client.send_message(message.channel, "?guess "+s)

            print(s)









client.run('NDY0MDcyMjA0OTU1NDE4NjI0.Dh5o1g.npsAT1VO4Beo98dYsG9BhknUIX0')






    
