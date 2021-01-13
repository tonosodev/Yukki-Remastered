import io

import aiohttp
import discord
from discord.ext import commands

from config import commands_permission, yt_comment_aliases


class YtCommentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=yt_comment_aliases)
    @commands.has_any_role(*commands_permission['yt_comment_command_permission'])
    async def youtube_comment(self, ctx, *, comment):
        if not ctx.message.attachments:
            await ctx.send("Вы не отправили аватар комментатора!")
        else:
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                            f"https://some-random-api.ml/canvas/youtube-comment?avatar={url}&comment={comment}&username={ctx.author.name}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file=discord.File(data, "comment.png"))


def setup(bot):
    bot.add_cog(YtCommentCog(bot))
