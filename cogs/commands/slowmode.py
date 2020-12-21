import discord

from discord.ext import commands

from config import slowmode_command_aliases, commands_permission


class SlowMode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=slowmode_command_aliases)
    @commands.has_any_role(*commands_permission['slowmode_command_permission'])
    async def slowmode(self, ctx, value: int = None):
        await ctx.message.delete()
        if value is None:
            embed = discord.Embed(title="SlowMode", description="Укажите количество секунд `>slowmode <int value>`",
                                  color=discord.Color.red())
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=10)
        elif value > 21600:
            embed = discord.Embed(title="SlowMode", description="Максимальное количество секунд: 21600",
                                  color=discord.Color.red())
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=10)
        else:
            channel = ctx.channel
            await channel.edit(slowmode_delay=value)

            if value == 1:
                sec = 'секунду'
            elif value == 2 or value == 3 or value == 4:
                sec = 'секунды'
            else:
                sec = 'секунд'

            logs = self.bot.get_channel(766218369279852554)
            embed = discord.Embed(title="SlowMode ⚔️",
                                  description=f"Установлен медленный режим на **{value}** {sec} в канале {ctx.channel.mention}",
                                  color=0x8A2BE2)
            embed.set_footer(text='Установлен управляющим {}'.format(ctx.author.name),
                             icon_url=ctx.author.avatar_url)
            log = open('log.txt', 'a', encoding='utf-8')
            log.write(f'[SLOWMODE] ' + f'Пользователь:\n')
            log.write(f'[SLOWMODE] ' + f'- ' + str(ctx.author.name) + '\n')
            log.write(f'[SLOWMODE] ' + f'Канал:\n')
            log.write(f'[SLOWMODE] ' + f'- ' + str(ctx.channel) + '\n')
            log.write(f'[SLOWMODE] ' + f'Время:\n')
            log.write(f'[SLOWMODE] ' + f'- ' + str(value) + 'сек.\n')
            log.write('...\n')
            log.close()
            await logs.send(embed=embed)


def setup(bot):
    bot.add_cog(SlowMode(bot))
