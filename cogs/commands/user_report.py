import random
from io import BytesIO

import discord
from discord.ext import commands

from config import commands_permission, user_report_command_aliases, bot_settings


class UserReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=user_report_command_aliases)
    @commands.has_any_role(*commands_permission['user_report_command_permission'])
    async def report(self, ctx, member: discord.Member, *, reason: str = None):
        logs = self.bot.get_channel(bot_settings['report_channel'])
        if not member and reason is None:
            embed = discord.Embed(title="Жалоба 💬",
                                  description=f'{ctx.member.mention}, ОБЛИЗАТЕЛЬНО укажите пользователя и причну!',
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.add_field(name='Value Error', value='Укажите member, reason!')
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.reply(embed=embed, delete_after=15)
        else:
            files = []
            token = random.randint(0, 1000000)
            load_variable = await ctx.reply(f"{ctx.author.mention}, пожалуйста, подождите. . .")
            for file in ctx.message.attachments:
                fp = BytesIO()
                await file.save(fp)
                files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

            embed = discord.Embed(title="Жалоба 💬",
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.add_field(name='__**Выдана**__:', value=ctx.author.mention, inline=False)
            embed.add_field(name='__**Состояние**__:', value='На рассмотрении...', inline=False)
            embed.add_field(name='__**Нарушитель**__:', value=member.mention, inline=False)
            embed.add_field(name='__**ID Нарушителя**__:', value=member.id, inline=False)
            embed.add_field(name='__**Уникальный токен**__:', value=str(token), inline=False)
            embed.add_field(name='__**Причина**__:', value=reason, inline=False)

            embed.set_image(url=f"attachment://{files[0].filename}")
            msg = await logs.send(embed=embed, files=files)


            await load_variable.delete()
            await ctx.message.delete()
            warn_reaction = await msg.add_reaction("‼")
            mute_reaction = await msg.add_reaction("🔇")
            kick_reaction = await msg.add_reaction("🔥")
            ban_reaction = await msg.add_reaction("📛")
            close_ticket_reaction = await msg.add_reaction("❌")

            user_group = [*bot_settings['need_accept_report_roles']]
            # if ctx.user.guild == user_group:
            #    if mute_reaction:
            #        mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTED')
            #        await member.add_roles(mute_role, reason='Причина не указана.', atomic=True)


def setup(bot):
    bot.add_cog(UserReport(bot))
