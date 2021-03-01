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
    async def __user_info(self, ctx, member: discord.Member = None):
        def isnitro():
            if member.premium_since:
                return f'{member.premium_since.strftime("%d/%m/%Y")}'
            else:
                return 'Отсутствует'

        def isbot():
            if member.bot:
                return 'Да'
            else:
                return 'Нет'

        def isnick():
            if member.nick:
                return f'{member.nick}'
            else:
                return 'без изменений'

        def isactivity():
            desc = ""
            if not member.activity:
                desc += 'Нету статуса'
            # elif member.activity.name:
            #    desc += f'{member.activity.name}'
            else:
                current_activity = member.activities[0]
                if current_activity.type:
                    if current_activity.type == discord.ActivityType.listening and not isinstance(current_activity,
                                                                                                  discord.Spotify):
                        desc += "Тип активности: Музыка\n"

                    elif current_activity.type == discord.ActivityType.listening and isinstance(current_activity,
                                                                                                discord.Spotify):
                        desc += "Тип активности: Spotify\n"
                        desc += f"Название трека: {current_activity.title}\n"
                        desc += f"Название альбома: {current_activity.album}\n"
                        desc += f"Артисты: {', '.join(current_activity.artists)}\n"
                        total_seconds = current_activity.duration.seconds
                        hours = total_seconds // 3600
                        minutes = (total_seconds - hours * 3600) // 60
                        seconds = total_seconds - (hours * 3600 + minutes * 60)
                        desc += f"Продолжительность трека: {hours if str(hours) != '0' else '00'}:{minutes if str(minutes) != '0' else '00'}:{seconds if str(seconds) != '0' else '00'}\n"


                    elif current_activity.type == discord.ActivityType.watching:
                        desc += "Тип активности: Просмотр\n"

                    else:
                        desc += "Тип активности: Кастом\n"
                        desc += f"Играет в: {current_activity.name}\n"
                        desc += f"Создано: {current_activity.created_at.strftime('%d-%m-%Y %H:%M:%S')}"
            return desc

        if member is None:
            member = ctx.author
            embed = discord.Embed(title=f'Информация о {member.name}#{member.discriminator}', color=member.color)
            embed.add_field(name="ID Юзера:", value=member.id)
            embed.add_field(name="Ник на сервере:", value=isnick())
            embed.add_field(name="Присоеденился на сервер:", value=member.joined_at.strftime("%d/%m/%Y"))
            embed.add_field(name="Бот?", value=isbot())
            embed.add_field(name="Роли:", value=" ".join(role.mention for role in member.roles[1:]))
            embed.add_field(name="Высшая роль:", value=member.top_role.mention)
            embed.add_field(name="Активность:", value=isactivity())
            embed.add_field(name="Дата получения нитро:", value=isnitro())
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title=f'Информация о {member.name}#{member.discriminator}', color=member.color)
            embed.add_field(name="ID Юзера:", value=member.id)
            embed.add_field(name="Ник на сервере:", value=isnick())
            embed.add_field(name="Присоеденился на сервер:", value=member.joined_at.strftime("%d/%m/%Y"))
            embed.add_field(name="Бот?", value=isbot())
            embed.add_field(name="Роли:", value=" ".join(role.mention for role in member.roles[1:]))
            embed.add_field(name="Высшая роль:", value=member.top_role.mention)
            embed.add_field(name="Активность:", value=isactivity())
            embed.add_field(name="Дата получения нитро:", value=isnitro())
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(MemberActivityCog(bot))
