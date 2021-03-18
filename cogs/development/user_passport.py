"""
Today is 3/18/2021
Session by: https://github.com/DevilDesigner
Create Time: 10:57 AM
This Class: user_pasport
"""

import discord
from discord.ext import commands
from loguru import logger


class UserPassportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog UserPassport loaded!")

    @commands.command(aliases=[''])
    async def passport(self, ctx):
        await ctx.send(f"{ctx.message.author.menttion}")


def setup(bot):
    bot.add_cog(UserPassportCog(bot))
