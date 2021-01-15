import asyncio

import discord
from discord.ext import commands

from config import commands_permission, bot_initialize


class RecoveryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*commands_permission['recovery_command_permission'])
    async def recovery(self, ctx):
        embed = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='WARNING:',
                        value="Make sure you are going to make the right choice of action before use.\n"
                              "**Attention!**\n"
                              "*protocol: Self-Destruction was created in case of 'hopelessness'.* \n"
                              "*Don't forget - this will destroy the entire project...*",
                        inline=False)
        embed.add_field(name='Select action:', value=f'⭕ __**Reload**__\n'
                                                     f'❌ __**Shutdown**__\n'
                                                     f'========================\n'
                                                     f'♦ __**Recovery**__\n'
                                                     f'========================\n'
                                                     f'💥 __**protocol: Self-Destruction**__', inline=False)
        embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                         icon_url=self.bot.user.avatar_url)
        rec = await ctx.reply(embed=embed)
        await rec.add_reaction("⭕")
        await rec.add_reaction("❌")
        await rec.add_reaction("♦")
        await rec.add_reaction("💥")

        if rec.content.startswith('$thumb'):
            owner = ctx.message.author.id
            if ctx.user is owner:
                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) == '⭕'
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await ctx.message.delete()
                else:
                    await ctx.send('debug')
            else:
                pass


def setup(bot):
    bot.add_cog(RecoveryCog(bot))
