anyerror = False
try:
    import requests
    import colorama
    import discord
    from discord.ext import commands
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install discord")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()

import json
colorama.init(autoreset=True)
try:
    from os import system
    system("title " + "Discord Mass Message Saver Selfbot,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass

token = "OTgxMjA2NTU5MzU3MDE0MDI2.GPkr3P.mr3CjL4PCFxZ5uSVa9n3yMzpiKvbDg0-SmrMvM"



try:
    error = False
    json_data = open("settings.json")
    json_data = json.load(json_data)
    tokens = str(json_data["token"])
    prefix = json_data["prefix"]
    send_message_when_done_y_or_n = json_data["send_message_when_done_y_or_n"]
    if send_message_when_done_y_or_n != "n" and send_message_when_done_y_or_n != "y":
        print(colorama.Fore.RED + "On send_message_when_done_y_or_n Please Enter A Valid Choice")
        error = True
    invite_code = "weYYXeUSNm"

    r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
    if "200" not in str(r1):
        print(colorama.Fore.RED + "Invalid Token!")
        error = True
    if "200" in str(r1):
        r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
        if "200" in str(r):
            pass
        if "403" in str(r):
            print(colorama.Fore.YELLOW + "Locked Token!")
            error = True
    if error == True:
        input("")
except:
    print(colorama.Fore.RED + "Missing settings.json, It Stores All Data")
    input("")
token = tokens







bot = commands.Bot(command_prefix=str(prefix), self_bot=True)


@bot.event
async def on_ready():
    print("Selfbot Is Up! Type "+str(prefix)+"save To Save The Last 100 Messages")





@bot.command()
async def save(ctx):
    id2 = str(ctx.channel.id)
    url = f"https://discord.com/api/v9/channels/{id2}/messages?limit=100"
    headers = {
        "authorization": token
    }
    re = requests.get(url=url, headers=headers)
    done = 0
    for jes in re.json():
        name = str(jes["author"]["username"])
        id = str(jes["author"]["id"])
        content = str(jes["content"])
        done = int(done) + 1
        print(colorama.Fore.GREEN + f"[{str(done)}] Saved Message")
        file = open(f"{id2}_save.txt", "a")
        file.write(f"Sender Name: {name}\nSender Id: {id}\nMessgae Content: {content}\n\n")
    file.close()
    if send_message_when_done_y_or_n == "y":
        await ctx.send("Selfbot - Saved The Last 100 Messages In This Conversation!")
    print(colorama.Fore.GREEN + "Saved The Last 100 Messages In This Conversation!")



bot.run(token, bot=False)