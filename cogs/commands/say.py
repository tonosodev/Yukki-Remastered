import discord
from discord.ext import commands
import io

from discord.ext.commands import ChannelNotFound

from config import say_command_aliases, commands_permission


class SayCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=say_command_aliases)
    @commands.has_any_role(*commands_permission['say_permission'])
    async def say(self, ctx, channel: discord.TextChannel, *, message: str):
        files = []
        await ctx.message.delete()
        try:
            for file in ctx.message.attachments:
                fp = io.BytesIO()
                await file.save(fp)
                files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
            await channel.send(message, files=files)
        except channel is not discord.TextChannel:
            for file in ctx.message.attachments:
                fp = io.BytesIO()
                await file.save(fp)
                files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
            await ctx.send(message, files=files)
        finally:
            pass


def setup(bot):
    bot.add_cog(SayCommandCog(bot))
