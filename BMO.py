import discord
from discord.ext import commands
import youtube_dl
import os
import time
import random
import itertools
from datetime import date
import asyncio

client = commands.Bot(command_prefix = ':)')
naughtycount = 0
normal = ["https://www.youtube.com/watch?v=W_FRPoJIrlI","https://www.youtube.com/watch?v=0nf_0Thk_4Q","https://www.youtube.com/watch?v=MBmb5_TTT-w"]
reverb = ["https://www.youtube.com/watch?v=HwYwBq1ZCEQ","https://www.youtube.com/watch?v=hr7GyFM7pX4","https://www.youtube.com/watch?v=Q_9VMaX61nI"]
bassboost = ["https://www.youtube.com/watch?v=N6_NcCcNhA4","https://www.youtube.com/watch?v=LVZ9YycnNSg","https://www.youtube.com/watch?v=t_PzQ--8Cyc"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Use :)terminate to terminate the program')
    
    while True:
        await asyncio.sleep(random.randint(100,1000))
        adlibs = os.listdir("/Users/Radhesh Salgadoe/Documents/Discord Bots/BMO/adlibs")
        adlib = adlibs[random.randint(0,(len(adlibs)-1))]
        path = "adlibs/" + adlib
        print(f"PATH: {path}")
        print(f"all adlibs:{adlibs}// chosen adlib:{adlib}")
        guild = client.get_guild(747160612416520413)
        voiceChannel = discord.utils.get(guild.voice_channels, name="Finn & Jake's Treehouse")
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=guild)
        voice.play(discord.FFmpegPCMAudio(path))
            
        while voice.is_playing(): #Checks if voice is playing
            await asyncio.sleep(1) #While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(2.5) #If it's not playing it waits 15 seconds
            while voice.is_playing(): #and checks once again if the bot is not playing
                break #if it's playing it breaks
            else:
                await voice.disconnect() #if not it disconnects


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("Fart has occured")
        url = normal + reverb + bassboost
        url = url[random.randint(0,8)]
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current fart to stop.")
            return            
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Finn & Jake's Treehouse")
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        
        while voice.is_playing(): #Checks if voice is playing
            await asyncio.sleep(1) #While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(2.5) #If it's not playing it waits 15 seconds
            while voice.is_playing(): #and checks once again if the bot is not playing
                break #if it's playing it breaks
            else:
                await voice.disconnect() #if not it disconnects


@client.command()
async def fart(ctx, effect : str):
    print("Fart has occured")
    error = False
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current fart to stop.")
        return

    if effect == "normal":
        url = normal[random.randint(0,2)]
    elif effect == "reverb":
        url = reverb[random.randint(0,2)]
    elif effect == "bassboost":
        url = bassboost[random.randint(0,2)]
    else:
        error = True
        

    if error != True:
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Finn & Jake's Treehouse")
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        
        while voice.is_playing(): #Checks if voice is playing
            await asyncio.sleep(1) #While it's playing it sleeps for 1 second
        else:
            await asyncio.sleep(2.5) #If it's not playing it waits 15 seconds
            while voice.is_playing(): #and checks once again if the bot is not playing
                break #if it's playing it breaks
            else:
                await voice.disconnect() #if not it disconnects
    else:
        await ctx.send("You must enter a valid effect, eg: :)fart normal")


@client.command()
async def info(ctx):
    await ctx.send("Hello! I am BMO Bot version 1.0.0. You can say hi to me if you feel lonely. My command prefix us ' :) '. Here are just a few things that I can do as of currently in my development:':)fart [effect]' to make BMO fart. Choose an effect of either normal, reverb or bassboost.")

@client.command()
async def terminate(ctx):
    await client.logout()

@client.event   
async def on_message(message):
    await client.process_commands(message)
    global naughtycount
    swears = ("fuck","Fuck","FUCK","shit","Shit","SHIT","bitch","Bitch","BITCH","cunt","Cunt","CUNT")
    s_greetings = ("hello","hey","hi")
    greeting_choices = ('Hello {0.author.mention}!','Greetings {0.author.mention}!','Why hello there {0.author.mention}!')
    if message.author == client.user:
        return
    
    if message.content.startswith(s_greetings):
        r = random.randint(0,(len(greeting_choices)-1))
        msg =  greeting_choices[r].format(message)
        await message.channel.send(msg)
        print(naughtycount)

    for i in swears:
        if i in message.content:
            naughtycount += 1
            print(naughtycount)
            timesuntil = 10 - naughtycount
            if naughtycount < 4:
                await message.channel.send("Hello {0.author.mention}, it seems as if you have started swearing on this text channel! As this is a Christian server we would very much appreciate and expect you not to do this again.".format(message))
            elif naughtycount >= 4 and timesuntil >  1:
                await message.channel.send("It seems as if there have been a lot of curse words on this server :), please do not continue to do this.")
                await message.channel.send(f"If everyone keeps swearing {timesuntil} more times. I might have to go sicko mode.")
            elif timesuntil == 1:
                await message.channel.send("Someone swear one more goddamn time and i'll fucking overclock your pc enough to send humans to the 5th nearest galaxy cluster.")
            elif timesuntil == 0:
                url = "https://www.youtube.com/watch?v=xCNSQC5217Q"
                song_there = os.path.isfile("song.mp3")
                try:
                    if song_there:
                        os.remove("song.mp3")
                except PermissionError:
                    await message.channel.send("Wait for the current fart to stop.")
                    return

                voiceChannel = discord.utils.get(message.guild.voice_channels, name="Finn & Jake's Treehouse")
                await voiceChannel.connect()
                voice = discord.utils.get(client.voice_clients, guild=message.guild)

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                voice.play(discord.FFmpegPCMAudio("song.mp3"))
                
                while voice.is_playing(): #Checks if voice is playing
                    await asyncio.sleep(1) #While it's playing it sleeps for 1 second
                else:
                    await asyncio.sleep(2.5) #If it's not playing it waits 15 seconds
                    while voice.is_playing(): #and checks once again if the bot is not playing
                        break #if it's playing it breaks
                    else:
                        await voice.disconnect() #if not it disconnects


client.run('NzQ3MTYwNDQ5MDk4NzExMDgy.X0K1ZA.4SgQSAchBNe8M1NP9U23URdt4Vc')