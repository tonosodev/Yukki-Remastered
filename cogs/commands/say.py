import discord
from discord.ext import commands
import io


class SayCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(766293535832932392, 766233124681547776,
                           766231587104620554)  # Head.tech-spec, #Support,  #Owner
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
