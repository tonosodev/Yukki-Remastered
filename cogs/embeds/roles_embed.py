"""
Today is 3/7/2021
Session by: https://github.com/DevilDesigner
Create Time: 8:38 AM
This Class: roles_embed
"""
from datetime import datetime

import discord
from discord.ext import commands

from config import commands_permission


class MetaPeaceRolesEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*commands_permission['server_status_permission'])
    async def roles_embed(self, ctx):
        # GENERAL ROLES
        programmer_role = ctx.guild.get_role(818001571710763028)
        designer_role = ctx.guild.get_role(818002281172697088)
        streamer_role = ctx.guild.get_role(818003818113269770)
        musician_role = ctx.guild.get_role(818002500111826978)
        writer_role = ctx.guild.get_role(818003143639433246)
        anime_role = ctx.guild.get_role(818004267084414976)
        memer_role = ctx.guild.get_role(818003458094399508)
        gamer_role = ctx.guild.get_role(818860755763331072)

        # EXTRA ROLES
        newspaper_role = ctx.guild.get_role(818748991135023125)

        await ctx.message.delete()
        await ctx.send(file=discord.File(r".\cogs\embeds\roles2.png"))
        msg = await ctx.send(
            "<:gdash:817934432661012480>   <:pdash:817934816950485042>   <:gdash:817934432661012480>   <:pdash:817934816950485042>   <:gdash:817934432661012480>   <:pdash:817934816950485042>   <:gdash:817934432661012480>   <:pdash:817934816950485042>\n\n"
            "<:blank:817933141514911754><:blank:817933141514911754><:blank:817933141514911754>ೋ•<a:magic:816330941424730132> **Хобби и интересы**\n\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:gamer:818865783479599154> ┇ {gamer_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:memer:818868967825080330> ┇ {memer_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:anime:818870007810883614> ┇ {anime_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:writter:818878406698598453> ┇ {writer_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:musician:818877410950119434> ┇ {musician_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:streamer:818867326564565033> ┇ {streamer_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:designer:818872164823728189> ┇ {designer_role.mention}\n"
            f"<:blank:817933141514911754><:blank:817933141514911754><:programmer:818874039178100776> ┇ {programmer_role.mention}\n\n"
            f"<:blank:817933141514911754>\n\n"
            # Header

            # Body
            # Description

            # Footer
        )
        # GENERAL EMOJIS
        gamer_emoji = await msg.add_reaction("<:gamer:818865783479599154>")
        memer_emoji = await msg.add_reaction("<:memer:818868967825080330>")
        anime_emoji = await msg.add_reaction("<:anime:818870007810883614>")
        writer_emoji = await msg.add_reaction("<:writter:818878406698598453>")
        musician_emoji = await msg.add_reaction("<:musician:818877410950119434>")
        streamer_emoji = await msg.add_reaction("<:streamer:818867326564565033>")
        designer_emoji = await msg.add_reaction("<:designer:818872164823728189>")
        programmer_emoji = await msg.add_reaction("<:programmer:818874039178100776>")


        news_channel = ctx.guild.get_channel(766213910595633155)
        msg2 = await ctx.send(
            f"<:blank:817933141514911754>\n\n"
            "<:wdash:817934436317528125>   <:pdash:817934816950485042>   <:wdash:817934436317528125>   <:pdash:817934816950485042>   <:wdash:817934436317528125>   <:pdash:817934816950485042>   <:wdash:817934436317528125>   <:pdash:817934816950485042>\n\n"
            "<:blank:817933141514911754><:blank:817933141514911754><:blank:817933141514911754>ೋ•<a:magic:816330941424730132> **Дополнительные**\n\n"
            f"..｡ﾟ+ <a:nwspaper:818848454708166707> ┇ {newspaper_role.mention} - новостная газета.\n"
            f"<:blank:817933141514911754>**Заметка:** ||__В Ваши личные сообщения будет отправляться рассылка информационных каналов!__||"
            f"<:blank:817933141514911754>"
        )
        # EXTRA EMOJIS
        newspaper_emoji = await msg2.add_reaction("<a:nwspaper:818848454708166707>")


def setup(bot):
    bot.add_cog(MetaPeaceRolesEmbed(bot))
