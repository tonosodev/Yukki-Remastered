import json

import discord
import requests
from discord.ext import commands

from config import commands_permission, covid_command_aliases


class CovidCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=covid_command_aliases)
    @commands.has_any_role(*commands_permission['covid_command_permission'])
    async def covide(self, ctx, country=None):
        msg = await ctx.reply("`Пожалуйста, подождите. . .`")
        if not country:
            await ctx.reply(
                f"Введите название страны на английском языке с заглавной буквы!",
                delete_after=10)  # Ошибка Если кто-то не написал страну на англ

        else:

            for item in json.loads(requests.get("https://corona.lmao.ninja/v2/countries").text):

                if item['country'] == country:
                    embed = discord.Embed(
                        title=f'Статистика Коронавируса | {country}', color=0x8B0000)
                    embed.add_field(name=f'Выздоровело:', value=f'{item["recovered"]} человек')
                    embed.add_field(name=f'Заболеваний:', value=f'{item["cases"]} человек')
                    embed.add_field(name=f'Погибло:', value=f'{item["deaths"]} человек')
                    embed.add_field(name=f'Заболеваний за сутки:', value=f'+{item["todayCases"]} человек')
                    embed.add_field(name=f'Погибло за сутки:', value=f'+{item["todayDeaths"]} человек')
                    embed.add_field(name=f'Проведено тестов:', value=f'{item["tests"]} человек')
                    embed.add_field(name=f'Активные зараженные:', value=f'{item["active"]} человек')
                    embed.add_field(name=f'В тяжелом состоянии:', value=f'{item["critical"]}  человек')
                    embed.add_field(name='Запросил:', value=f'{ctx.author.mention}', inline=False)
                    embed.set_thumbnail(url=item["countryInfo"]['flag'])
                    embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                                     icon_url=self.bot.user.avatar_url)
                    await msg.delete()
                    await ctx.send(embed=embed, delete_after=20)
                    await ctx.message.delete()


def setup(bot):
    bot.add_cog(CovidCog(bot))
