"""
Today is 2/15/2021
Session by: https://github.com/DevilDesigner
Create Time: 1:38 AM
This Class: member_activity
"""

import discord
from discord.ext import commands

from config import member_activity


class MemberActivityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=member_activity)
    async def activity(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        if len(member.activities) <= 0:
            return await ctx.send("Этот пользователь не играет в игру")
        current_activity = member.activities[0]

        desc = ""

        if current_activity.type:
            if current_activity.type == discord.ActivityType.playing:
                desc += "Тип активности: Игра\n\n"

            elif current_activity.type == discord.ActivityType.streaming:
                desc += "Тип активности: Стрим\n\n"

            elif current_activity.type == discord.ActivityType.listening and not isinstance(current_activity,
                                                                                            discord.Spotify):
                desc += "Тип активности: Музыка\n\n"

            elif current_activity.type == discord.ActivityType.listening and isinstance(current_activity,
                                                                                        discord.Spotify):
                desc += "Тип активности: Spotify\n\n"

            elif current_activity.type == discord.ActivityType.watching:
                desc += "Тип активности: Просмотр\n\n"

            else:
                desc += "Тип активности: Кастом\n\n"

        if isinstance(current_activity, discord.CustomActivity):
            desc += f"Название: {current_activity.name}\n\n"
            desc += f"Создано: {current_activity.created_at.strftime('%d-%m-%Y %H:%M:%S')}"

        if isinstance(current_activity, discord.Spotify):
            desc += f"Название альбома: {current_activity.album}\n\n"

        else:
            if current_activity.name:
                desc += f"Название: {current_activity.name}\n\n"

        if not isinstance(current_activity, discord.Spotify):
            if current_activity.details:
                desc += f"Детали: {current_activity.details}\n\n"

            if current_activity.state:
                desc += f"Состояние: {current_activity.state}\n\n"

        else:
            desc += f"Артисты: {', '.join(current_activity.artists)}\n\n"
            total_seconds = current_activity.duration.seconds
            hours = total_seconds // 3600
            minutes = (total_seconds - hours * 3600) // 60
            seconds = total_seconds - (hours * 3600 + minutes * 60)
            desc += f"Продолжительность трека: {hours if str(hours) != '0' else '00'}:{minutes if str(minutes) != '0' else '00'}:{seconds if str(seconds) != '0' else '00'}\n\n"
            desc += f"Название трека: {current_activity.title}\n\n"

        if current_activity.start:
            desc += f"Начал: {current_activity.start.strftime('%d.%m.%Y %H:%M:%S')}\n\n"

        if current_activity.end:
            desc += f"Закончит: {current_activity.end.strftime('%d.%m.%Y %H:%M:%S')}\n\n"

        if not isinstance(current_activity, discord.Spotify):
            if current_activity.large_image_text:
                desc += f"Текст большой картинки: {current_activity.large_image_text}\n\n"

            if current_activity.small_image_text:
                desc += f"Текст маленькой картинки: {current_activity.small_image_text}\n\n"

            if current_activity.large_image_url:
                desc += f"[Большая картинка]({current_activity.large_image_url})\n\n"

            if current_activity.small_image_url:
                desc += f"[Маленькая картинка]({current_activity.small_image_url})"

        embed = discord.Embed(title="Активность", description=desc, color=0x16b568)
        embed.set_thumbnail(url=member.activities.large_image_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MemberActivityCog(bot))
