import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv


class Jail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="jail", help='!jail @user "Reason" "Sentence (min)"')
    async def jail_(self, ctx, jailUser: discord.Member, reason, sentence: int):
        auth_role = ctx.author.roles  # get author roles
        user_role = jailUser.roles  # get jail user roles
        jail_role = discord.utils.find(
            lambda r: r.name == "Jail", ctx.message.guild.roles
        )
        if jail_role in user_role:
            return await ctx.send("{} is already in jail".format(jailUser.mention))

        if sentence < 10:
            user = jailUser
            og_role = user_role
            sentence_min = sentence * 60
            desc = "{} has been jailed\nReason: {}\nSentenced to serve: {} minute(s)".format(
                user.mention, reason, sentence
            )
        else:
            user = ctx.author
            og_role = auth_role
            sentence_min = sentence * 120
            desc = "Reason: ABUSE OF POWER!!\n Sentenced to serve: {} minute(s)".format(
                sentence * 2
            )

        await user.edit(roles=[jail_role])
        jail_msg = discord.Embed(description=desc, color=0xFF0000)
        appa_jail = discord.File(".//assets/Jail.png", filename="Jail.png")
        jail_msg.set_image(url="attachment://Jail.png")
        await ctx.send(file=appa_jail, embed=jail_msg)

        await asyncio.sleep(sentence_min)
        await user.edit(roles=og_role)
        release_msg = discord.Embed(
            description="{} has been released!".format(user.mention), color=0xFF0000
        )
        appa_release = discord.File(".//assets/Release.jpg", filename="Release.jpg")
        release_msg.set_image(url="attachment://Release.jpg")
        await ctx.send(file=appa_release, embed=release_msg)


def setup(bot):
    bot.add_cog(Jail(bot))
