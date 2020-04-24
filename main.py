#輸入Discord用的函式庫
import discord
from discord.ext import commands
import os
import json

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

bot = commands.Bot(command_prefix='!')

#當bot成功上線時輸出成功訊息
@bot.event
async def on_ready():
    print("Bot works successfully!")

#當新成員加入伺服器時輸出訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(data['IN_SERVER & OUT_SERVER'])
    await channel.send(f'{member} join the server OwO!')
    #print("f'{member}' join in the server!")

#當新成員離開伺服器時輸出訊息
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(data['IN_SERVER & OUT_SERVER'])
    await channel.send(f'{member} leave the server Q^Q!')
    #print(f'{member} leave the server Q^Q!')

#讓bot在Discord伺服器上啟動(需要密鑰)
#if os.environ.get('DISCORD_TOKEN'):
#    bot.run(os.environ.get('DISCORD_TOKEN'))
bot.run(data['DISCORD_TOKEN'])
#bot.run('NzAzMDc0ODg3NjQ3ODg3NDYx.XqJf-g.CI8Ejj6lzfnGLDcEcMWWEqeh2ZA')