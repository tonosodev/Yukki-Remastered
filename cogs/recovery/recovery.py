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
        embed.set_thumbnail(url=ctx.author.avatar_url)

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
        msg = await ctx.reply(embed=embed)
        await msg.add_reaction("⭕")
        await msg.add_reaction("❌")
        await msg.add_reaction("♦")
        await msg.add_reaction("💥")
        try:
            react_user = await self.bot.wait_for('reaction_add',
                                                 check=lambda reaction, react: reaction.emoji == '⭕')
            if react_user:
                if ctx.message.author is True:
                    await ctx.send(ctx.message.author.id)
                    await msg.clear_reactions()
                else:
                    await ctx.send("User error")
            else:
                await ctx.send("Local error")
        except:
            await ctx.send("Global error")


def setup(bot):
    bot.add_cog(RecoveryCog(bot))
