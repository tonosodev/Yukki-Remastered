import asyncio

import discord
from discord.ext import commands
import random
from io import BytesIO
from config import commands_permission, user_report_command_aliases, bot_settings, bot_initialize, \
    user_report_reaction_permission_owner, user_report_reaction_permission_support, server_roles
from managers_data import MetaPeace_owner_url


class UserReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=user_report_command_aliases)
    @commands.has_any_role(*commands_permission['user_report_command_permission'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def report(self, ctx, member: discord.Member = None, *, reason=None):
        report_logs = self.bot.get_channel(bot_settings['report_channel'])
        info_logs = self.bot.get_channel(bot_settings['log_channel'])
        load_variable = await ctx.reply(f"{ctx.author.mention}, пожалуйста, подождите. . .")
        token = random.randint(111111111, 999999999)
        roles = [ctx.guild.get_role(user_report_reaction_permission_owner),
                 ctx.guild.get_role(user_report_reaction_permission_support)]
        # Отправка эмбеда об ошибке, если не указан пользователь.
        if member is None:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.add_field(name='__**Ошибка при отправке жалобы от**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Перед отправкой соблюдайте следующие пункты**__:',
                            value='- Укажите @пользователя и "причину"'
                                  '\n- Прикрепите снимок нарушения со стороны пользователя к сообщению', inline=False)
            embed.add_field(name="__**Совет**__:",
                            value='Для обработки жалобы не прикрепляйте изображения большого размера!', inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.add_field(name='__**Пример правильного заполнения**__:', value="*см. во вложении.", inline=False)
            embed.set_image(
                url='https://sun9-48.userapi.com/impg/xvWDgPDXtJlEXP2NeWY6E5zGld0WUxc5JE6Pvw/s6FniY0Yz0M.jpg?size=594x595&quality=96&proxy=1&sign=eb265d60619fb69cd078a2e3816a1c6c&type=album')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        # Отправка эмбеда об ошибке, если пользователь - автор.

        elif member is ctx.message.author:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=member.color)
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:', value="Вы не можете просто взять, и пожаловаться на самого себя..."
                                                           "\nОставьте это другим пользователям!", inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        # Отправка эмбеда об ошибке, если пользователь - создатель или имеет роль старшего руководителя.

        elif member is ctx.guild.owner or any([role in member.roles for role in roles]):
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=member.color)
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:',
                            value="Вы ведь понимаете, что жалоба на старший состав руководителей все равно не может быть обработана?..."
                                  "\nНе занимайтесь глупостями!", inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)


        # Отправка эмбеда об ошибке, если не указана причина.
        else:
            if reason is None:
                await load_variable.delete()
                embed = discord.Embed(title="Жалоба ❌",
                                      color=member.color)
                embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
                embed.add_field(name='__**Причина**__:', value="Не указана причина жалобы."
                                                               "\nПожалуйста, укажите причину репорта после упоминания пользователя!",
                                inline=False)
                embed.add_field(name="__**Совет**__:",
                                value=f"Пропишите «{bot_settings['bot_prefix']}репорт» для вывода информации по заполнению формы!",
                                inline=False)
                embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
                embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                 icon_url=self.bot.user.avatar_url)
                await ctx.reply(embed=embed)
                self.report.reset_cooldown(ctx)

            # Отправка эмбеда жалобы

            elif reason is not None:
                try:
                    files = []
                    for file in ctx.message.attachments:
                        fp = BytesIO()
                        await file.save(fp)
                        files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

                    embed = discord.Embed(title="Жалоба 💬",
                                          color=member.color)
                    embed.add_field(name='__**Выдана**__:', value=ctx.author.mention, inline=False)
                    embed.add_field(name='__**Состояние**__:', value='На рассмотрении...', inline=False)
                    embed.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                    embed.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                    embed.add_field(name='__**Уникальный номер**__:', value='#' + str(token), inline=False)
                    embed.add_field(name='__**Причина**__:', value=reason, inline=False)
                    embed.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                    embed.set_image(url=f"attachment://{files[0].filename}")
                    embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                     icon_url=self.bot.user.avatar_url)

                    embed_success = discord.Embed(title="Жалоба 💬",
                                                  color=member.color)
                    embed_success.add_field(name='__**В обработку принята жалоба**__', value='#' + str(token),
                                            inline=False)
                    embed_success.add_field(name='__**Выдана**__:', value=ctx.author.mention, inline=False)
                    embed_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                    embed_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                    embed_success.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)

                    await ctx.send(embed=embed_success, delete_after=15)
                    await ctx.author.send(embed=embed_success)

                    await ctx.message.delete()
                    await load_variable.delete()

                    msg = await report_logs.send(embed=embed, files=files)
                    warn_reaction = await msg.add_reaction("<:sys_warn:816798299541078046>")
                    mute_reaction = await msg.add_reaction("<:sys_mute:816800250148552735>")
                    kick_reaction = await msg.add_reaction("<:sys_kick:816799762245877810>")
                    ban_reaction = await msg.add_reaction("<:sys_ban:816797326474739744>")
                    close_ticket_reaction = await msg.add_reaction("<:mark:816332017477615698>")

                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=3600.0,
                                                                 check=lambda react, user:
                                                                 any([role in user.roles for role in roles])
                                                                 and react.message.id == msg.id and str(
                                                                     react.emoji) in ["<:sys_warn:816798299541078046>", "<:sys_mute:816800250148552735>", "<:sys_kick:816799762245877810>", "<:sys_ban:816797326474739744>", "<:mark:816332017477615698>"])
                    except asyncio.TimeoutError:
                        return await msg.clear_reactions()

                    #
                    #  WARN REACTION
                    #

                    if str(reaction.emoji) == "<:sys_warn:816798299541078046>":
                        files = []
                        for file in ctx.message.attachments:
                            fp = BytesIO()
                            await file.save(fp)
                            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
                        embed_warn_success = discord.Embed(title="Жалоба 💬",
                                                           color=member.color)
                        embed_warn_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                     inline=False)
                        embed_warn_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_warn_success.add_field(name='__**Решение**__:',
                                                     value=f'Заявка **обработана** руководителем {user.mention}.\n__**Наказание:**__ \n||Пользователю вынесено предупреждение.||')
                        embed_warn_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                        embed_warn_success.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                        embed_warn_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                     inline=False)
                        embed_warn_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_warn_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_warn_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_warn_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)

                        await msg.clear_reactions()
                        await msg.edit(embed=embed_warn_success)

                    #
                    #  MUTE REACTION
                    #

                    if str(reaction.emoji) == "<:sys_mute:816800250148552735>":
                        files = []
                        for file in ctx.message.attachments:
                            fp = BytesIO()
                            await file.save(fp)
                            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
                        embed_mute_success = discord.Embed(title="Жалоба 💬",
                                                           color=member.color)
                        embed_mute_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                     inline=False)
                        embed_mute_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_mute_success.add_field(name='__**Решение**__:',
                                                     value=f'Заявка **обработана** руководителем {user.mention}.\n__**Наказание:**__ \n||Пользователю выдан мут.||')
                        embed_mute_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                        embed_mute_success.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                        embed_mute_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                     inline=False)
                        embed_mute_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_mute_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_mute_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_mute_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)

                        member_role = discord.utils.get(ctx.message.guild.roles, id=server_roles['member_role'])
                        mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTED')
                        info_mute = discord.Embed(title=f'Мут 🔇', color=0x4B0082)
                        info_mute.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        info_mute.add_field(name='__**Выдал(а)**__:', value=user.mention, inline=False)
                        info_mute.add_field(name='__**Тип наказания**__:', value='Mute', inline=False)
                        info_mute.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                        info_mute.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                        info_mute.add_field(name='__**Причина**__:', value=f'{reason}', inline=False)
                        info_mute.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)
                        await info_logs.send(embed=info_mute)

                        await member.remove_roles(member_role)
                        await member.add_roles(mute_role, reason=str(reason), atomic=True)

                        await msg.clear_reactions()
                        await msg.edit(embed=embed_mute_success)

                    #
                    #  KICK REACTION
                    #

                    if str(reaction.emoji) == "<:sys_kick:816799762245877810>":
                        files = []
                        for file in ctx.message.attachments:
                            fp = BytesIO()
                            await file.save(fp)
                            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
                        embed_kick_success = discord.Embed(title="Жалоба 💬",
                                                           color=member.color)
                        embed_kick_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                     inline=False)
                        embed_kick_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_kick_success.add_field(name='__**Решение**__:',
                                                     value=f'Заявка **обработана** руководителем {user.mention}.\n__**Наказание:**__ \n||Пользователь кикнут с сервера.||')
                        embed_kick_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                        embed_kick_success.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                        embed_kick_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                     inline=False)
                        embed_kick_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_kick_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_kick_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_kick_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)

                        info_kick = discord.Embed(title='Кик :wave:', colour=discord.Color.red())
                        info_kick.set_author(name=member.name, icon_url=member.avatar_url)
                        info_kick.add_field(name='Был кикнут', value='пользователь: {}'.format(member.mention))
                        info_kick.set_footer(text='Кикнут с сервера руководителем {}'.format(user.name),
                                             icon_url=user.avatar_url)
                        await info_logs.send(embed=info_kick)

                        try:
                            for_kicked_user_embed = discord.Embed(color=0x8B0000,
                                                                  title="‼Вас выгнали с сервера\n Meta Peace Team®")
                            for_kicked_user_embed.add_field(name="__**Жалобу обработал управляющий**__:",
                                                            value=f"{user}", inline=False)
                            for_kicked_user_embed.add_field(name="__**Причина пользовательской жалобы**__:",
                                                            value=str(reason), inline=False)
                            for_kicked_user_embed.set_image(
                                url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")
                            await member.send(embed=for_kicked_user_embed)
                            await member.send(
                                f'\n```Если Вы считаете, что это произошло по ошибке, пожалуйста, успокойтесь и сообщите об инциденте разработчику:```'
                                f'```fix\nDiscord: {ctx.guild.owner}\nVKontakte: {MetaPeace_owner_url["vk"]}\n```'
                                f'```Приносим глубочайшие сожаления.```')
                        except Exception:
                            await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                                description=f'❗️ Не удалось отправить личное сообщение пользователю {member}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                        finally:
                            await member.kick()
                        await msg.clear_reactions()
                        await msg.edit(embed=embed_kick_success)

                    #
                    #  BAN REACTION
                    #

                    if str(reaction.emoji) == "<:sys_ban:816797326474739744>":
                        files = []
                        for file in ctx.message.attachments:
                            fp = BytesIO()
                            await file.save(fp)
                            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

                        embed_ban_success = discord.Embed(title="Жалоба 💬",
                                                          color=member.color)
                        embed_ban_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                    inline=False)
                        embed_ban_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_ban_success.add_field(name='__**Решение**__:',
                                                    value=f'Заявка **обработана** руководителем {user.mention}.\n__**Наказание:**__ \n||Пользователь заблокирован на сервере.||')
                        embed_ban_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                        embed_ban_success.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                        embed_ban_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                    inline=False)
                        embed_ban_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_ban_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_ban_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_ban_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)

                        info_kick = discord.Embed(title='Бан 🔒', color=0x8B0000)
                        info_kick.set_author(name=member.name, icon_url=member.avatar_url)
                        info_kick.add_field(name='Был заблокирован', value=' пользователь: {}'.format(member.mention))
                        info_kick.set_footer(text='Заблокирован управляющим {}'.format(user.name),
                                             icon_url=user.avatar_url)
                        await info_logs.send(embed=info_kick)
                        try:
                            for_banned_user_embed = discord.Embed(color=0x8B0000,
                                                                  title="‼Вас заблокировали на сервере\n Meta Peace Team®")  # Создание Embed'a
                            for_banned_user_embed.add_field(name="__**Жалобу обработал управляющий**__:",
                                                            value=f"{user}", inline=False)
                            for_banned_user_embed.add_field(name="__**Причина пользовательской жалобы**__:",
                                                            value=str(reason), inline=False)
                            for_banned_user_embed.set_image(
                                url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")
                            await member.send(embed=for_banned_user_embed)
                            await member.send(
                                f'\n```Если Вы считаете, что это произошло по ошибке, пожалуйста, успокойтесь и сообщите об инциденте разработчику:```'
                                f'```fix\nDiscord: {ctx.guild.owner}\nVKontakte: {MetaPeace_owner_url["vk"]}\n```'
                                f'```Приносим глубочайшие сожаления.```')
                        except Exception:
                            await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                                description=f'❗️ Не удалось отправить личное сообщение пользователю {member}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                        finally:
                            await ctx.guild.ban(member)
                        await msg.clear_reactions()
                        await msg.edit(embed=embed_ban_success)

                    #
                    #  CLOSE TICKET REACTION
                    #

                    if str(reaction.emoji) == "<:mark:816332017477615698>":
                        # Редактирование основного эмбеда в случае отмены жалобы
                        files = []
                        for file in ctx.message.attachments:
                            fp = BytesIO()
                            await file.save(fp)
                            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

                        embed_report_success = discord.Embed(title="Жалоба 💬",
                                                             color=member.color)
                        embed_report_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                       inline=False)
                        embed_report_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_report_success.add_field(name='__**Решение**__:',
                                                       value=f'Заявка **отклонена** руководителем {user.mention}.\n__**Наказание:**__ \n||Не вынесено.||')
                        embed_report_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                        embed_report_success.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                        embed_report_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                       inline=False)
                        embed_report_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_report_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_report_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_report_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await msg.clear_reactions()
                        await msg.edit(embed=embed_report_success)

                # Отправка эмбеда об ошибке, если не прикреплено изображение.

                except:
                    await load_variable.delete()
                    embed = discord.Embed(title="Жалоба ❌",
                                          color=member.color)
                    embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}',
                                    inline=False)
                    embed.add_field(name='__**Причина**__:',
                                    value="К Вашему сообщению не было прикреплено изображения, подтверждающего причастность пользователя к правонарушению."
                                          "\nПожалуйста, сделайте снимок с нарушением и прикрепите его во вложение к жалобе перед её отправкой!",
                                    inline=False)
                    embed.add_field(name="__**Совет**__:",
                                    value=f"Пропишите «{bot_settings['bot_prefix']}репорт» для вывода информации по заполнению формы!",
                                    inline=False)
                    embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
                    embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                     icon_url=self.bot.user.avatar_url)
                    await ctx.reply(embed=embed)

                    self.report.reset_cooldown(ctx)


def setup(bot):
    bot.add_cog(UserReport(bot))
