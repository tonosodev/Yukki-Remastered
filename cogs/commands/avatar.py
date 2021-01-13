import discord
from discord.ext import commands

from config import avatar_command_aliases, commands_permission, bot_initialize


class UserAvatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=avatar_command_aliases)
    @commands.has_any_role(*commands_permission['avatar_command_permission'])
    async def avatar(self, ctx, member: discord.Member):
        msg = await ctx.reply("`Пожалуйста, подождите. . .`")
        if not member:
            member = ctx.author

        user = ctx.message.author if not member else member

        embed = discord.Embed(title=f'Аватар пользователя {member}', color=0xFF000)

        embed.set_image(url=user.avatar_url_as(format=None, size=4096))
        embed.set_author(icon_url='https://www.flaticon.com/premium-icon/icons/svg/2919/2919600.svg',
                         name='Участник | Аватар')
        embed.add_field(name="Запросил:", value=f"{ctx.author.mention}", inline=False)
        embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'], icon_url=self.bot.user.avatar_url)

        await msg.delete()
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(UserAvatar(bot))
