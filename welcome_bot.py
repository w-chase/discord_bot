#### A Welcome Bot for Discord Servers ####

## Imports ##
import discord
import asyncio
import config
#------------#
## Versions: ##

# Python Version ==  Python 3.6.5  (64bit)
# discord.py version == 0.16.12 


# Working Code #

#Token NTYzNTQ5OTgzOTEyMDk5ODQx.XKgZCw.x7n-_t9V4iWCtJLEiC1R_bPO2Nc
#Client 563549983912099841


TOKEN = config.Token

client = discord.Client()

@client.event
async def on_message(message):
    ### We do not want the bot to reply to itself
    if message.author == client.user:
        return
    ###

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!goodnight'):
        msg = 'Have a good Rest!! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('!welcome'):
        msg = '''Welcome to House Aratus {0.author.mention}.\n
            Please make your self comfortable.'''.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!rules'):
        msg = '''~~~HARAT Discord Server Rules~~~ \n
            1. Don't be a dipshit. \n
            2. Keep the NSFW (Not Safe For Work) in the NSFW Channel. \n
            3. Respect others. \n
            If you become an issue then the issue will be removed.'''
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!help'):
        msg = '''  ~*~*~*~ Welcome Bot ~*~*~*~ \n Public Area command list: \n !hello \n !goodnight \n !welcome \n !rules'''
        await client.send_message(message.channel, msg)



    ### Below this are Opsec Messages only to be called in the discord channel "members"  ###



    elif message.content.startswith('?help'):
        msg = '''  ~~~~ Welcome Bot~~~~ \n Members Area command list: \n !hello <> !goodnight \n !welcome <> !rules \n ?info <> ?policy \n ?newgoon '''
        await client.send_message(discord.Object(id='328624738077507584'), msg)

    elif message.content.startswith('?policy'):
        msg = "Please review the Corporation guidelines listed here: http://bit.ly/haratpolicy "
        
        await client.send_message(discord.Object(id='328624738077507584'), msg)

    elif message.content.startswith('?info'):
        msg = '''A list of useful links:\n
            https://goonfleet.com/  ---> Link to Goonswarm Forums\n
            https://www.housearatus.space/home ---> Link to Corporation Website\n
            https://zkillboard.com/corporation/1817710684/ ---> Corporate zKillboard\n
            http://evemaps.dotlan.net/ ---> DOTLAN --- An EVE Online Atlas\n'''
        message.channel = 328624738077507584
        await client.send_message(discord.Object(id='328624738077507584'), msg)
        
    elif message.content.startswith('?newgoon'):
        msg = "If you are new to Goonswarm or just need a refresher please visit this webpage:\n https://esi.goonfleet.com"
        await client.send_message(discord.Object(id='328624738077507584'), msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')




client.run(config.Token)
