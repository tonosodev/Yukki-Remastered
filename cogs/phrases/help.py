import discord
from Cybernator import Paginator
from discord.ext import commands

from config import help_command_aliases, commands_permission, MetaPeace_head_tech_spec_id, MetaPeace_supports_id, \
    MetaPeace_owner_url, MetaPeace_head_tech_spec_url_name


class HelpCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=help_command_aliases)
    @commands.has_any_role(*commands_permission['help_command_permission'])
    @commands.cooldown(1, 30, commands.BucketType.user)
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
                               f'\n{self.bot.get_channel(766217874422759434).mention}'
                               f'\n{self.bot.get_channel(768556053682978816).mention}'
                               f'\n**Серверные оповещения**:'
                               f'\n{self.bot.get_channel(766213910595633155).mention}'
                               f'\n{self.bot.get_channel(766213910595633156).mention}'
                               f'\n**Советуемое к просмотру**:'
                               f'\n{self.bot.get_channel(774065006186463283).mention}'
                               f'\n**Спонсоры**:'
                               f'\n{self.bot.get_channel(766217471514247169).mention}',
                         inline=False)
        embed1.add_field(name='💠 __**Команды**__:', value='см. раздел II', inline=False)
        embed1.add_field(name='👥 __**Поддержка пользователей**__:', value='см. раздел III', inline=False)
        embed1.add_field(name='__**Совет**__:', value='Для перемещения по разделам кликайте на эмодзи под этим меню',
                         inline=False)
        embed1.add_field(name=f'Информацию запросил:', value=f'{ctx.author.mention}', inline=False)

        # EMBED 2

        embed2 = discord.Embed(title=f"💠 Команды сервера {ctx.guild.name}",
                               description=f'Список основных команд сервера {ctx.guild.name}, доступных пользователям.')
        embed2.add_field(name='__**header**__', value='value')

        # EMBED 3

        embed3 = discord.Embed(title=f"👥 Поддержка пользователей {ctx.guild.name}",
                               description='Контактные данные для связи с командой пользовательской поддержки сервера')

        embed3.add_field(name='__**Разработчик**__:',
                         value=f'ᅠ\n`DISCORD`: {ctx.guild.owner.mention}\n`VKONTAKTE`: [[**кликните**]]({MetaPeace_owner_url["vk"]})\n`GITHUB`: [[**кликните**]]({MetaPeace_owner_url["github"]}])',
                         inline=False)
        embed3.add_field(name='__**Техническая поддержка**__:',
                         value=f'ᅠ\n`DISCORD`: {MetaPeace_head_tech_spec_id["1"]}\n`{MetaPeace_head_tech_spec_url_name["1:any"]}`: [[**кликните**]](https://)',
                         inline=True)
        embed3.add_field(name='ᅠ', value=f'ᅠ\n`DISCORD`: {MetaPeace_head_tech_spec_id["1"]}\n`VKONTAKTE`: [[**кликните**]](https://)',
                         inline=True)
        embed3.add_field(name='__**Поддержка пользователей**__:', value=f'ᅠ\n`DISCORD`: {MetaPeace_supports_id["1"]}',
                         inline=False)

        embeds = [embed1, embed2, embed3]
        message = await ctx.send(embed=embed1)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                         footer_icon=self.bot.user.avatar_url, timeout=60, use_exit=False, delete_message=True,
                         color=0x6A5ACD, use_remove_reaction=True)
        await page.start()


def setup(bot):
    bot.add_cog(HelpCommandCog(bot))
