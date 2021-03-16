import discord
from discord.ext import commands

import random
import json
import requests
from loguru import logger
from requests.exceptions import Timeout

from config import commands_permission, bot_initialize, joke_command_aliases


class JokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog Jokes loaded!")

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

    @commands.command(aliases=joke_command_aliases)
    @commands.has_any_role(*commands_permission['joke_command_permission'])
    async def joke(self, ctx):
        req = self.get_from('https://randstuff.ru/joke/generate/')

        yukki_comment = (
            "<:admin_face:769707992891129897>", "Вот и думай головой.", "Такие дела...", "М-да...", "Чушь какая!",
            "Сама в шоке.", "Более глупой шутки я еще не слышала...", "Кто это вообще придумал?!",
            "А теперь дружно об этом забудем...", "Чего...", "Ну надо же!", "Гениально.", "Это - щедевр!",
            "Крайне полезная информация, да, {} ?".format(ctx.message.author.mention),
            "Что скажешь, {} ?".format(ctx.message.author.mention), "От смеха со всеми ботами по пингу просели)",
        )

        try:
            joke_embed = discord.Embed(title=f"{req['joke']['text']}",
                                       color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                    random.randint(1, 255)))
            joke_embed.set_author(name=f"Случайная шутка 💥", icon_url=ctx.author.avatar_url)
            joke_embed.add_field(name="ᅠ", value=f"{self.bot.user.mention}:\n"
                                                 f"- {random.choice(yukki_comment)}")
            joke_embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                  icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=joke_embed)
        except:
            if not req:
                error_embed = discord.Embed(title=f"Ошибка соединения с API:\n\n{self.bot.req_error}")
                await ctx.reply(embed=error_embed)


def setup(bot):
    bot.add_cog(JokeCog(bot))
