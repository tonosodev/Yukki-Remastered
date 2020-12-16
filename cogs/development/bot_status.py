import random

import discord
import psutil
from Cybernator import Paginator
from discord.ext import commands
from psutil._common import bytes2human


class DevOpStatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def bytes2human(number, typer=None):
        # Пример Работы Этой Функции перевода чисел:
        # >> bytes2human(10000)
        # >> '9.8K'
        # >> bytes2human(100001221)
        # >> '95.4M'

        if typer == "system":
            symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ',
                       'ИБ')  # Для перевода в Килобайты, Мегабайты, Гигобайты, Террабайты, Петабайты, Петабайты, Эксабайты, Зеттабайты, Йоттабайты
        else:
            symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')  # Для перевода в обычные цифры (10k, 10MM)

        prefix = {}

        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10

        for s in reversed(symbols):
            if number >= prefix[s]:
                value = float(number) / prefix[s]
                return '%.1f%s' % (value, s)

        return f"{number}B"

    @commands.command(
        name="бот",
        aliases=["bot", "botinfo", "ботинфо"],
        brief="Информация о боте",
        usage="бот <None>",
        description="Подробная информация о боте")
    async def _bot(self, ctx):
        await ctx.message.delete()

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
                               color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                            random.randint(1, 255)), timestamp=ctx.message.created_at)
        embed1.set_thumbnail(url=ctx.guild.icon_url)

        embed1.add_field(name=f"Пользователей", value=f"🐥 Участников: **{users}**\n"
                                                      f"‍🔧  Ботов: **{bots}**\n"
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
        embed1.add_field(name=f"Дата создания сервера", value=f"{ctx.guild.created_at.strftime('%b %#d %Y')}")

        embed1.add_field(name=f'Сервер Meta Peace Team®:', value="[Тык](https://discord.gg/e46AKbpV)",
                         inline=True)  # Создает строку
        embed1.set_thumbnail(url=self.bot.user.avatar_url)
        embed1.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                          icon_url=self.bot.user.avatar_url)  # создаение футера

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
                         value=f'Используется:\n **{psutil.cpu_percent()}%**',
                         inline=True)

        embed2.add_field(name='Использование RAM',
                         value=f'Доступно: {bytes2human(mem.available)}\n'
                               f'Используется: {bytes2human(mem.used)} **({mem.percent}%)**\n'
                               f'Всего: {bytes2human(mem.total)}',
                         inline=True)

        embed2.add_field(name='Задержка системы',
                         value=f'Ping: **{ping * 1000:.0f}ms**\n'
                               f'`{ping_emoji}`',
                         inline=True)

        for disk in psutil.disk_partitions():
            usage = psutil.disk_usage(disk.mountpoint)
            embed2.add_field(name="‎‎‎‎", value=f'```{disk.device}```',
                             inline=False)
            embed2.add_field(name='Всего на диске',
                             value=f'{bytes2human(usage.total)}', inline=True)
            embed2.add_field(name='Свободное место на диске',
                             value=f'{bytes2human(usage.free)}', inline=True)
            embed2.add_field(name='Используемое дисковое пространство',
                             value=f'{bytes2human(usage.used)}', inline=True)

        embeds = [embed1, embed2]

        message = await ctx.send(embed=embed1)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                         footer_icon=self.bot.user.avatar_url, timeout=120, use_exit=True, delete_message=False,
                         color=0x6A5ACD, use_remove_reaction=True)
        await page.start()


def setup(bot):
    bot.add_cog(DevOpStatusCog(bot))
