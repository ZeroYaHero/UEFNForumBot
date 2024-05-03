import re
import requests
import discord
from discord.ext import commands
from enum import Enum

botintents = discord.Intents.default()
botintents.message_content = True
bot = commands.Bot(command_prefix='-',intents=botintents)

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

query = 'https://forums.unrealengine.com/user_actions.json?offset=0&username=bug-reporter&filter=4,5'

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

# @client.event
# async def on_message(message):
#     # print(f'Message from {message.author}: {message.content}')
#     if message.author == client.user:
#         return
#     else:
#         response = requests.get(query)
#         recentticket = response.json()['user_actions'][0]
#         await message.channel.send(str(recentticket['excerpt']))
#     await bot.process_commands(message)
    
# Replies -> 5, Posts -> 4, Likes -> 1
# @bot.command(name='likes')
# async def listUserLike(ctx, user = None, count = 1):
#     print('Command called')
#     if user == None:
#         await ctx.send('Unable to make request. Please supply user argument.')
#     else:
#         userquery = f'https://forums.unrealengine.com/user_actions.json?offset=0&username={user}&filter=4,5'
#         response = requests.get(userquery)
#         if response.ok:
#             messagetosend = []

#             actionindex = 0
#             for i in range(0, count):
#                 while True:
#                     try:
#                         useraction = response.json()['user_actions'][actionindex]
#                         actionindex += 1
#                         if useraction['action_type'] == 1:
#                             messagetosend.append(response.json()['user_actions']['title'] + '\n')
#                             break
#                     except:
#                         await ctx.send(f'Did not find any likes for user: {user}')
#                         return None

#             await ctx.send(messagetosend)
#         else:
#             await ctx.send('User not found.')

@bot.command()
async def list(ctx, filter = {4,5}, user = None, count = 1):
    print('Command called')
    for i in filter:
        
        await ctx.send(filter)
    await ctx.send(filter)
    return 
    if user == None:
        await ctx.send('Unable to make request. Please supply user argument.')
    else:
        userquery = f'https://forums.unrealengine.com/user_actions.json?offset=0&username={user}&filter={", ".join(str(e) for e in filter)}'
        response = requests.get(userquery)
        if response.ok:
            messagetosend = []

            actionindex = 0
            for i in range(0, count):
                while True:
                    try:
                        useraction = response.json()['user_actions'][actionindex]
                        actionindex += 1
                        if useraction['action_type'] == 1:
                            messagetosend.append(response.json()['user_actions']['title'] + '\n')
                            break
                    except:
                        await ctx.send(f'Did not find any likes for user: {user}')
                        return None

            await ctx.send(messagetosend)
        else:
            await ctx.send('User not found.')



bot.run('MTIzNTY3OTM5NDk1ODE1MTY4MA.GFJmjt.sNwLPrv9Zsk3vNprFpqEwt8RKSs-JjTv-fd6n0')

# response = requests.get(query)
# bugreports = {}

# class BugReportStatus(Enum):
#     Unconfirmed = 1
#     NeedsTriage = 2
#     NeedsMoreInfo = 3
#     ReadyForQA = 4
#     AwaitingValidation = 5
#     Closed = 6

# class ResolutionReason(Enum):
#     Fixed = 1
#     Duplicate = 2

# class BugReport:

#     def __init__(self, id : str, title : str, status : BugReportStatus, resolution : ResolutionReason = None):
#         self.id = id
#         self.title = title
#         self.status = status
#         self.resolution = resolution



# for i in response.json()['user_actions']:
#     print(i['excerpt'])
