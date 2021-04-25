import discord
from discord.ext import commands

TOKEN = 'PUT BOT TOKEN BETWEEN THESE DASHES' # Put the token of the bot you are using here
GUILD =   # Put the ID of the discord server the bot is using here

bot = commands.Bot(command_prefix='!')  # Thing in '' can be changed to configure what prefix bot uses
bot_actions =   # Put a channel you want all actions the bot takes to be sent to whenever someone does an action

# ref1 =  # put your discord user ID here to be given special bot privileges; also does nothing rn

# refs = [ref1] # more refs can be added too! Doesn't do anything rn

passwords = {'password1': <id here>,  # put the roleids here, without the <>
             'password2': <id here>}

print("Starting bot")

@bot.event
async def on_ready():
    print("on_ready just happened!")
    activity = discord.Activity(name='you.', type=discord.ActivityType.watching) # feel free to play with stuff here
    await bot.change_presence(activity=activity)
    channel_ba = bot.get_channel(bot_actions)
    await channel_ba.send("Hazel Bot is now live!")


@bot.command(name='unlock', help='Allows access to secret channels and roles.')
async def unlock(ctx, password):
    user = ctx.author  # This is who sent the message. ctx allows it to be any channel
    channel_ba = bot.get_channel(bot_actions)  # Defines the channel you want the bot to send stuff to tell refs
    print(password)
    # when stuff happens
    if password in passwords:
        rolename = passwords[password]
        guild = bot.get_guild(GUILD)
        role = guild.get_role(rolename)
        await user.add_roles(role)
        message = str(user) + " was given the role " + str(role)
        await channel_ba.send(message)
    else:
        await ctx.send("That is not a valid password! :(")
        message = str(user) + " incorrectly guessed a password! They wrote: " + str(password)
        await channel_ba.send(message)
        return



bot.run(TOKEN)