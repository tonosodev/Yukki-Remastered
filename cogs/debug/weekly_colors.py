"""
Today is 3/9/2021
Session by: https://github.com/DevilDesigner
Create Time: 6:12 PM
This Class: weekly_rolors
"""

import discord
from discord.ext import commands

from config import commands_permission


class WeeklyColorsEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(WeeklyColorsEmbed(bot))
