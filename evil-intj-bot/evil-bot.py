import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

Client = discord.Client()
bot_prefix = "."
client = commands.Bot(command_prefix=bot_prefix)
INTJ_EVIL_BOT_SECRET_KEY = os.environ.get('INTJ_EVIL_BOT_SECRET_KEY')

@client.event
async def on_ready():
    print("Bot Online!")
    print('Logged in as')
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print('------')


@client.command(pass_context=True)
async def intj(ctx):
    await client.say("same")




@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    is_INTJ = False
    msg_contains_INTJ = False

    roles = message.author.roles

    for role in roles:
        if 'INTJ' == role.name:
            is_INTJ = True

    if 'intj' in message.content:
         msg_contains_INTJ = True

    if 'INTJ' in message.content:
         msg_contains_INTJ = True


    if is_INTJ and msg_contains_INTJ:
        msg = 'same'
        await client.send_message(message.channel, msg)

    await client.process_commands(message)




client.run(INTJ_EVIL_BOT_SECRET_KEY)
