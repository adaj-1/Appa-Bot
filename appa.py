# bot.py
import os
import discord
import random
import datetime
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("GUILD_ID")

bot = commands.Bot(command_prefix="!")


@bot.command(name="fku", help="Tell Appa to go fuck himself")
async def fku(ctx):
    await ctx.send("fuck you too!")


@bot.command(name="hort", help="Heads or Tails")
async def HorT(ctx):
    appa_images = [discord.File("Head.png"), discord.File("Tail.png")]
    hort = random.choice(appa_images)
    await ctx.send(file=hort)


@bot.command(name="jail", help='!jail @user "Reason" "Sentence (min)"')
async def jail(ctx, jailUser: discord.Member, reason, sentence: int):
    auth_role = ctx.author.roles  # get author roles
    user_role = jailUser.roles  # get jail user roles
    jail_role = discord.utils.find(lambda r: r.name == "Jail", ctx.message.guild.roles)
    if jail_role in user_role:
        return await ctx.send("{} is already in jail".format(jailUser.mention))

    if sentence < 10:
        user = jailUser
        og_role = user_role
        sentence_min = sentence * 60
        desc = (
            "{} has been jailed\nReason: {}\nSentenced to serve: {} minute(s)".format(
                user.mention, reason, sentence
            )
        )
    else:
        user = ctx.author
        og_role = auth_role
        sentence_min = sentence * 120
        desc = "Reason: ABUSE OF POWER!!\n Sentenced to serve: {} minute(s)".format(
            sentence * 2
        )

    await user.edit(roles=[jail_role])
    msg = discord.Embed(description=desc, color=0xFF0000)
    appa_jail = discord.File("Jail.png")
    await ctx.send(embed=msg, file=appa_jail)

    await asyncio.sleep(sentence_min)
    await user.edit(roles=og_role)
    release = discord.Embed(
        description="{} has been released!".format(user.mention), color=0xFF0000
    )
    appa_release = discord.File("Release.jpg")
    await ctx.send(embed=release, file=appa_release)


bot.run(TOKEN)
