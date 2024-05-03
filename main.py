import requests
import discord
from discord.ext import commands
from enum import Enum

botintents = discord.Intents.default()
botintents.message_content = True
bot = commands.Bot(command_prefix='-',intents=botintents)
query = 'https://forums.unrealengine.com/user_actions.json?offset=0&username=bug-reporter&filter=4,5'
url = 'https://forums.unrealengine.com/'

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



def actions_query(user, filter, page):
    return f'{url}user_actions.json?offset={page * 30}&username={user}&filter={filter}'

def request_actions(user, filters, page):
    url = f'{url}user_actions.json'
    headers = {'offset' : page * 30, 'username' : user, 'filter' : filters}
    response = requests.get(url, headers=headers)
    print(response.url)
    return response

def profile_query(user):
    return f'{url}u/{user}.json'

def profile_summary_url(user):
    return f'{url}u/{user}/Summary'

def summary_query(user):
    return f'{url}u/{user}/summary.json'


action_types = {
    'l' : 1,
    'p' : 4,
    'r' : 5
    }

# @bot.command()
# async def remind(ctx):


# Use a list of keys and values instead of this garbage
# Message desc = key: 
def make_summary_message(summarydict):
    try:
        result = str()
        result += 'Post Count :mailbox:: ' + str(summarydict['post_count']) + '\n'
        result += 'Likes Given :heart:: ' + str(summarydict['likes_given']) + '\n'
        result += 'Likes Received :blue_heart:: ' + str(summarydict['likes_received']) + '\n'
        result += 'Days Visited :calendar:: ' + str(summarydict['days_visited']) + '\n'
        return result
    except KeyError as e:
        return f"Error: Missing key {e}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


@bot.command()
async def activity(ctx, user = None, filters = 'p'):
    print(help(ctx))
    if user != None:
        filter = str()
        for c in filters:
            action_type = action_types.get(c)
            if action_type != None:
                filter += str(action_type) + ','
        filter = filter[0:len(filter) - 1]
        response = requests.get(actions_query(user, filter, 0))
        if response.ok:
            try:
                useraction = response.json()['user_actions'][0]
                await ctx.send(useraction['title'])
            except:
                await ctx.send(f'Did not find any {filters} actions for user: {user}')
                return None

@bot.command()
async def profile(ctx, user = None):
    if user != None:
        profileresponse = requests.get(profile_query(user))
        summaryresponse = requests.get(summary_query(user))
        if profileresponse.ok and summaryresponse.ok:
            try:
                summaryjson = summaryresponse.json()
                summarymap = summaryjson['user_summary']
                summarymessage = make_summary_message(summarymap)
                embedVar = discord.Embed(title=user, type='rich', url=profile_summary_url(user), description=summarymessage)
                embedVar.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.send(embed=embedVar)
            except:
                return
        else:
            await ctx.send(f'Unable to retrieve profile "{user}" due to Status Code: {profileresponse.status_code}')
    else:
        await ctx.send('Supply user param.')


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
