import discord
from Cybernator import Paginator
from discord.ext import commands

from config import help_command_aliases, commands_permission
from managers_data import MetaPeace_supports_id, MetaPeace_supports_url_name, MetaPeace_supports_url, \
    MetaPeace_head_tech_spec_url_name, MetaPeace_head_tech_spec_id, MetaPeace_head_tech_spec_url, MetaPeace_owner_url


class HelpCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=help_command_aliases)
    @commands.has_any_role(*commands_permission['help_command_permission'])
    @commands.cooldown(1, 80, commands.BucketType.user)
    async def help(self, ctx):
        await ctx.message.delete()
        embed1 = discord.Embed(title=f"Приветствуем Вас в {ctx.guild.name}",
                               color=0x6A5ACD,
                               description=f'{ctx.guild.name} - жилище для людей с чувством юмора и хорошим настроением.'
                                           f'\nСпасибо, что Вы с нами!')
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        embed1.add_field(name='📡 __**Информация**__:',
                         value=f'Важную к ознакомлению информацию всегда можно найти в следующих каналах:'
                               f'\n**Локальная информация**:'
                               f'\n{self.bot.get_channel(766217771151261697).mention}' 
                               f'\n{self.bot.get_channel(766213910595633155).mention}'
                               f'\n{self.bot.get_channel(766217874422759434).mention}'
                               f'\n**Серверные оповещения**:'
                               f'\n{self.bot.get_channel(767819023178006569).mention}'
                               f'\n{self.bot.get_channel(766218369279852554).mention}'
                               f'\n**Советуемое к просмотру**:'
                               f'\n{self.bot.get_channel(768556053682978816).mention}'
                               f'\n{self.bot.get_channel(767917902791311370).mention}'
                               f'\n**Спонсоры**:'
                               f'\n{self.bot.get_channel(766217471514247169).mention}',
                         inline=False)
        embed1.add_field(name='💠 __**Команды**__:',
                         value='см. раздел II', inline=False)
        embed1.add_field(name='👥 __**Поддержка пользователей**__:',
                         value='см. раздел III', inline=False)
        embed1.add_field(name='__**Совет**__:',
                         value='Для перемещения по разделам используйте эмодзи под этим сообщением!', inline=False)
        embed1.add_field(name=f'Информацию запросил:',
                         value=f'{ctx.author.mention}', inline=False)

        # EMBED 2

        embed2 = discord.Embed(title=f"💠 Команды сервера {ctx.guild.name}",
                               description=f'Список основных команд сервера {ctx.guild.name}, доступных пользователям.')
        embed2.add_field(name='__**AVATAR**__',
                         value='Использование: Юкки, аватар @пользователь\nВыводит аватар пользователя в текущий чат.',
                         inline=False)
        embed2.add_field(name='__**COVID**__',
                         value='Использование: Юкки, ковид "country"\nВыводит статистику коронавируса в указанной стране.',
                         inline=False)
        embed2.add_field(name='__**LINK-CUTTER**__',
                         value='Использование: Юкки, сократи "https://source"\nСокращает ссылку на указанный ресурс.',
                         inline=False)

        # EMBED 3

        embed3 = discord.Embed(title=f"👥 Поддержка пользователей {ctx.guild.name}",
                               description='Контактные данные для связи с командой пользовательской поддержки сервера')

        embed3.add_field(name='__**Разработчик**__:',
                         value=f'ᅠ\n`DISCORD`: {ctx.guild.owner.mention}\n'
                               f'`VKONTAKTE`: [[**кликните**]]({MetaPeace_owner_url["vk"]})\n'
                               f'`GITHUB`: [[**кликните**]]({MetaPeace_owner_url["github"]}])',
                         inline=False)
        embed3.add_field(name='__**Техническая поддержка**__:',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_head_tech_spec_id["1"]}\n'
                               f'`{MetaPeace_head_tech_spec_url_name["1:url_name_1"]}`: [[**кликните**]]({MetaPeace_head_tech_spec_url["1:url_1"]})\n'
                               f'`{MetaPeace_head_tech_spec_url_name["1:url_name_2"]}`: [[**кликните**]]({MetaPeace_head_tech_spec_url["1:url_2"]})\n',
                         inline=True)
        embed3.add_field(name='ᅠ',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_head_tech_spec_id["2"]}\n'
                               f'`{MetaPeace_head_tech_spec_url_name["2:url_name_1"]}`: [[**кликните**]]({MetaPeace_head_tech_spec_url["2:url_1"]})\n'
                               f'`{MetaPeace_head_tech_spec_url_name["2:url_name_2"]}`: [[**кликните**]]({MetaPeace_head_tech_spec_url["2:url_2"]})\n',
                         inline=True)
        embed3.add_field(name='ᅠ',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_head_tech_spec_id["3"]}\n'
                               f'`{MetaPeace_head_tech_spec_url_name["3:url_name_1"]}`: [[**кликните**]]({MetaPeace_head_tech_spec_url["3:url_1"]})\n'
                               f'`{MetaPeace_head_tech_spec_url_name["3:url_name_2"]}`: [[**кликните**]]({MetaPeace_head_tech_spec_url["3:url_2"]})\n',
                         inline=True)
        embed3.add_field(name='__**Поддержка пользователей**__:',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_supports_id["1"]}\n'
                               f'`{MetaPeace_supports_url_name["1:url_name_1"]}`: [[**кликните**]]({MetaPeace_supports_url["1:url_1"]})\n'
                               f'`{MetaPeace_supports_url_name["1:url_name_2"]}`: [[**кликните**]]({MetaPeace_supports_url["1:url_2"]})\n',
                         inline=True)
        embed3.add_field(name='ᅠ',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_supports_id["2"]}\n'
                               f'`{MetaPeace_supports_url_name["2:url_name_1"]}`: [[**кликните**]]({MetaPeace_supports_url["2:url_1"]})\n'
                               f'`{MetaPeace_supports_url_name["2:url_name_2"]}`: [[**кликните**]]({MetaPeace_supports_url["2:url_2"]})\n',
                         inline=True)
        embed3.add_field(name='ᅠ',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_supports_id["3"]}\n'
                               f'`{MetaPeace_supports_url_name["3:url_name_1"]}`: [[**кликните**]]({MetaPeace_supports_url["3:url_1"]})\n'
                               f'`{MetaPeace_supports_url_name["3:url_name_2"]}`: [[**кликните**]]({MetaPeace_supports_url["3:url_2"]})\n',
                         inline=True)
        embeds = [embed1, embed2, embed3]
        message = await ctx.send(embed=embed1)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                         footer_icon=self.bot.user.avatar_url, timeout=60, use_exit=False, delete_message=True,
                         color=0x6A5ACD, use_remove_reaction=True)
        await page.start()


def setup(bot):
    bot.add_cog(HelpCommandCog(bot))
