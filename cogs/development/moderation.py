import discord
from discord.ext import commands
from config import bot_initialize, bot_settings, kick_command_aliases, clear_command_aliases, add_role_command_aliases, \
    remove_role_command_aliases, ban_command_aliases, mute_command_aliases, unmute_command_aliases, \
    version_command_aliases, unban_command_aliases, commands_permission, server_roles


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=kick_command_aliases)
    @commands.has_any_role(*commands_permission['kick_command_permission'])
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        logs = self.bot.get_channel(bot_settings['log_channel'])

        if member is None:
            await ctx.send(f'{ctx.author.mention}, укажите в аргумент @пользователя и "причину"!', delete_after=10)
            await ctx.message.delete()
        elif member is ctx.message.author:
            await ctx.send(f'{ctx.author.mention}, я не позволю Вам выгнать самого себя!', delete_after=10)
            await ctx.message.delete()
        else:
            if reason is None:
                emb = discord.Embed(title='Кик :wave:', colour=discord.Color.red())
                emb.set_author(name=member.name, icon_url=member.avatar_url)
                emb.add_field(name='Был кикнут', value='пользователь: {}'.format(member.mention))
                emb.set_footer(text='Кикнут с сервера руководителем {}'.format(ctx.author.name),
                               icon_url=ctx.author.avatar_url)
                await logs.send(embed=emb)

                try:
                    embed = discord.Embed(color=0x8B0000,
                                          title="‼Вас выгнали с сервера\n Meta Peace Team®")
                    embed.set_image(
                        url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")
                    await member.send(embed=embed)
                    await member.send(
                        f'\n```Если это произошло по ошибке, пожалуйста, успокойтесь и сообщите об этом администрации:``````fix\nDiscord: NeverMind#5885\nVKontakte: https://vk.com/devildesigner\n``````Приносим извинения за инцидент.```')
                except Exception:
                    await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                        description=f'❗️ Не удалось отправить личное сообщение пользователю {member}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                finally:
                    await member.kick()
                    await ctx.message.delete()

            elif reason is not None:
                emb = discord.Embed(title='Кик :wave:', colour=discord.Color.red())
                emb.set_author(name=member.name, icon_url=member.avatar_url)
                emb.add_field(name='Был кикнут', value='пользователь: {}'.format(member.mention))
                emb.set_footer(
                    text='Кикнут управляющим {}'.format(ctx.author.name) + '\nПо причине:\n{}'.format(reason),
                    icon_url=ctx.author.avatar_url)
                await logs.send(embed=emb)
                try:
                    embed = discord.Embed(color=0x8B0000,
                                          title="‼Вас выгнали с сервера\n Meta Peace Team®")
                    embed.set_image(
                        url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")
                    await member.send(embed=embed)
                    await member.send(
                        f'\n```Если это произошло по ошибке, пожалуйста, успокойтесь и сообщите об этом администрации:``````fix\nDiscord: NeverMind#5885\nVKontakte: https://vk.com/devildesigner\n``````Приносим извинения за инцидент.```\nПричина блокировки:\n**{reason}**')
                except Exception:
                    await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                        description=f'❗️ Не удалось отправить личное сообщение пользователю {member}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                finally:
                    await member.kick()
                    await ctx.message.delete()

    @commands.command(aliases=clear_command_aliases)
    @commands.has_any_role(*commands_permission['clear_command_permission'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def clear(self, ctx, amount: str = None):
        if not amount:
            await ctx.send(
                "{}, Вы не ввели аргументы!\nТак что я сброшу кулдаун для этой команды, чтобы вы повторили попытку.".format(
                    ctx.author.mention), delete_after=10)
            await ctx.message.delete()
            self.clear.reset_cooldown(ctx)
        elif str:
            if int(amount) > 100:
                await ctx.reply(
                    "{}, Вы не можете очистить более сотни сообщений раз в 30 секунд!\nТак что я сброшу кулдаун для этой команды, чтобы вы повторили попытку.".format(
                        ctx.author.mention), delete_after=10)
                await ctx.message.delete()
                self.clear.reset_cooldown(ctx)

            elif int(amount) < 1:
                await ctx.reply(
                    "{}, Вы не можете очистить менее одного сообщения!\nТак что я сброшу кулдаун для этой команды, чтобы вы повторили попытку.".format(
                        ctx.author.mention), delete_after=10)
                await ctx.message.delete()
                self.clear.reset_cooldown(ctx)

            else:
                if amount is None:
                    await ctx.reply('Укажите в аргумент количество сообщений, которые необходимо удалить!',
                                    delete_after=10)
                else:
                    await ctx.channel.purge(limit=int(amount))
                    emb = discord.Embed(title='Очистка чата',
                                        description=f'Управляющий {ctx.author.mention} очистил чат на ' + amount + ' сообщений!')
                    await ctx.send(embed=emb, delete_after=10)

    @commands.command(aliases=add_role_command_aliases)
    @commands.has_any_role(*commands_permission['add_role_command_permission'])
    async def add_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member is None:
            await ctx.reply('Укажите в аргумент @пользователя и @роль, которую необходимо выдать пользователю!',
                            delete_after=10)
        elif role is None:
            await ctx.reply('Укажите в аргумент @пользователя и @роль, которую необходимо выдать пользователю!',
                            delete_after=10)
        else:
            await member.add_roles(role)
            emb = discord.Embed(title='Выдача роли ❇️', color=0x00FF7F)
            emb.set_author(name=member.name, icon_url=member.avatar_url)
            emb.add_field(name='Выдана роль {}'.format(role), value=' пользователю : {}'.format(member.mention))
            emb.set_footer(text='Выдана управляющим {}'.format(ctx.author.name),
                           icon_url=ctx.author.avatar_url)
            await logs.send(embed=emb)

    @commands.command(aliases=remove_role_command_aliases)
    @commands.has_any_role(*commands_permission['remove_role_command_permission'])
    async def remove_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member is None:
            await ctx.reply('Укажите в аргумент @пользователя и @роль, у которую необходимо забрать роль!',
                            delete_after=10)
        elif role is None:
            await ctx.reply('Укажите в аргумент @пользователя и @роль, у которого необходимо забрать роль!',
                            delete_after=10)
        else:
            await member.remove_roles(role)
            emb = discord.Embed(title='Снятие роли ❎', color=0x008000)
            emb.set_author(name=member.name, icon_url=member.avatar_url)
            emb.add_field(name='Снята роль {}'.format(role), value='с пользователя : {}'.format(member.mention))
            emb.set_footer(text='Снята управляющим {}'.format(ctx.author.name),
                           icon_url=ctx.author.avatar_url)
            await logs.send(embed=emb)

    @commands.command(aliases=ban_command_aliases)
    @commands.has_any_role(*commands_permission['ban_command_permission'])
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        await ctx.message.delete()
        if member is None:
            await ctx.reply(
                'Укажите в аргумент @пользователя, количество дней блокировки и причину, для пользователя, которому необходимо ограничить доступ к серверу!',
                delete_after=10)
        elif member is ctx.message.author:
            await ctx.reply("Я не позволю Вам заблокировать самого себя!\n", delete_after=10)
        else:
            if reason is None:
                emb = discord.Embed(title='Бан 🔒', color=0x8B0000)
                emb.set_author(name=member.name, icon_url=member.avatar_url)
                emb.add_field(name='Был заблокирован', value=' пользователь: {}'.format(member.mention))
                emb.set_footer(text='Заблокирован управляющим {}'.format(ctx.author.name),
                               icon_url=ctx.author.avatar_url)
                await logs.send(embed=emb)
                try:
                    embed = discord.Embed(color=0x8B0000,
                                          title="‼Вас заблокировали на сервере\n Meta Peace Team®")  # Создание Embed'a
                    embed.set_image(
                        url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")  # Устанавливаем картинку Embed'a
                    await member.send(embed=embed)
                    await member.send(
                        f'\n```Если блокировка произошла по ошибке, пожалуйста, успокойтесь и сообщите об этом администрации:``````fix\nDiscord: NeverMind#5885\nVKontakte: https://vk.com/devildesigner\n``````Приносим извинения за инцидент.```')
                except Exception:
                    await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                        description=f'❗️ Не удалось отправить личное сообщение пользователю {member}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
                finally:
                    await ctx.guild.ban(member)
            elif reason is not None:
                emb = discord.Embed(title='Блокировка 🔒', color=0x8B0000)
                emb.set_author(name=member.name, icon_url=member.avatar_url)
                emb.add_field(name='Выдана блокировка', value=' пользователю : {}'.format(member.mention))
                emb.set_footer(
                    text='Заблокирован управляющим {}'.format(ctx.author.name) + '\nПо причине:\n{}'.format(reason),
                    icon_url=ctx.author.avatar_url)
                await logs.send(embed=emb)
            try:
                embed = discord.Embed(color=0x8B0000,
                                      title="‼Вас заблокировали на сервере\n Meta Peace Team®")  # Создание Embed'a
                embed.set_image(
                    url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")  # Устанавливаем картинку Embed'a
                await member.send(embed=embed)
                await member.send(
                    f'\n```Если блокировка произошла по ошибке, пожалуйста, успокойтесь и сообщите об этом администрации:``````fix\nDiscord: NeverMind#5885\nVKontakte: https://vk.com/devildesigner\n``````Приносим извинения за инцидент.```\nПричина блокировки:\n**{reason}**')
            except Exception:
                await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                    description=f'❗️ Не удалось отправить личное сообщение пользователю {member}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n'))
            finally:
                await ctx.guild.ban(member, reason=reason)

    @commands.command(aliases=unban_command_aliases)
    @commands.has_any_role(*commands_permission['unban_command_permission'])
    async def unban(self, ctx, member):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user

            await ctx.guild.unban(user)
            emb = discord.Embed(title='Анбан :unlock:', color=0xFA8072)
            emb.add_field(name='Был разблокирован', value='пользователь: {}'.format(user))
            emb.set_footer(text='Разблокирован управляющим {}'.format(ctx.author.name),
                           icon_url=ctx.author.avatar_url)
            await logs.send(embed=emb)
            return

    @commands.command(aliases=mute_command_aliases)
    @commands.has_any_role(*commands_permission['mute_command_permission'])
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        member_role = discord.utils.get(ctx.message.guild.roles, id=server_roles['member_role'])
        mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTED')
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if not mute_role:
            mute_role = await ctx.guild.create_role(name='MUTED',
                                                    permissions=discord.Permissions(send_messages=False),
                                                    color=discord.Color.light_grey())
            for i in ctx.guild.channels:
                await i.set_permissions(mute_role, send_messages=False)
            mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTED')

        elif mute_role in member.roles:
            emb = discord.Embed(title=f'Мут 🔇', description=f'Участник {member.mention} уже имеет мут.',
                                color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)


        elif member.id == ctx.guild.owner.id:
            emb = discord.Embed(title=f'Мут 🔇', description='Невозможно заглушить владельца гильдии!',
                                color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif member.id == ctx.guild.me.id:
            emb = discord.Embed(title=f'Мут 🔇', description='Невозможно заглушить этого участника!', color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif ctx.author.top_role.position < member.top_role.position:
            emb = discord.Embed(title=f'Мут 🔇', description='Невозможно заглушить участника с ролью выше вашей!',
                                color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif member.id == ctx.author.id:
            emb = discord.Embed(title=f'Мут 🔇', description='Невозможно заглушить самого себя!',
                                color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif member.top_role > ctx.guild.me.top_role:
            emb = discord.Embed(title=f'Мут 🔇', description='Невозможно заглушить участника с ролью выше моей!',
                                color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif not reason:
            await ctx.message.delete()
            emb = discord.Embed(title=f'Мут 🔇', color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.add_field(name='__**Выдал(а)**__:', value=ctx.author.mention, inline=False)
            emb.add_field(name='__**Тип наказания**__:', value='Mute', inline=False)
            emb.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
            emb.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
            emb.add_field(name='__**Причина**__:', value='Не указана.', inline=False)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await member.remove_roles(member_role)
            await member.add_roles(mute_role, reason='Причина не указана.', atomic=True)
            await logs.send(embed=emb)


        else:
            await ctx.message.delete()
            emb = discord.Embed(title=f'Мут 🔇', color=0x4B0082)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.add_field(name='__**Выдал(а)**__:', value=ctx.author.mention, inline=False)
            emb.add_field(name='__**Тип наказания**__:', value='Mute', inline=False)
            emb.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
            emb.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
            emb.add_field(name='__**Причина**__:', value=reason, inline=False)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await member.remove_roles(member_role)
            await member.add_roles(mute_role, reason=reason, atomic=True)
            await logs.send(embed=emb)

    @commands.command(aliases=unmute_command_aliases)
    @commands.has_any_role(*commands_permission['unmute_command_permission'])
    async def unmute(self, ctx, member: discord.Member = None, *, reason: str = None):
        mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTED')
        member_role = discord.utils.get(ctx.message.guild.roles, id=server_roles['member_role'])
        logs = self.bot.get_channel(bot_settings['log_channel'])

        if member.top_role > ctx.guild.me.top_role:
            emb = discord.Embed(title=f'Анмут 🔉',
                                description=f'Роль участника {member.mention} выше Вашей!',
                                color=0x6A5ACD)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif mute_role.position > ctx.guild.me.top_role.position:
            emb = discord.Embed(title=f'Анмут 🔉', description=f'Роль мута выше Вашей!', color=0x6A5ACD)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=emb, delete_after=15)

        elif reason is None:
            await ctx.message.delete()
            await member.remove_roles(mute_role)
            await member.add_roles(member_role, reason='Причина не указана.', atomic=True)
            emb = discord.Embed(title=f'Анмут 🔉',
                                description=f'Снят мут с пользователя {member.mention}.\n**Причина:** Не указана.',
                                color=0x6A5ACD)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)
        else:
            await ctx.message.delete()
            await member.remove_roles(mute_role)
            await member.add_roles(member_role, reason=reason, atomic=True)
            emb = discord.Embed(title=f'Анмут 🔉',
                                description=f'Снят мут с пользователя {member.mention}.\n**Причина:** {reason}',
                                color=0x6A5ACD)
            emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

    @commands.command(aliases=version_command_aliases)
    @commands.has_any_role(*commands_permission['version_command_permission'])
    async def version(self, ctx):
        try:
            logo = open("logo.txt", "r", encoding="utf8")
            data = logo.read()
            logo.close()
            await ctx.send(data, delete_after=10)
        except IOError:
            print(bot_initialize['logo_initialize_error'])
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(ModerationCog(bot))
