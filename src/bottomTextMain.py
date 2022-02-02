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
# Sample discord ID: '138133173707057152'
user_ID = '138133173707057152' #id of user we wish to send messages to

@client.event
async def on_ready():
    #Wait to perform task until given time
    user = await client.fetch_user(user_ID)

    allFiles = listdir('messages\\')#Fetch all messages from folder
    print(allFiles)

    pause.until(1629522000) #time stamp for aug 24th 2021

    count = 0
    for x in range(len(allFiles)-1):
        count+=1
        file = open(f'messages\\{allFiles[x+1]}', 'r') #open individual txt file
        message = file.readlines()

        print(f'Sending package {count} to user')

        #messages are written with dilimeters. If first character is * it will pause for the integer value following it
        #If first character is ~it will send an incorporated image
        for line in message:
            if (line[0] == '*'):
                time.sleep(int(line[1:]))
            elif (line[0] == '~'):
                await user.send(file=discord.File(line[1:].rstrip()))
            else:
                await user.send(line)
            time.sleep(3)
        file.close()
        await user.send("==================================================================================================")
        await user.send("==================================================================================================")
        time.sleep(3600)
    pass



client.run(TOKEN)