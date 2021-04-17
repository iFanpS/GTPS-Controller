# IFANPS COPYRIGHT 2021
# WANT TO RECODE OR MAKE THIS CODE BETTER DM iFanpS#0007

import discord
from discord.ext import commands
from discord import Client
import os, psutil
from datetime import datetime
    
bot = commands.Bot(command_prefix="c.")
bot.remove_command("help")

Client = discord.Client()

config = configparser.ConfigParser()
config.read("config.ini")

@bot.event
async def on_ready():
    print(f"{Client.user} is on")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

@bot.command()
async def status(ctx):
    for proc in psutil.process_iter():
        if 'enet' in proc.name():
            await ctx.send("Server is UP")
            break;
        else:
            if 'enet' not in proc.name():
                await ctx,send("Server is Down")
            
@bot.command()
async def online(ctx):
    player = open('online.txt').readlines()
    await ctx.send(f"{player[0]} Online")
    
@bot.command()
async def player(ctx):
    listplayer = len(os.listdir('players'))
    await ctx.send(f"{listplayer} Account created")
    
@bot.command()
async def start(ctx):
    os.system(r'"Yout enet Path"')
    await ctx.send("Your server is UP Now")
    
@bot.command()
async def stop(ctx):
    gabut = os.system("taskkill /f /im Your enet name.exe")
    if gabut == True:
        await ctx.send("Your server is Down")

@bot.command()
async def world(ctx):
    listworld = len(os.listdir('worlds'))
    await ctx.send(f"{listworld} Created For Now")

@bot.command()
async def givegem(ctx, args1, args2):
    while True:
        try:
            task1 = open(f'C:\\yourfolderplayer\\{args1}', 'r').read();
            oldgems = re.findall("irfan: (.+?)",str(task1))[0]

            givegems = task1.replace(oldgems, args2);

            task2 = open(f'C:\\yourfolderplayer\\{args1}.json', 'w')
            task2.write(givegems)
            task2.close()
            await ctx.send(f"Gems already added to\nPlayer: {args1}\nAmount: {args2}")
        except FileNotFoundError:
            await ctx.send("Error path to gem folder not found")
            
@bot.command()
async def givelevel(ctx, args1, args2):
    while True:
        try:
            task1 = open(f'C:\\yourfolderplayer\\{args1}.json', 'r').read();
            oldlevel = re.findall('"level":(.+?)',str(task1))[0]

            newlevel = task1.replace(oldlevel, args2);

            task2 = open(f'C:\\yourfolderplayer\\{args1}.json', 'w')
            task2.write(newlevel)
            task2.close()
            await ctx.send(f"New Level already added to\nPlayer: {args1}\nAmount: {args2}")
        except FileNotFoundError:
            await ctx.send("Error path to gem folder not found")

@bot.command()
async def giverank(ctx, args1, args2):
    while True:
        try:
            task1 = open(f'C:\\yourfolderplayer\\{args1}.json', 'r').read();
            oldlevel = re.findall('"adminLevel":(.+?)',str(task1))[0]

            newlevel = task1.replace(oldlevel, args2);

            task2 = open(f'C:\\yourfolderplayer\\{args1}.json', 'w')
            task2.write(newlevel)
            task2.close()
            await ctx.send(f"New rank added to\nPlayer: {args1}\nAmount: {args2}")
        except FileNotFoundError:
            await ctx.send("Error path to gem folder not found")    
    
@bot.command()
async def count(ctx):
    def decsize(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("KB", "MB", "GB", "TB", "PB", "ZB")
        hitungan = int(math.floor(math.log(size_bytes, 1024)))
        prediksi = math.pow(1024, hitungan)
        sindikat = round(size_bytes / prediksi,2)
        return "%s %s" % (sindikat, size_name[hitungan])
    file1 = open('players', 'rb').read()
    htng = len(file1)
    ukuran = (decsize(htng))
    file1y = len(os.listdir('players'))
    file2 = open('worlds', 'rb').read()
    htng1 = len(file2)
    ukuran2 = (decsize(htng1))
    file2y = len(os.listdir('worlds')
    await ctx.send(f'Player count: {file1y}\nPlayer folder size: {ukuran}\nWorld count: {file2y}\nWorld folder size: {ukuran2}')
    
@bot.command()
async def maintenance(ctx):
    on_off = ["on", "off"]
    await ctx.send("type on or off")
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in on_off

    user_onoff = (await bot.wait_for('message', check=check)).content
    
    if user_onoff == "on":
        file = open('server_data.php', 'r').read()
        olfmt = re.findall('(.*?)maint|Mainetrance', str(file))[0]
        chgmt = file.replace(olfmt, "");
        file2 = open('server_data.php', 'w')
        file2.write(chgmt)
        file2.close()
        await ctx.send("Your maintenance message has on")
    elif user_onoff == "off":
        file1 = open('server_data.php', 'r').read()
        chgmt1 = file1.replace("maint", "#maint");
        file3 = open('server_data.php', 'w')
        file3.write(chgmt1)
        file3.close()
        await ctx.send("Your maintenance message has off")

@bot.command(pass_context = True)
async def pdel(ctx, *, args):
    while True:
        try:
            namafile1 = f"{args}.json"
            filepath = "yourfoldeplayerpath"
            path = os.path.join(filepath, namafile1)
            os.remove(path)
            ift = os.system("taskkill /f /im Your enet name.exe")
            if ift == True:
                await ctx.send(f"Server has been restart and {namafile1} has deleted")
                break;
        except FileNotFoundError:
            await ctx.send("player not in folder")
            break;
    
@bot.command()
async def wdel(ctx, args):
    while True:
        try:
            namaworld = f"{args}.json"
            filepath = "yourfolderworldpath"
            path = os.path.join(filepath, namaworld)
            os.remove(path)
            restart = os.system("taskkill /f /im Your enet name.exe")
            if restart == True:
                await ctx.send(f"Server has been restart and {namaworld} has deleted")
        except FileNotFoundError:
            await ctx.send("player not in folder")                
                 
@bot.command()
async def help(ctx):
    time = datetime.now()
    clock = time.strftime(' %H:%M %p')
    embed = discord.Embed(color=0x00ff00, title="Help Command")
    embed.add_field(name="List", value="wdel(for delete world),\npdel(for delete player),\nmaintenance(for activate maintenance msg),\ncount(for counting folder),\nstart(for start server),\nstop(for stop server)\ngiverank(for give rank to player),\ngivelevel(same like giverank),\ngivegem(same like givelevel),\nworld(for see how many wolrd created),\nplayer(for see how many account created),\nonline(for see online people)\nstatus(see if server up or down)")
    embed.set_footer(text=f"{clock} | GTPS Controller by iFanpS :)")
    await ctx.send(embed=embed)

bot.run(config['TOKEN']['token'])
