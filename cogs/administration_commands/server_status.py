import json

import discord
import datetime
import psutil
import requests
from Cybernator import Paginator
from discord.ext import commands
from psutil._common import bytes2human

from config import server_status_aliases, commands_permission, bot_initialize


class ServerStatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=server_status_aliases)
    @commands.has_any_role(*commands_permission['server_status_permission'])
    async def status(self, ctx):
        msg = await ctx.reply("`Пожалуйста, подождите. . .`")
        members_count = 0
        guild_count = len(self.bot.guilds)

        def region(region: discord.VoiceRegion = None):
            if region == discord.VoiceRegion.amsterdam:
                return ":flag_nl: Амстердам"
            if region == discord.VoiceRegion.brazil:
                return ":flag_br: Бразилия"
            if region == discord.VoiceRegion.dubai:
                return ":flag_ae: Дубаи"
            if region == discord.VoiceRegion.eu_central:
                return ":flag_eu: Центральная Европа"
            if region == discord.VoiceRegion.eu_west:
                return ":flag_eu: Западная Европа"
            if region == discord.VoiceRegion.europe:
                return ":flag_eu: Европа"
            if region == discord.VoiceRegion.frankfurt:
                return ":flag_fk: Франкфурт"
            if region == discord.VoiceRegion.hongkong:
                return ":flag_hk: Гонк-конг"
            if region == discord.VoiceRegion.india:
                return ":flag_in: Индия"
            if region == discord.VoiceRegion.japan:
                return ":flag_jp: Япония"
            if region == discord.VoiceRegion.london:
                return ":flag_gb: Лондон"
            if region == discord.VoiceRegion.russia:
                return ":flag_ru: Россия"
            if region == discord.VoiceRegion.singapore:
                return ":flag_sg: Сингапур"
            if region == discord.VoiceRegion.southafrica:
                return ":flag_af: Южная Африка"
            if region == discord.VoiceRegion.sydney:
                return ":flag_sy: Сидней"
            if region == discord.VoiceRegion.us_east:
                return ":flag_us: Востоковая Америка"
            if region == discord.VoiceRegion.us_south:
                return ":flag_us: Южная Америка"
            if region == discord.VoiceRegion.us_west:
                return ":flag_us: Западная Америка"
            if region == discord.VoiceRegion.vip_amsterdam:
                return "[VIP] :flag_nl: Амстердам"
            if region == discord.VoiceRegion.vip_us_east:
                return "[VIP] :flag_us: Востоковая Америка"
            if region == discord.VoiceRegion.vip_us_west:
                return "[VIP] :flag_us: Западная Америка"
            else:
                return '🏳️ Не знаю'

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

        #
        #  Server Info Embed
        #

        for guild in self.bot.guilds:
            members_count += len(guild.members)

        embed_server_info = discord.Embed(title=f"{ctx.guild.name}",
                                          color=0x6A5ACD, timestamp=ctx.message.created_at)
        embed_server_info.set_thumbnail(url=ctx.guild.icon_url)

        embed_server_info.add_field(name=f"__**Пользователи**__",
                                    value=f"<:groups:816332018396168254> Участников: **{users}**\n"
                                    # f"<:bot:816332020745371668> Ботов: **{bots}**\n"
                                          f"<:online:816332016551329832> Онлайн: **{online}**\n"
                                          f"<:sleep:816332016172662804> Отошёл: **{idle}**\n"
                                          f"<:dnd:816332015845638194> Не Беспокоить: **{dnd}**\n"
                                          f"<:offline:816332016453812236> Оффлайн: **{offline}**")

        embed_server_info.add_field(name=f"__**Каналы**__",
                                    value=f"<:voice:816332018304155698> Голосовые: **{allvoice}**\n"
                                          f"<:text:816332018077007933> Текстовые: **{alltext}**\n")

        embed_server_info.add_field(name=f"__**Количество Ролей**__", value=f"{allroles}")
        embed_server_info.add_field(name=f"__**Уровень буста**__",
                                    value=f"<a:nitro:816330886567034880> **{ctx.guild.premium_tier}** | Бустов: **{ctx.guild.premium_subscription_count}**",
                                    inline=False)
        embed_server_info.add_field(name=f'__**Сервер {ctx.guild.name}**__',
                                    value="[[**кликните**]](https://discord.gg/VSAcZUX22a)",
                                    inline=True)
        embed_server_info.add_field(name=f"__**Дата создания сервера**__",
                                    value=f"{ctx.guild.created_at.strftime('%d/%#m/%Y')}")
        embed_server_info.add_field(name=f"__**Создатель сервера**__", value=f"{ctx.guild.owner.mention}", inline=False)
        embed_server_info.add_field(name=f"__**Регион сервера**__", value=region(ctx.guild.region))

        embed_server_info.add_field(name=f'__**Информацию запросил**__:', value=f'{ctx.author.mention}', inline=False)
        embed_server_info.set_thumbnail(url=ctx.guild.icon_url)
        embed_server_info.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
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

        #
        #  Discord Status Embed
        #

        ret = requests.get('https://status.discordapp.com/index.json')
        rec = json.loads(ret.text)
        color = 0x000000
        if rec['status']['description'] == "All Systems Operational":
            discord_rec = '<a:shard_2:816330982545424415> Все системы активны!'
        else:
            discord_rec = '<a:attention:816330945429897216> Присутствуют проблемы с подключением!'
        embed_discord_status = discord.Embed(title="Состояние Discord", color=0x6A5ACD,
                                             description='Данные получены из [Discord\'s status](https://status.discordapp.com/index.json).')
        embed_discord_status.set_thumbnail(url="https://img.icons8.com/nolan/452/discord-logo.png")
        if rec["components"][0]["status"] == "operational":
            embed_discord_status.add_field(name="__**API**__", value="✅", inline=True)
        else:
            embed_discord_status.add_field(name="__**API**__", value='❌', inline=True)
        if rec["components"][1]["status"] == "operational":
            embed_discord_status.add_field(name="__**Шлюз**__", value='✅', inline=True)
        else:
            embed_discord_status.add_field(name="__**Шлюз**__", value='❌', inline=True)
        if rec["components"][2]["status"] == "operational":
            embed_discord_status.add_field(name="__**CloudFlare**__", value='✅', inline=True)
        else:
            embed_discord_status.add_field(name="__**CloudFlare**__", value='❌', inline=True)
        if rec["components"][3]["status"] == "operational":
            embed_discord_status.add_field(name="__**Медиа прокси**__", value='✅', inline=True)
        else:
            embed_discord_status.add_field(name="__**Шлюз**__", value='❌', inline=True)
        if rec["components"][3]["status"] == "operational":
            embed_discord_status.add_field(name="__**Голосовые сервера**__", value='✅', inline=False)
            embed_discord_status.add_field(name="__**Ответ сервера**__", value=discord_rec)
        else:
            embed_discord_status.add_field(name="__**Шлюз**__", value='❌', inline=True)

        #
        #  System Info Embed
        #

        for ping_one in ping_list:
            if ping <= ping_one["ping"]:
                ping_emoji = ping_one["emoji"]
                break

        embed_system_information = discord.Embed(title='__**Состояние системы**__', color=0x6A5ACD)
        embed_system_information.set_thumbnail(url="https://img.icons8.com/cotton/2x/server.png")
        embed_system_information.add_field(name='__**Использование CPU**__',
                                           value=f'💻 Используется:\n **{psutil.cpu_percent()}%**',
                                           inline=True)

        embed_system_information.add_field(name='__**Использование RAM**__',
                                           value=
                                           f'💿 Используется: **{bytes2human(mem.used)} \ {bytes2human(mem.total)}**',
                                           inline=True)

        embed_system_information.add_field(name='__**Задержка системы**__',
                                           value=f'📡 Ping: **{ping * 1000:.0f}ms**\n'
                                                 f'`{ping_emoji}`',
                                           inline=True)
        embed_system_information.add_field(name="__**Аптайм системы от**__:",
                                           value=f'🕥 ||{datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%y | %H:%M")}||')

        embeds = [embed_server_info, embed_discord_status, embed_system_information]

        await msg.delete()
        await ctx.message.delete()
        message = await ctx.send(embed=embed_server_info)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                         footer_icon=self.bot.user.avatar_url, timeout=30, use_exit=True, delete_message=True,
                         color=0x6A5ACD, use_remove_reaction=True)
        await page.start()


def setup(bot):
    bot.add_cog(ServerStatusCog(bot))
