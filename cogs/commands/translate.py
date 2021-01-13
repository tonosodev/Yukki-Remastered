import random
from datetime import datetime

import discord
import googletrans
from googletrans import Translator
from discord.ext import commands

from config import commands_permission, translate_command_aliases, bot_initialize


class GoogleTranslateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=translate_command_aliases)
    @commands.has_any_role(*commands_permission['translate_command_permission'])
    async def translate(self, ctx, dest, *, txt: str):
        try:
            result = Translator.translate(text=txt, dest=dest)

            embed = discord.Embed(title=f'**Перевод твоего сообщения**',
                                  description=f"**Твое сообщение:** - {result.origin}\n\n"
                                              f"**Перевод:** - {result.text}\n\n",
                                  timestamp=datetime.utcnow(),
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(
                url='https://upload.wikimedia.org/wikipedia/commons/1/14/Google_Translate_logo_%28old%29.png')

            await ctx.send(embed=embed)

        except ValueError:
            embed = discord.Embed(
                description=f':x: {ctx.author.mention}, данного **языка** не существует, я отправлю список **языков** тебе в **лс** :x:',
                timestamp=datetime.utcnow(), color=0xff0000)

            embed.set_author(icon_url='https://www.flaticon.com/premium-icon/icons/svg/1828/1828665.svg',
                             name='Бот | Ошибка')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)

            await ctx.send(embed=embed)

            languages = ", ".join(googletrans.LANGUAGES)

            embed = discord.Embed(description=f'**Список всех языков:** {languages}', timestamp=datetime.utcnow(),
                                  color=0x00FF00)

            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.channel.purge(limit=1)
            await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(GoogleTranslateCog(bot))
