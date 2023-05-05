# Star Sniper
# Version 1.0.0
# ONLY DOWNLOAD FROM https://github.com/up2rival/star-sniper/

import requests
import json
import os
import re
import discord
from discord.ext import commands
from colorama import Fore

os.system("cls & title Star Sniper - Initializing")
os.system("mode con: cols=70 lines=22")

version = "1.0.0"

print(f'''
{Fore.YELLOW}            .           {Fore.WHITE}.dP"Y8 888888    db    88""Yb
{Fore.YELLOW}           ,O,          {Fore.WHITE}`Ybo."   88     dPYb   88__dP
{Fore.YELLOW}          ,OOO,         {Fore.WHITE}o.`Y8b   88    dP__Yb  88"Yb
{Fore.YELLOW}    'oooooOOOOOooooo'   {Fore.WHITE}8bodP'   88   dP""""Yb 88  Yb
{Fore.YELLOW}      `OOOOOOOOOOO`
{Fore.YELLOW}        `OOOOOOO`       {Fore.WHITE}.dP"Y8 88b 88 88 88""Yb 888888 88""Yb
{Fore.YELLOW}        OOOO'OOOO       {Fore.WHITE}`Ybo." 88Yb88 88 88__dP 88__   88__dP
{Fore.YELLOW}       OOO'   'OOO      {Fore.WHITE}o.`Y8b 88 Y88 88 88"""  88""   88"Yb
{Fore.YELLOW}      O'         'O     {Fore.WHITE}8bodP' 88  Y8 88 88     888888 88  Yb

{Fore.YELLOW}    Version: {Fore.WHITE}1.0.0
{Fore.YELLOW}    Author: {Fore.WHITE}+_+#0908

''')

data=requests.get("https://raw.githubusercontent.com/up2rival/star-sniper/main/meta.json").json()
os.system("title Star Sniper - " + data["credits"] + " - " + data["version"])
if data["version"] != version:
    print(f"{Fore.WHITE}[{Fore.YELLOW}STAR{Fore.WHITE}-{Fore.YELLOW}SNIPER{Fore.WHITE}] {Fore.YELLOW}- {Fore.WHITE}UPDATE REQUIRED {Fore.YELLOW}" + data["version"])
    os.system("pause >null") 
    exit()
try: 
    token = json.load(open("config.json", "r"))["token"]
    channel = json.load(open("config.json", "r"))["channel"]
except: 
    print(f"{Fore.WHITE}[{Fore.YELLOW}STAR{Fore.WHITE}-{Fore.YELLOW}SNIPER{Fore.WHITE}] {Fore.YELLOW}- {Fore.WHITE}ERROR CODE {Fore.YELLOW}1")
    os.system("pause >null") 
    exit()

if requests.get("https://discord.com/api/users/@me", headers={"Authorization": token}).status_code != 200:
    print(f"{Fore.WHITE}[{Fore.YELLOW}STAR{Fore.WHITE}-{Fore.YELLOW}SNIPER{Fore.WHITE}] {Fore.YELLOW}- {Fore.WHITE}ERROR CODE {Fore.YELLOW}2")
    os.system("pause >null") 
    exit()

if requests.get(f"https://discord.com/api/channels/{channel}/messages", headers={"Authorization": token}).status_code != 200:
    print(f"{Fore.WHITE}[{Fore.YELLOW}STAR{Fore.WHITE}-{Fore.YELLOW}SNIPER{Fore.WHITE}] {Fore.YELLOW}- {Fore.WHITE}ERROR CODE {Fore.YELLOW}3")
    os.system("pause >null") 
    exit()

starsniper = commands.Bot(
    command_prefix="Star-Sniper$",
    activity=discord.Streaming(name="Star Sniper", url="https://twitch.tv/starsniper"),
    self_bot=True
)

@starsniper.event
async def on_ready():
    print(f"{Fore.WHITE}[{Fore.YELLOW}STAR{Fore.WHITE}-{Fore.YELLOW}SNIPER{Fore.WHITE}] {Fore.YELLOW}- {Fore.WHITE}SNIPING IN {Fore.YELLOW}{channel}")

@starsniper.event
async def on_message(message):
    if message.channel.id == channel:
        print(message.content)
        if "https://www.roblox.com/games/2788229376?privateServerLinkCode=" in message.content:
            os.system('start "" ' + re.search("(?P<url>https?://[^\s]+)", message.content).group("url"))
            print(f"{Fore.WHITE}[{Fore.YELLOW}STAR{Fore.WHITE}-{Fore.YELLOW}SNIPER{Fore.WHITE}] {Fore.YELLOW}- {Fore.WHITE}SNIPED LINK IN {Fore.YELLOW}{message.id}")

starsniper.run(token, log_handler=None)
