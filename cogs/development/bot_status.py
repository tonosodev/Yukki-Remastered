import discord
import datetime
import psutil
from Cybernator import Paginator
from discord.ext import commands
from psutil._common import bytes2human

from config import bot_status_aliases, commands_permission, bot_initialize


class DevOpStatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=bot_status_aliases)
    @commands.has_any_role(*commands_permission['bot_status_permission'])
    async def status(self, ctx):
        msg = await ctx.reply("`Пожалуйста, подождите. . .`")
        members_count = 0
        guild_count = len(self.bot.guilds)

        members = ctx.guild.members
        bots = len([m for m in members if m.bot])
        users = len(members) - bots
        online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
        offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
        idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)

        for guild in self.bot.guilds:
            members_count += len(guild.members)

        embed1 = discord.Embed(title=f"{ctx.guild.name}",
                               color=0x6A5ACD, timestamp=ctx.message.created_at)
        embed1.set_thumbnail(url=ctx.guild.icon_url)

        embed1.add_field(name=f"Пользователей", value=f"👥 Участников: **{users}**\n"
                                                      # f"‍🔧  Ботов: **{bots}**\n"
                                                      f"🟢 Онлайн: **{online}**\n"
                                                      f"🟠 Отошёл: **{idle}**\n"
                                                      f"🔴 Не Беспокоить: **{dnd}**\n"
                                                      f"⚫ Оффлайн: **{offline}**")

        embed1.add_field(name=f"Каналов", value=f"🔉 Голосовые: **{allvoice}**\n"
                                                f"💬 Текстовые: **{alltext}**\n")

        embed1.add_field(name=f"Уровень Буста",
                         value=f"{ctx.guild.premium_tier} (Бустеров: {ctx.guild.premium_subscription_count})")
        embed1.add_field(name=f"Количество Ролей", value=f"{allroles}")
        embed1.add_field(name=f"Создатель сервера", value=f"{ctx.guild.owner}")
        embed1.add_field(name=f"Регион сервера", value=f"{ctx.guild.region}")
        embed1.add_field(name=f'Сервер Meta Peace Team®', value="[[**кликните**]](https://discord.gg/ZrfkCEAcfW)",
                         inline=True)  # Создает строку
        embed1.add_field(name=f"Дата создания сервера", value=f"{ctx.guild.created_at.strftime('%b %#d %Y')}")

        embed1.add_field(name=f'Информацию запросил:', value=f'{ctx.author.mention}', inline=False)
        embed1.set_thumbnail(url=self.bot.user.avatar_url)
        embed1.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                          icon_url=self.bot.user.avatar_url)

        # ==================

        mem = psutil.virtual_memory()
        ping = self.bot.ws.latency

        ping_emoji = "🟩🔳🔳🔳🔳"
        ping_list = [
            {"ping": 0.00000000000000000, "emoji": "🟩🔳🔳🔳🔳"},
            {"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
            {"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
            {"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
            {"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
            {"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
            {"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}
        ]

        for ping_one in ping_list:
            if ping <= ping_one["ping"]:
                ping_emoji = ping_one["emoji"]
                break

        embed2 = discord.Embed(title='Статистика системы', color=0x6A5ACD)

        embed2.add_field(name='Использование CPU',
                         value=f'💻 Используется:\n **{psutil.cpu_percent()}%**',
                         inline=True)

        embed2.add_field(name='Использование RAM',
                         value=
                         f'📀 Всего: **{bytes2human(mem.total)}**\n'
                         f'💿 Используется: **{bytes2human(mem.used)}**',
                         inline=True)

        embed2.add_field(name='Задержка системы',
                         value=f'📡 Ping: **{ping * 1000:.0f}ms**\n'
                               f'`{ping_emoji}`',
                         inline=True)
        embed2.add_field(name="Аптайм системы от:",
                         value=f'🕥 {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d | %H:%M:%S")}')

        embeds = [embed1, embed2]

        await msg.delete()
        await ctx.message.delete()
        message = await ctx.send(embed=embed1)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                         footer_icon=self.bot.user.avatar_url, timeout=30, use_exit=True, delete_message=True,
                         color=0x6A5ACD, use_remove_reaction=True)
        await page.start()


def setup(bot):
    bot.add_cog(DevOpStatusCog(bot))
