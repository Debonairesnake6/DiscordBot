import discord
import datetime
import asyncio
import MySQLdb
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, time

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="123456789",
                     db="420database")
cur = db.cursor()

client = commands.Bot(command_prefix="b!")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=' with joints'))
    print("client Online!")
    print("Name: " + client.user.name)
    print("ID: " + client.user.id)

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Hello")


@client.command(pass_context=True)
async def addchannel(ctx):
    await client.say("Channel added to database.")

    
 
async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='409941922388639744')
    while not client.is_closed:

        now = datetime.now()
        gmthr = now.hour + 5  ## +5 to get from EST to GMT
        offset = 16 - gmthr ## 16 is 4 pm, so to find offset we take target hr and minus GMT.
        
        minute = now.minute

        if minute == 20:
            cur.execute("SELECT timeZone FROM timezoneinfo WHERE ID = " + str(offset))
            timeZone = ''.join(cur.fetchone())

            cur.execute("SELECT message FROM timezoneinfo WHERE ID = " + str(offset))
            message = ''.join(cur.fetchone())
    
            await client.send_message(channel, 'It\'s 4:20pm in ' + str(timeZone) + ', happy tokes to those in ' + str(message) + '!' )
            
            await asyncio.sleep(3540)
        else: 
            await asyncio.sleep(1)

client.loop.create_task(my_background_task())

client.run("NDM2NzI1OTg2Njg4NDk5NzQy.DbrsaA.aLKkZ-YT8npp12AK9auj7DrSVLk")
