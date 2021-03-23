"""
Today is 2/15/2021
Session by: https://github.com/DevilDesigner
Create Time: 1:38 AM
This Class: member_activity
"""

import discord
from Cybernator import Paginator
from discord.ext import commands
from loguru import logger

from config import member_activity, bot_initialize


class MemberActivityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog MemberInfo loaded!")

    @commands.command(aliases=member_activity)
    async def __user_info(self, ctx, member: discord.Member = None):
        msg = await ctx.reply("`Пожалуйста, подождите. . .`")

        #
        # Activity stats embed
        #

        def isnitro():
            if member.premium_since:
                return f'{member.premium.strftime("%d/%m/%Y")}'
            else:
                return 'Подписка отсутствует'

        # def isbot():
        #    if member.bot:
        #        return 'Да'
        #    else:
        #        return 'Нет'

        def isnick():
            if member.nick:
                return f'{member.nick}'
            else:
                return 'Без изменений'

        def isactivity():
            desc = ""
            if not member.activity:
                desc += 'Отсутствует'
            # elif member.activity.name:
            #   desc += f'{member.activity.name}'
            else:
                current_activity = member.activities[0]
                if current_activity.type:
                    if current_activity.type == discord.ActivityType.listening and not isinstance(current_activity,
                                                                                                  discord.Spotify):
                        desc += "Прослушивает музыку\n"

                    elif current_activity.type == discord.ActivityType.listening and isinstance(current_activity,
                                                                                                discord.Spotify):
                        desc += "Слушает Spotify\n"
                        desc += f"Название трека: **{current_activity.title}**\n"
                        desc += f"Название альбома: **{current_activity.album}**\n"
                        desc += f"Исполнители: **{', '.join(current_activity.artists)}**\n"
                        total_seconds = current_activity.duration.seconds
                        hours = total_seconds // 3600
                        minutes = (total_seconds - hours * 3600) // 60
                        seconds = total_seconds - (hours * 3600 + minutes * 60)
                        desc += f"Продолжительность трека: **{hours if str(hours) != '0' else ''}{minutes if str(minutes) != '0' else '00'}:{seconds if str(seconds) != '0' else '00'}**\n"


                    elif current_activity.type == discord.ActivityType.watching:
                        desc += "Просматривает трансляцию\n"

                    else:
                        desc += f"Пользовательский статус:\n__{current_activity.name}__\n"
                        desc += f"Создан:\n __{current_activity.created_at.strftime('%d-%m-%Y | %H:%M')}__"
            return desc

        if member is None:
            member = ctx.author
            embed_self_info = discord.Embed(title=f'Информация о пользователе {member.name}#{member.discriminator}',
                                            color=member.color)

            embed_self_info.set_thumbnail(url=ctx.author.avatar_url)

            embed_self_info.add_field(name="__**Серверное имя**__:", value=ctx.author.mention)
            embed_self_info.add_field(name="__**Роли**__:", value=", ".join(role.mention for role in member.roles[1:]),
                                      inline=False)
            embed_self_info.add_field(name="__**Высшая роль**__:", value=member.top_role.mention, inline=True)
            embed_self_info.add_field(name="__**Текущая активность**__:", value=isactivity(), inline=False)
            embed_self_info.add_field(name="__**Присоеденился**__:", value=f"{str(member.joined_at)[:16]}",
                                      inline=True)
            embed_self_info.add_field(name="__**Аккаунт создан**__:", value=f"{str(member.created_at)[:16]}", inline=False),
            embed_self_info.add_field(name="__**ID пользователя**__:", value=f"||{member.id}||", inline=False)
            # embed.add_field(name="Бот?", value=isbot())
            embed_self_info.add_field(name="__**Дата получения Nitro**__:", value=isnitro(), inline=True)
            embed_self_info.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                       icon_url=self.bot.user.avatar_url)
            #
            # Stats embed
            #

            embed_self_stats = discord.Embed(title=f"Статистика пользователя {member.name}#{member.discriminator}",
                                             color=member.color)
            embed_self_stats.add_field(name="__**Баланс**__:", value='None <:yukki_dollar:816330956137824266>',
                                       inline=False)
            embed_self_stats.add_field(name="__**Достижения**__:", value='None', inline=False)
            embed_self_stats.add_field(name="__**Предупреждений**__:", value='None / None', inline=False)
            embed_self_stats.set_thumbnail(url=member.avatar_url)

            #
            # Paginator
            #

            embeds = [embed_self_info, embed_self_stats]
            await msg.delete()
            await ctx.message.delete()
            message = await ctx.send(embed=embed_self_info)
            page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                             footer_icon=self.bot.user.avatar_url, timeout=30, use_exit=True, delete_message=True,
                             color=member.color, use_remove_reaction=True)
            await page.start()
        else:
            embed_member_info = discord.Embed(title=f'Информация о пользователе {member.name}#{member.discriminator}',
                                              color=member.color)

            embed_member_info.set_thumbnail(url=member.avatar_url)

            embed_member_info.add_field(name="__**Серверное имя**__:", value=ctx.author.mention)
            embed_member_info.add_field(name="__**Роли**__:",
                                        value=", ".join(role.mention for role in member.roles[1:]),
                                        inline=False)
            embed_member_info.add_field(name="__**Высшая роль**__:", value=member.top_role.mention, inline=True)
            embed_member_info.add_field(name="__**Текущая активность**__", value=isactivity(), inline=False)
            embed_member_info.add_field(name="__**Присоеденился**__:", value=member.joined_at.strftime("%d/%m/%Y"),
                                        inline=True)
            embed_member_info.add_field(name="__**ID пользователя**__:", value=f"||{member.id}||", inline=False)
            # embed.add_field(name="Бот?", value=isbot())
            embed_member_info.add_field(name="__**Дата получения Nitro**__:", value=isnitro(), inline=True)
            embed_member_info.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                         icon_url=self.bot.user.avatar_url)

            #
            # Stats embed
            #

            embed_member_stats = discord.Embed(title=f"Статистика пользователя {member.name}#{member.discriminator}",
                                               color=member.color)
            embed_member_stats.add_field(name="__**Баланс**__:", value='None', inline=False)
            embed_member_stats.add_field(name="__**Достижения**__:", value='None', inline=False)
            embed_member_stats.add_field(name="__**Предупреждений**__:", value='None / None', inline=False)
            embed_member_stats.set_thumbnail(url=member.avatar_url)

            #
            # Paginator
            #

            embeds = [embed_member_info, embed_member_stats]
            await msg.delete()
            await ctx.message.delete()
            message = await ctx.send(embed=embed_member_stats)
            page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, language="ru",
                             footer_icon=self.bot.user.avatar_url, timeout=30, use_exit=True, delete_message=True,
                             color=member.color, use_remove_reaction=True)
            await page.start()


def setup(bot):
    bot.add_cog(MemberActivityCog(bot))
