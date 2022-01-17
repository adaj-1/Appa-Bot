import random
import discord
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fku", help="Tell Appa to go fuck himself")
    async def fku_(self, ctx):
        await ctx.send("fuck you too!")

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command(name="hort", help="Heads or Tails")
    async def hort_(self, ctx):
        hort = self.coinflip()
        if hort == 1:
            await ctx.send(file=discord.File(".\\assets\\Head.png"))

        else:
            await ctx.send(file=discord.File(".\\assets\\Tail.png"))


def setup(bot):
    bot.add_cog(Basic(bot))
