#輸入Discord用的函式庫
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
import requests

with open('set.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

class fastcar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def NTUT(self, ctx, *, arg):
        url = data['NTUT']
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        inputstring = arg
        x = inputstring.split()
        await ctx.send(x)
    
        if x[0] == "id":
            html = soup.find(id = x[1]).text
            await ctx.send(len(html))
            if len(html) > 2000:
                await ctx.send("This html is too long that can't output.\n")
            else:
                await ctx.send(html)

        elif x[0] == "class":
            html = soup.find(class_ = x[1]).text
            if len(html) > 2000:
                await ctx.send("This html is too long that can't output.\n")
            else:
                await ctx.send(html)

    @commands.command()
    async def Pixiv(self, ctx, arg):
        url = "https://www.pixiv.net/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        
def setup(bot):
    bot.add_cog(fastcar(bot))
    #bot.add_command(NTUT)
    

