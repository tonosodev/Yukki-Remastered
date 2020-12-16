import discord
from discord.ext import commands

from config import bot_initialize, bot_settings, kick_command_aliases, clear_command_aliases, add_role_command_aliases, \
    remove_role_command_aliases, ban_command_aliases, mute_command_aliases, unmute_command_aliases, \
    version_command_aliases


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=kick_command_aliases)
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member is None:
            await ctx.reply('Укажите в аргумент @пользователя, которого необходимо выгнать с сервера!', delete_after=10)
        elif member is ctx.message.author:
            await ctx.reply("Я не позволю Вам выгнать самого себя!\n", delete_after=10)
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
                print('[ERROR] Кажется я не могу писать в личку')
            finally:
                await member.kick()

    @commands.command(aliases=clear_command_aliases)
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def clear(self, ctx, amount: str = None):
        if not amount:
            await ctx.reply(
                "{}, Вы не ввели аргументы!\nТак что я сброшу кулдаун для этой команды, чтобы вы повторили попытку.".format(
                    ctx.author.mention), delete_after=10)
            self.clear.reset_cooldown(ctx)
        elif str:
            await ctx.message.delete()
            if int(amount) > 100:
                await ctx.reply(
                    "{}, Вы не можете очистить более сотни сообщений раз в 30 секунд!\nТак что я сброшу кулдаун для этой команды, чтобы вы повторили попытку.".format(
                        ctx.author.mention), delete_after=10)
                self.clear.reset_cooldown(ctx)

            elif int(amount) < 1:
                await ctx.reply(
                    "{}, Вы не можете очистить менее одного сообщения!\nТак что я сброшу кулдаун для этой команды, чтобы вы повторили попытку.".format(
                        ctx.author.mention), delete_after=10)
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
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    async def add_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member == None:
            await ctx.reply('Укажите в аргумент @пользователя и @роль, которую необходимо выдать пользователю!',
                            delete_after=10)
        elif role == None:
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
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    async def remove_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member == None:
            await ctx.reply('Укажите в аргумент @пользователя и @роль, у которую необходимо забрать роль!',
                            delete_after=10)
        elif role == None:
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
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    async def ban(self, ctx, member: discord.Member = None, reason=None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
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
                    print('[ERROR] Кажется я не могу писать в личку')
                finally:
                    await ctx.guild.ban(member)
            elif reason is not None:
                emb = discord.Embed(title='Блокировка 🔒', color=0x8B0000)
                emb.set_author(name=member.name, icon_url=member.avatar_url)
                emb.add_field(name='Выдана блокировка', value=' пользователю : {}'.format(member.mention))
                emb.set_footer(
                    text='Заблокирован управляющим {}'.format(ctx.author.name) + '\nПо причине: {}'.format(reason),
                    icon_url=ctx.author.avatar_url)
                await logs.send(embed=emb)
                try:
                    embed = discord.Embed(color=0x8B0000,
                                          title="‼Вас заблокировали на сервере\n Meta Peace Team®")  # Создание Embed'a
                    embed.set_image(
                        url="https://imagizer.imageshack.com/img923/8017/ohEwnl.gif")  # Устанавливаем картинку Embed'a
                    await member.send(embed=embed)
                    await member.send(
                        f'\n```Если блокировка произошла по ошибке, пожалуйста, успокойтесь и сообщите об этом администрации:``````fix\nDiscord: NeverMind#5885\nVKontakte: https://vk.com/devildesigner\n``````Приносим извинения за инцидент.```\nПричина блокировки: {reason}')
                except Exception:
                    print('[ERROR] Кажется, я не могу писать в личку')
                finally:
                    await ctx.guild.ban(member, reason=reason)

    @commands.command(aliases=mute_command_aliases)
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    async def mute(self, ctx, member: discord.Member = None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member == None:
            await ctx.reply('Укажите в аргумент @пользователя, которому необходимо ограничить доступ общения!',
                            delete_after=10)
        elif member == ctx.message.author:
            await ctx.reply("Я не позволю Вам заглушить самого себя!\n", delete_after=10)
        else:
            emb = discord.Embed(title='Мут 🔇', color=0x4B0082)
            emb.set_author(name=member.name, icon_url=member.avatar_url)
            emb.add_field(name='Выдан мут', value=' пользователю : {}'.format(member.mention))
            emb.set_footer(text='Выдан управляющим {}'.format(ctx.author.name),
                           icon_url=ctx.author.avatar_url)
            await logs.send(embed=emb)
            role = discord.utils.get(ctx.message.guild.roles, id=766366691466149898)
            # member_role = discord.utils.get(ctx.message.guild.roles, name='🎃Member')
            # await member.remove_roles(member_role)
            await member.add_roles(role)

    @commands.command(aliases=unmute_command_aliases)
    @commands.has_any_role(766233124681547776, 766231587104620554)  # Support, # Owner
    async def unmute(self, ctx, member: discord.Member = None):
        logs = self.bot.get_channel(bot_settings['log_channel'])
        if member == None:
            await ctx.reply("Укажите в аргумент @пользователя, которому необходимо вернуть доступ к каналам связи!",
                            delete_after=10)
        else:
            emb = discord.Embed(title='Анмут 🔉', color=0x6A5ACD)
            emb.set_author(name=member.name, icon_url=member.avatar_url)
            emb.add_field(name='Снят мут', value=' с пользователя : {}'.format(member.mention))
            emb.set_footer(text='Снят управляющим {}'.format(ctx.author.name),
                           icon_url=ctx.author.avatar_url)
            await logs.send(embed=emb)
            role = discord.utils.get(ctx.message.guild.roles, id=766366691466149898)
            # member_role = discord.utils.get(ctx.message.guild.roles, id='🎃Member')
            # await member.add_roles(member_role)
            await member.remove_roles(role)

    @commands.command(aliases=version_command_aliases)
    @commands.has_any_role(766233124681547776, 766231587104620554,
                           766293535832932392)  # Support, # Owner, #Head_tech-spec
    async def version(self, ctx):
        await ctx.message.delete()
        try:
            logo = open("logo.txt", "r", encoding="utf8")
            data = logo.read()
            await ctx.send(data, delete_after=10)
        except IOError:
            print(bot_initialize['logo_initialize_error'])


def setup(bot):
    bot.add_cog(ModerationCog(bot))
