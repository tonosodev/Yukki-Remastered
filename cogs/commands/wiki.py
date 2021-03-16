import random

import discord
import requests
from discord.ext import commands
from loguru import logger

from config import wiki_command_aliases, commands_permission, bot_initialize


class WikiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog Wiki loaded!")

    @commands.command(aliases=wiki_command_aliases)
    @commands.has_any_role(*commands_permission['wiki_command_permission'])
    async def wiki(self, ctx, *, query: str):
        msg = await ctx.reply("**`Пожалуйста, подождите. . .`**")
        sea = requests.get(
            ('https://ru.wikipedia.org//w/api.php?action=query'
             '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
             ).format(query)).json()['query']

        if sea['searchinfo']['totalhits'] == 0:
            await ctx.reply(f'По запросу **"{query}"** ничего не найдено :confused:')
        else:
            for x in range(len(sea['search'])):
                article = sea['search'][x]['title']
                req = requests.get('https://ru.wikipedia.org//w/api.php?action=query'
                                   '&utf8=1&redirects&format=json&prop=info|images'
                                   '&inprop=url&titles={}'.format(article)).json()['query']['pages']
                if str(list(req)[0]) != "-1":
                    break
            article = req[list(req)[0]]['title']
            arturl = req[list(req)[0]]['fullurl']
            artdesc = requests.get('https://ru.wikipedia.org/api/rest_v1/page/summary/' + article).json()['extract']
            embed = discord.Embed(title=article, url=arturl, description=artdesc,
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.set_author(name='Google | Википедия', url='https://en.wikipedia.org/',
                             icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await msg.delete()
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(WikiCog(bot))
