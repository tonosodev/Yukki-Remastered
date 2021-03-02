import discord
import requests
from discord.ext import commands

from config import commands_permission, hug_command_aliases, bot_initialize


class HugCommentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=hug_command_aliases)
    @commands.has_any_role(*commands_permission['hug_command_permission'])
    async def hug(self, ctx, user: discord.Member):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f'{ctx.message.author.mention} обнимает {user.mention} 💜')
        embed.set_image(url=res['url'])
        embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                         icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HugCommentCog(bot))
