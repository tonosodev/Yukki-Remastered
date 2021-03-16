import random
from asyncio.log import logger

import discord
import pyshorteners
from discord.ext import commands

from config import link_cutter_command_aliases, commands_permission, bot_initialize


class LinkCutterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog LinkCutter loaded!")

    @commands.command(aliases=link_cutter_command_aliases)
    @commands.has_any_role(*commands_permission['link_cutter_command_permission'])
    async def link_cut(self, ctx, url: str = None):
        member = ctx.author.mention
        if url is None:
            await ctx.message.delete()
            embed = discord.Embed(title="✄ Link-cutter",
                                  color=discord.Color.red())
            embed.add_field(name="Ошибка обработки ссылки",
                            value="{}, обязательно укажите ссылку, которую хотите сократить!".format(member))
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=10)
        else:
            await ctx.message.delete()
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            embed = discord.Embed(title="✄ Link-cutter",
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)),
                                  timestamp=ctx.message.created_at)
            embed.add_field(name="Ссылка сокращена: ",
                            value="Обработана для {}".format(member) + "\nСсылка: " + short_url)
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=20)


def setup(bot):
    bot.add_cog(LinkCutterCog(bot))
