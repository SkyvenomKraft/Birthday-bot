import os
from os import listdir
import discord
from dotenv import load_dotenv
import time
import pause
import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
SkyID = '138133873707057152'
IceID = '717667111794901003'


@client.event
async def on_ready():
    # #Wait to perform task until saturday at midnight
    # userSky = await client.fetch_user(SkyID)
    # userIce = await client.fetch_user(IceID)
    #
    # allFiles = listdir('Ice\'s Suprise\\!FINAL MESSAGES!\\')
    # print(allFiles)
    #
    # pause.until(1629522000)
    #
    # count = 0
    # for x in range(len(allFiles)-1):
    #     count+=1
    #     file = open(f'Ice\'s Suprise\\!FINAL MESSAGES!\\{allFiles[x+1]}', 'r')
    #     message = file.readlines()
    #
    #     print(f'Sending package {count} to Sky')
    #     print(f'Sending package {count} to Ice')
    #     for line in message:
    #         if (line[0] == '*'):
    #             time.sleep(int(line[1:]))
    #         elif (line[0] == '~'):
    #             await userSky.send(file=discord.File(line[1:].rstrip()))
    #             await userIce.send(file=discord.File(line[1:].rstrip()))
    #         else:
    #             await userSky.send(line)
    #             await userIce.send(line)
    #         time.sleep(3)
    #     file.close()
    #     await userSky.send("==================================================================================================")
    #     await userIce.send("==================================================================================================")
    #     time.sleep(3600)
    pass



client.run(TOKEN)