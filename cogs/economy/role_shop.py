import discord
from discord.ext import commands
import pymongo


class RoleShopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(RoleShopCog(bot))
