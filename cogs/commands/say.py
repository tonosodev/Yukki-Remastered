import discord
from discord.ext import commands
import io

from config import say_command_aliases, commands_permission


class SayCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=say_command_aliases)
    @commands.has_any_role(*commands_permission['say_permission'])
    async def say(self, ctx, *, message=None):
        files = []
        for file in ctx.message.attachments:
            fp = io.BytesIO()
            await file.save(fp)
            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

        await ctx.channel.purge(limit=1)
        await ctx.send(message, files=files)


def setup(bot):
    bot.add_cog(SayCommandCog(bot))
