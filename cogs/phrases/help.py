import discord
from Cybernator import Paginator
from discord.ext import commands

from config import help_command_aliases, commands_permission


class HelpCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=help_command_aliases)
    @commands.has_any_role(*commands_permission['help_command_permission'])
    async def help(self, ctx):
        embed1 = discord.Embed(title=f"Приветствуем Вас в {ctx.guild.name}",
                               color=0x6A5ACD,
                               description=f'{ctx.guild.name} - это жилище для людей с чувством юмора и хорошим настроением.'
                                           f'\n')
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        embed1.add_field(name='__**Информация**__:', value=f'value', inline=False)
        embed1.add_field(name='__**Команды**__:', value='см. раздел II', inline=False)
        embed1.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                          icon_url=self.bot.user.avatar_url)

        embed2 = discord.Embed(title=f"Команды сервера {ctx.guild.name}",
                               description=f'Список основных команд сервера {ctx.guild.name}, доступных большинству пользователей.')
        embed2.add_field(name='__**header**__', value='value')
        embed2.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                          icon_url=self.bot.user.avatar_url)

        embed3 = discord.Embed(title=f"Техническая поддержка {ctx.guild.name}", description='Потом напишу...')

        embed3.add_field(name='__**header**__', value='value')
        embed3.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                          icon_url=self.bot.user.avatar_url)

        embeds = [embed1, embed2, embed3]
        message = await ctx.reply(embed=embed1)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                         footer_icon=self.bot.user.avatar_url, timeout=30, use_exit=False, delete_message=True,
                         color=0x6A5ACD, use_remove_reaction=True)
        await page.start()


def setup(bot):
    bot.add_cog(HelpCommandCog(bot))
