"""
Today is 3/11/2021
Session by: https://github.com/DevilDesigner
Create Time: 3:30 AM
This Class: roles_reactions
"""

from discord.ext import commands


class RolesReactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(RolesReactions(bot))
