import os
from os import listdir
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time
import pause

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=">")

SkyID = '138133873707057152'
IceID = '717667111794901003'


@bot.command(help = "Manual run")
async def manual_run(ctx):
    userSky = await bot.fetch_user(SkyID)
    userIce = await bot.fetch_user(IceID)

    allFiles = listdir('Ice\'s Suprise\\!FINAL MESSAGES!\\')
    print(allFiles)

    offset = 23

    pause.until(1629687600)

    count = 0
    for x in range(len(allFiles)-offset):
        count += 1
        file = open(f'Ice\'s Suprise\\!FINAL MESSAGES!\\{allFiles[x+(offset-1)]}', 'r')
        message = file.readlines()

        print(f'Sending package {count+offset} to Sky')
        print(f'Sending package {count+offset} to Ice')
        for line in message:
            if (line[0] == '*'):
                time.sleep(int(line[1:]))
            elif (line[0] == '~'):
                await userSky.send(file=discord.File(line[1:].rstrip()))
                await userIce.send(file=discord.File(line[1:].rstrip()))
            else:
                await userSky.send(line)
                await userIce.send(line)
            time.sleep(3)
        file.close()
        await userSky.send(
            "==================================================================================================")
        await userIce.send(
            "==================================================================================================")
        pause.until(1629687600+(count*3575))

@bot.command()
async def manual_send(ctx, msgNum):
    userSky = await bot.fetch_user(SkyID)
    userIce = await bot.fetch_user(IceID)

    allFiles = listdir('Ice\'s Suprise\\!FINAL MESSAGES!\\')
    print(allFiles)


    count = int(msgNum)
    count += 1
    file = open(f'Ice\'s Suprise\\!FINAL MESSAGES!\\{allFiles[int(msgNum)-1]}', encoding = "utf8")
    message = file.readlines()

    print(f'Sending package {count} to Sky')
    print(f'Sending package {count} to Ice')
    for line in message:
        if (line[0] == '*'):
            time.sleep(int(line[1:]))
        elif (line[0] == '~'):
            await userSky.send(file=discord.File(line[1:].rstrip()))
            await userIce.send(file=discord.File(line[1:].rstrip()))
        else:
            await userSky.send(line)
            await userIce.send(line)
        # time.sleep(3)
    file.close()
    await userSky.send(
        "==================================================================================================")
    await userIce.send(
        "==================================================================================================")

bot.run(TOKEN)