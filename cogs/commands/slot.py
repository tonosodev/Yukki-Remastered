import asyncio
import json
import random

import discord
from discord.ext import commands

from config import slot_command_aliases


class SlotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=slot_command_aliases)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def slot(self, ctx):
        await ctx.message.delete()
        await ctx.reply('{}, временно на технических работах.'.format(ctx.message.author.mention), delete_after=10)


def setup(bot):
    bot.add_cog(SlotCog(bot))
