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
    async def report(self, ctx, suspect: discord.Member = None, *, reason=None):
        report_logs = self.bot.get_channel(bot_settings['report_channel'])
        info_logs = self.bot.get_channel(bot_settings['log_channel'])
        load_variable = await ctx.reply(f"{ctx.author.mention}, пожалуйста, подождите. . .")
        token = random.randint(111111111, 999999999)
        roles = [ctx.guild.get_role(user_report_reaction_permission_owner),
                 ctx.guild.get_role(user_report_reaction_permission_support)]
        # Отправка эмбеда об ошибке, если не указан пользователь.
        if suspect is None:
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

        elif suspect is ctx.message.author:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=suspect.color)
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:', value="Вы не можете просто взять, и пожаловаться на самого себя..."
                                                           "\nОставьте это другим пользователям!", inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        # Отправка эмбеда об ошибке, если пользователь - создатель или имеет роль старшего руководителя.

        elif suspect is ctx.guild.owner or any([role in suspect.roles for role in roles]):
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=suspect.color)
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:',
                            value="Вы ведь понимаете, что жалоба на старший состав руководителей все равно не может быть обработана?..."
                                  "\nНе занимайтесь глупостями!", inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        elif suspect.id == self.bot.user.id:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=suspect.color)
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:',
                            value="Ну и зачем жаловаться на Юкки?\n"
                                  "Она самый честный и справедливый участник сервера...", inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        elif suspect.bot:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=suspect.color)
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:',
                            value="Вы серьезно пытаетесь пожаловаться на бота?\n"
                                  "Глупости какие...", inline=False)
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
                                      color=suspect.color)
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
                                          color=suspect.color)
                    embed.add_field(name='__**Выдана**__:', value=ctx.author.mention, inline=False)
                    embed.add_field(name='__**Состояние**__:', value='На рассмотрении...', inline=False)
                    embed.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                    embed.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                    embed.add_field(name='__**Уникальный номер**__:', value='#' + str(token), inline=False)
                    embed.add_field(name='__**Причина**__:', value=reason, inline=False)
                    embed.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                    embed.set_image(url=f"attachment://{files[0].filename}")
                    embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                     icon_url=self.bot.user.avatar_url)

                    embed_success = discord.Embed(title="Жалоба 💬",
                                                  color=suspect.color)
                    embed_success.add_field(name='__**В обработку принята Ваша жалоба**__', value='#' + str(token),
                                            inline=False)
                    embed_success.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                    embed_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                    embed_success.add_field(name='ᅠ', value=f'__**Спасибо!**__\n'
                                                            f'Команда проекта {ctx.guild.name} ценит Ваш вклад в поддержку порядка на сервере.\n')
                    embed_success.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)

                    await ctx.author.send(embed=embed_success)

                    await ctx.message.delete()
                    await load_variable.delete()

                    msg = await report_logs.send(embed=embed, files=files)
                    close_ticket_reaction = await msg.add_reaction("<:mark:816332017477615698>")
                    warn_reaction = await msg.add_reaction("<:sys_warn:816798299541078046>")
                    mute_reaction = await msg.add_reaction("<:sys_mute:816800250148552735>")
                    kick_reaction = await msg.add_reaction("<:sys_kick:816799762245877810>")
                    ban_reaction = await msg.add_reaction("<:sys_ban:816797326474739744>")

                    try:
                        reaction, manager = await self.bot.wait_for('reaction_add', timeout=86400.0,
                                                                    check=lambda react, manager:
                                                                    any([role in manager.roles for role in roles])
                                                                    and react.message.id == msg.id and str(
                                                                        react.emoji) in [
                                                                        "<:sys_warn:816798299541078046>",
                                                                        "<:sys_mute:816800250148552735>",
                                                                        "<:sys_kick:816799762245877810>",
                                                                        "<:sys_ban:816797326474739744>",
                                                                        "<:mark:816332017477615698>"])
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
                                                           color=suspect.color)
                        embed_warn_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                     inline=False)
                        embed_warn_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_warn_success.add_field(name='__**Решение**__:',
                                                     value=f'Заявка **обработана** руководителем {manager.mention}.\n__**Наказание:**__ \n||Пользователю вынесено предупреждение.||')
                        embed_warn_success.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        embed_warn_success.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
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
                        info_warn = discord.Embed(title=f'Предупреждение ❗️', color=0x4B0082)
                        info_warn.set_author(name=f"Автор жалобы: {ctx.author}", icon_url=ctx.author.avatar_url)
                        info_warn.add_field(name='__**Выдал(а)**__:', value=manager.mention, inline=False)
                        info_warn.add_field(name='__**Тип наказания**__:', value='Warn', inline=False)
                        info_warn.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        info_warn.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        info_warn.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)
                        await info_logs.send(embed=info_warn)

                        info_warn_for_author = discord.Embed(title=f'Жалоба рассмотрена ✅', color=0x4B0082)
                        info_warn_for_author.add_field(name=f'__**Модерация успешно рассмотрела Вашу жалобу**__',
                                                       value=f'#{token}', inline=False)
                        info_warn_for_author.add_field(name=f'__**Решение:**__',
                                                       value=f'Пользователю {suspect.mention} было `вынесено предупреждение`.',
                                                       inline=False)
                        info_warn_for_author.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await ctx.author.send(embed=info_warn_for_author)

                        info_warn_for_suspect = discord.Embed(title=f'На Вас была рассмотрена жалоба ‼', color=0x4B0082)
                        info_warn_for_suspect.add_field(name=f'__**Модерация рассмотрела жалобу на Вас**__',
                                                        value=f'#{token}', inline=False)
                        info_warn_for_suspect.add_field(name=f'__**Жалобу выдал**__:', value=f"{manager.mention}")
                        info_warn_for_suspect.add_field(name=f'__**Решение:**__',
                                                        value=f'Вам было `вынесено предупреждение`.',
                                                        inline=False)
                        info_warn_for_suspect.add_field(name='ᅠ',
                                                        value=f'__**Пожалуйста...**__\n'
                                                              f'Постарайтесь впредь соблюдать правила поведения на сервере {ctx.guild.name}.\n'
                                                              f'Дружный коллектив - залог общего успеха!',
                                                        inline=False)
                        info_warn_for_suspect.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await suspect.send(embed=info_warn_for_suspect)

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
                                                           color=suspect.color)
                        embed_mute_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                     inline=False)
                        embed_mute_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_mute_success.add_field(name='__**Решение**__:',
                                                     value=f'Заявка **обработана** руководителем {manager.mention}.\n__**Наказание:**__ \n||Пользователю выдан мут.||')
                        embed_mute_success.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        embed_mute_success.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
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
                        await suspect.remove_roles(member_role)
                        await suspect.add_roles(mute_role, reason=str(reason), atomic=True)

                        await msg.clear_reactions()
                        await msg.edit(embed=embed_mute_success)

                        info_mute = discord.Embed(title=f'Мут 🔇', color=0x4B0082)
                        info_mute.set_author(name=f"Автор жалобы: {ctx.author}", icon_url=ctx.author.avatar_url)
                        info_mute.add_field(name='__**Выдал(а)**__:', value=manager.mention, inline=False)
                        info_mute.add_field(name='__**Тип наказания**__:', value='Mute', inline=False)
                        info_mute.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        info_mute.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        info_mute.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)
                        await info_logs.send(embed=info_mute)

                        info_mute_for_author = discord.Embed(title=f'Жалоба рассмотрена ✅', color=0x4B0082)
                        info_mute_for_author.add_field(name=f'__**Модерация успешно рассмотрела Вашу жалобу**__',
                                                       value=f'#{token}', inline=False)
                        info_mute_for_author.add_field(name=f'__**Решение:**__',
                                                       value=f'Пользователю {suspect.mention} был `временно ограничен доступ к общему чату`.',
                                                       inline=False)
                        info_mute_for_author.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await ctx.author.send(embed=info_mute_for_author)

                        info_mute_for_suspect = discord.Embed(title=f'На Вас была рассмотрена жалоба ‼', color=0x4B0082)
                        info_mute_for_suspect.add_field(name=f'__**Модерация рассмотрела жалобу на Вас**__',
                                                        value=f'#{token}', inline=False)
                        info_mute_for_suspect.add_field(name=f'__**Жалобу выдал**__:', value=f"{manager.mention}")
                        info_mute_for_suspect.add_field(name=f'__**Решение:**__',
                                                        value=f'Вам был `временно ограничен доступ к общему чату`.',
                                                        inline=False)
                        info_mute_for_suspect.add_field(name='ᅠ',
                                                        value=f'__**Пожалуйста...**__\n'
                                                              f'Постарайтесь впредь соблюдать правила поведения на сервере {ctx.guild.name}.\n'
                                                              f'Дружный коллектив - залог общего успеха!',
                                                        inline=False)
                        info_mute_for_suspect.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await suspect.send(embed=info_mute_for_suspect)
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
                                                           color=suspect.color)
                        embed_kick_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                     inline=False)
                        embed_kick_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_kick_success.add_field(name='__**Решение**__:',
                                                     value=f'Заявка **обработана** руководителем {manager.mention}.\n__**Наказание:**__ \n||Пользователь кикнут с сервера.||')
                        embed_kick_success.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        embed_kick_success.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        embed_kick_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                     inline=False)
                        embed_kick_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_kick_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_kick_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_kick_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)

                        info_kick = discord.Embed(title=f'Кик :wave:', color=0x4B0082)
                        info_kick.set_author(name=f"Автор жалобы: {ctx.author}", icon_url=ctx.author.avatar_url)
                        info_kick.add_field(name='__**Выдал(а)**__:', value=manager.mention, inline=False)
                        info_kick.add_field(name='__**Тип наказания**__:', value='Kick', inline=False)
                        info_kick.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        info_kick.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        info_kick.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)
                        await info_logs.send(embed=info_kick)

                        info_kick_for_author = discord.Embed(title=f'Жалоба рассмотрена ✅', color=0x4B0082)
                        info_kick_for_author.add_field(name=f'__**Модерация успешно рассмотрела Вашу жалобу**__',
                                                       value=f'#{token}', inline=False)
                        info_kick_for_author.add_field(name=f'__**Решение:**__',
                                                       value=f'Пользователь {suspect.mention} был `кикнут с сервера`.',
                                                       inline=False)
                        info_kick_for_author.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await ctx.author.send(embed=info_kick_for_author)

                        try:
                            for_kicked_user_embed = discord.Embed(color=0x8B0000,
                                                                  title="‼Вас выгнали с сервера\n Meta Peace Team®")
                            for_kicked_user_embed.add_field(name="__**Жалобу обработал управляющий**__:",
                                                            value=f"{manager}", inline=False)
                            for_kicked_user_embed.add_field(name="__**Причина пользовательской жалобы**__:",
                                                            value=str(reason), inline=False)
                            for_kicked_user_embed.add_field(name='ᅠ',
                                                            value=f'__**Пожалуйста...**__\n'
                                                                  f'Постарайтесь впредь соблюдать правила поведения на сервере {ctx.guild.name}.\n'
                                                                  f'Дружный коллектив - залог общего успеха!',
                                                            inline=False)
                            for_kicked_user_embed.set_image(
                                url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")
                            await suspect.send(embed=for_kicked_user_embed)
                            await suspect.send(
                                f'\n```Если Вы считаете, что это произошло по ошибке, пожалуйста, успокойтесь и сообщите об инциденте разработчику:```'
                                f'```fix\nDiscord: {ctx.guild.owner}\nVKontakte: {MetaPeace_owner_url["vk"]}\n```'
                                f'```Приносим глубочайшие сожаления.```')
                        except Exception:
                            await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                                description=f'❗️ Не удалось отправить личное сообщение пользователю {suspect}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                        finally:
                            await suspect.kick()
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
                                                          color=suspect.color)
                        embed_ban_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                    inline=False)
                        embed_ban_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_ban_success.add_field(name='__**Решение**__:',
                                                    value=f'Заявка **обработана** руководителем {manager.mention}.\n__**Наказание:**__ \n||Пользователь заблокирован на сервере.||')
                        embed_ban_success.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        embed_ban_success.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        embed_ban_success.add_field(name='__**Уникальный номер**__:', value='#' + str(token),
                                                    inline=False)
                        embed_ban_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                        embed_ban_success.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                        embed_ban_success.set_image(url=f"attachment://{files[0].filename}")
                        embed_ban_success.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)

                        info_ban = discord.Embed(title=f'Бан 🔒', color=0x4B0082)
                        info_ban.set_author(name=f"Автор жалобы: {ctx.author}", icon_url=ctx.author.avatar_url)
                        info_ban.add_field(name='__**Выдал(а)**__:', value=manager.mention, inline=False)
                        info_ban.add_field(name='__**Тип наказания**__:', value='Ban', inline=False)
                        info_ban.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        info_ban.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        info_ban.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                            icon_url=self.bot.user.avatar_url)
                        await info_logs.send(embed=info_ban)
                        info_ban_for_author = discord.Embed(title=f'Жалоба рассмотрена ✅', color=0x4B0082)
                        info_ban_for_author.add_field(name=f'__**Модерация успешно рассмотрела Вашу жалобу**__',
                                                      value=f'#{token}', inline=False)
                        info_ban_for_author.add_field(name=f'__**Решение:**__',
                                                      value=f'Пользователь {suspect.mention} был `перманентно заблокирован на сервере`.',
                                                      inline=False)
                        info_ban_for_author.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await ctx.author.send(embed=info_ban_for_author)
                        try:
                            for_banned_user_embed = discord.Embed(color=0x8B0000,
                                                                  title="‼Вас заблокировали на сервере\n Meta Peace Team®")  # Создание Embed'a
                            for_banned_user_embed.add_field(name="__**Жалобу обработал управляющий**__:",
                                                            value=f"{manager}", inline=False)
                            for_banned_user_embed.add_field(name="__**Причина пользовательской жалобы**__:",
                                                            value=str(reason), inline=False)
                            for_banned_user_embed.set_image(
                                url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")
                            await suspect.send(embed=for_banned_user_embed)
                            await suspect.send(
                                f'\n```Если Вы считаете, что это произошло по ошибке, пожалуйста, успокойтесь и сообщите об инциденте разработчику:```'
                                f'```fix\nDiscord: {ctx.guild.owner}\nVKontakte: {MetaPeace_owner_url["vk"]}\n```'
                                f'```Приносим глубочайшие сожаления.```')
                        except Exception:
                            await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                                description=f'❗️ Не удалось отправить личное сообщение пользователю {suspect}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                        finally:
                            await ctx.guild.ban(suspect)
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
                                                             color=suspect.color)
                        embed_report_success.add_field(name='__**Заявитель**__:', value=ctx.author.mention,
                                                       inline=False)
                        embed_report_success.add_field(name='__**Состояние**__:', value='Рассмотрена.', inline=False)
                        embed_report_success.add_field(name='__**Решение**__:',
                                                       value=f'Заявка **отклонена** руководителем {manager.mention}.\n__**Наказание:**__ \n||Не вынесено.||')
                        embed_report_success.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        embed_report_success.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
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
                        info_close_ticket = discord.Embed(title=f'Жалоба отклонена <:mark:816332017477615698>',
                                                          color=0x4B0082)
                        info_close_ticket.set_author(name=f"Автор жалобы: {ctx.author}", icon_url=ctx.author.avatar_url)
                        info_close_ticket.add_field(name='__**Рассмотрел(а)**__:', value=manager.mention, inline=False)
                        info_close_ticket.add_field(name='__**Тип наказания**__:', value='Отсутствует', inline=False)
                        info_close_ticket.add_field(name='__**Нарушитель**__:', value=suspect.mention, inline=False)
                        info_close_ticket.add_field(name='__**ID Нарушителя**__:', value=suspect.id, inline=False)
                        info_close_ticket.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await info_logs.send(embed=info_close_ticket)

                        info_close_ticket_for_author = discord.Embed(title=f'Жалоба рассмотрена ✅', color=0x4B0082)
                        info_close_ticket_for_author.add_field(
                            name=f'__**Модерация успешно рассмотрела Вашу жалобу**__',
                            value=f'#{token}', inline=False)
                        info_close_ticket_for_author.add_field(name=f'__**Решение:**__',
                                                               value=f'Наказание пользователю {suspect.mention} `не было вынесено`.',
                                                               inline=False)
                        info_close_ticket_for_author.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await ctx.author.send(embed=info_close_ticket_for_author)

                        info_close_ticket_for_suspect = discord.Embed(title=f'На Вас была рассмотрена жалоба ‼',
                                                                      color=0x4B0082)
                        info_close_ticket_for_suspect.add_field(name=f'__**Модерация рассмотрела жалобу на Вас**__',
                                                                value=f'#{token}', inline=False)
                        info_close_ticket_for_suspect.add_field(name=f'__**Жалобу выдал**__:',
                                                                value=f"{manager.mention}")
                        info_close_ticket_for_suspect.add_field(name=f'__**Решение:**__',
                                                                value=f'Наказание `не было вынесено`.',
                                                                inline=False)
                        info_close_ticket_for_suspect.add_field(name='ᅠ',
                                                                value=f'__**Пожалуйста...**__\n'
                                                                      f'Постарайтесь соблюдать правила поведения на сервере {ctx.guild.name}.\n'
                                                                      f'Дружный коллектив - залог общего успеха!',
                                                                inline=False)
                        info_close_ticket_for_suspect.set_footer(
                            text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                            icon_url=self.bot.user.avatar_url)
                        await suspect.send(embed=info_close_ticket_for_suspect)
                # Отправка эмбеда об ошибке, если не прикреплено изображение.

                except:
                    await load_variable.delete()
                    embed = discord.Embed(title="Жалоба ❌",
                                          color=suspect.color)
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