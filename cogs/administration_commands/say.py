import discord
from discord.ext import commands
from io import BytesIO

from config import say_command_aliases, commands_permission


class SayCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=say_command_aliases)
    @commands.has_any_role(*commands_permission['say_permission'])
    async def say(self, ctx, channel: discord.TextChannel = None, *, message: str):
        files = []
        load_variable = await ctx.reply(f"{ctx.author.mention}, пожалуйста, подождите. . .")
        for file in ctx.message.attachments:
            fp = BytesIO()
            await file.save(fp)
            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
        await channel.send(message, files=files)
        await load_variable.delete()

        await ctx.message.delete()


def setup(bot):
    bot.add_cog(SayCommandCog(bot))
