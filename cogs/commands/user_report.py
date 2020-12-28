import discord
from discord.ext import commands
import random
from io import BytesIO
from config import commands_permission, user_report_command_aliases, bot_settings


class UserReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=user_report_command_aliases)
    @commands.has_any_role(*commands_permission['user_report_command_permission'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def report(self, ctx, member: discord.Member = None, *, reason=None):
        logs = self.bot.get_channel(bot_settings['report_channel'])
        load_variable = await ctx.reply(f"{ctx.author.mention}, пожалуйста, подождите. . .")
        token = random.randint(0, 999999999)
        if member is None:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Перед отправкой соблюдайте следующие пункты**__:',
                            value='- Укажите @пользователя и "причину"'
                                  '\n- Прикрепите снимок нарушения со стороны пользователя к сообщению', inline=False)
            embed.add_field(name="__**Совет**__:",
                            value='Для обработки жалобы не прикрепляйте изображения большого размера!', inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.add_field(name='__**Пример правильного заполнения**__:', value="*см. во вложении.", inline=False)
            embed.set_image(
                url='https://sun9-48.userapi.com/impg/xvWDgPDXtJlEXP2NeWY6E5zGld0WUxc5JE6Pvw/s6FniY0Yz0M.jpg?size=594x595&quality=96&proxy=1&sign=eb265d60619fb69cd078a2e3816a1c6c&type=album')
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        elif member is ctx.message.author:
            await load_variable.delete()
            embed = discord.Embed(title="Жалоба ❌",
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
            embed.add_field(name='__**Причина**__:', value="Вы не можете просто взять, и пожаловаться на самого себя..."
                                                           "\nОставьте это другим пользователям!", inline=False)
            embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            self.report.reset_cooldown(ctx)

        else:
            if reason is None:
                await load_variable.delete()
                embed = discord.Embed(title="Жалоба ❌",
                                      color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                   random.randint(1, 255)))
                embed.add_field(name='__**Ошибка при отправке жалобы**__:', value=f'{ctx.author.mention}', inline=False)
                embed.add_field(name='__**Причина**__:', value="Не указана причина жалобы."
                                                               "\nПожалуйста, укажите причину репорта после упоминания пользователя!",
                                inline=False)
                embed.add_field(name="__**Совет**__:",
                                value=f"Пропишите «{bot_settings['bot_prefix']}репорт» для вывода информации по заполнению формы!",
                                inline=False)
                embed.add_field(name='__**Действие**__:', value='Задержка на использование команды обнулена.')
                embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                                 icon_url=self.bot.user.avatar_url)
                await ctx.reply(embed=embed)
                self.report.reset_cooldown(ctx)

            elif reason is not None:
                try:
                    files = []
                    for file in ctx.message.attachments:
                        fp = BytesIO()
                        await file.save(fp)
                        files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

                    embed = discord.Embed(title="Жалоба 💬",
                                          color=discord.Color.from_rgb(random.randint(1, 255),
                                                                       random.randint(1, 255),
                                                                       random.randint(1, 255)))
                    embed.add_field(name='__**Выдана**__:', value=ctx.author.mention, inline=False)
                    embed.add_field(name='__**Состояние**__:', value='На рассмотрении...', inline=False)
                    embed.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                    embed.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
                    embed.add_field(name='__**Уникальный номер**__:', value='#' + str(token), inline=False)
                    embed.add_field(name='__**Причина**__:', value=reason, inline=False)
                    embed.add_field(name='__**Вложение**__:', value='Прикреплено.', inline=False)

                    embed.set_image(url=f"attachment://{files[0].filename}")
                    embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                                     icon_url=self.bot.user.avatar_url)

                    await load_variable.delete()
                    await ctx.message.delete()

                    embed_success = discord.Embed(title="Жалоба 💬",
                                                  color=discord.Color.from_rgb(random.randint(1, 255),
                                                                               random.randint(1, 255),
                                                                               random.randint(1, 255)))
                    embed_success.add_field(name='__**В обработку принята жалоба**__', value='#' + str(token),
                                            inline=False)
                    embed_success.add_field(name='__**Выдана**__:', value=ctx.author.mention, inline=False)
                    embed_success.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
                    embed_success.add_field(name='__**Причина**__:', value=reason, inline=False)
                    embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                                     icon_url=self.bot.user.avatar_url)

                    await ctx.send(embed=embed_success, delete_after=15)

                    msg = await logs.send(embed=embed, files=files)
                    warn_reaction = await msg.add_reaction("‼")
                    mute_reaction = await msg.add_reaction("🔇")
                    kick_reaction = await msg.add_reaction("🔥")
                    ban_reaction = await msg.add_reaction("📛")
                    close_ticket_reaction = await msg.add_reaction("❌")


                except:
                    await load_variable.delete()
                    embed = discord.Embed(title="Жалоба ❌",
                                          color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                       random.randint(1, 255)))
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
                    embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                                     icon_url=self.bot.user.avatar_url)
                    await ctx.reply(embed=embed)

                    self.report.reset_cooldown(ctx)

                finally:
                    pass


def setup(bot):
    bot.add_cog(UserReport(bot))
