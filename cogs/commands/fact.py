import random

import discord
from discord.ext import commands

import json
import requests
from requests.exceptions import Timeout

from config import fact_command_aliases, commands_permission, bot_initialize


class FactCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_from(self, url):
        headers = {'X-Requested-With': 'XMLHttpRequest',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
        try:
            req = requests.get(url, headers=headers, timeout=8)
        except Timeout:
            self.req_error = 'Превышено время ожидания :cold_face:'
            return False
        else:
            return json.loads(req.text)

    @commands.command(aliases=fact_command_aliases)
    @commands.has_any_role(*commands_permission['fact_command_permission'])
    async def fact(self, ctx):
        req = self.get_from('https://randstuff.ru/fact/generate/')
        yukki_comment = ("Факт.",
                         "Поразительно!",
                         "Что об этом думает чат?...",
                         "Занимательно...",
                         "Забавно)", "Будем знать.", "{}, имей ввиду!".format(ctx.message.author.mention),
                         "Хм... А {} это знал?...".format(ctx.message.author.mention), "И подумать об этом не могла...",
                         "Знала.", "Это ведь очевидно!", "Банальщина...")
        try:
            fact_embed = discord.Embed(title=f"{req['fact']['text']}",
                                       color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                    random.randint(1, 255)))
            fact_embed.set_author(name=f"Случайный факт 💭", icon_url=ctx.author.avatar_url)
            fact_embed.add_field(name="ᅠ", value=f"{self.bot.user.mention}:\n"
                                                 f"- {random.choice(yukki_comment)}")
            fact_embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                  icon_url=self.bot.user.avatar_url)

            await ctx.reply(embed=fact_embed)
        except:
            if not req:
                error_embed = discord.Embed(title=f"Ошибка соединения с API:\n\n{self.bot.req_error}")
                await ctx.reply(embed=error_embed)


def setup(bot):
    bot.add_cog(FactCog(bot))
