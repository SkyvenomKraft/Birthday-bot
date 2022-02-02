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

user_id = '138133873302057152'


@bot.command(help = "Manual run with offset designating where to start")
async def manual_run(ctx, offset):
    user = await bot.fetch_user(user_id)

    allFiles = listdir('messages\\')
    print(allFiles)

    pause.until(1629687600) #send at time stamp

    count = 0
    for x in range(len(allFiles)-offset):
        count += 1
        file = open(f'messages\\{allFiles[x+(offset-1)]}', 'r')
        message = file.readlines()

        print(f'Sending package {count+offset} to user')
        for line in message:
            if (line[0] == '*'):
                time.sleep(int(line[1:]))
            elif (line[0] == '~'):
                await user.send(file=discord.File(line[1:].rstrip()))
            else:
                await user.send(line)
            time.sleep(3)
        file.close()
        await user.send(
            "==================================================================================================")
        pause.until(1629687600+(count*3575))

@bot.command(help = "Manually send an individual message")
async def manual_send(ctx, msgNum):
    user = await bot.fetch_user(user_id)

    allFiles = listdir('messages\\')
    print(allFiles)


    count = int(msgNum)
    count += 1
    file = open(f'messages\\{allFiles[int(msgNum)-1]}', encoding = "utf8")
    message = file.readlines()

    print(f'Sending package {count} to user')
    for line in message:
        if (line[0] == '*'):
            time.sleep(int(line[1:]))
        elif (line[0] == '~'):
            await user.send(file=discord.File(line[1:].rstrip()))
        else:
            await user.send(line)
        time.sleep(3)
    file.close()
    await user.send(
        "==================================================================================================")

bot.run(TOKEN)