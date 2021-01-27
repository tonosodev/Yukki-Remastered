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
        await ctx.message.delete()
        member = discord.Member = "641398600727003197"
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
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("⭕")
        await msg.add_reaction("❌")
        await msg.add_reaction("♦")
        await msg.add_reaction("💥")

        def reload_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '⭕'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=reload_reaction)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            await ctx.channel.send(ctx.message.author.mention + ", перезапуск...", delete_after=10)
            await msg.delete()

        ############################################################################################################

        def shutdown_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '❌'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=shutdown_reaction)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            await ctx.channel.send(ctx.message.author.mention + ", завершение работы...", delete_after=10)
            await msg.delete()

        ############################################################################################################

        def recovery_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '♦'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=recovery_reaction)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            await ctx.channel.send(ctx.message.author.mention + ", начинаю процесс восстановления...\nПроверьте лог.", delete_after=10)
            await msg.delete()

        ############################################################################################################

        def protocol_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '💥'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=protocol_reaction)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            await ctx.channel.send(ctx.message.author.mention + ", ты все же решился?\nПротокол самоуничтожения приведен в исполнение.\nВсего хорошего, папочка...", delete_after=10)
            await msg.delete()



#        try:
#            react_user = await self.bot.wait_for('reaction_add',
#                                                 check=lambda reaction, react: reaction.emoji == '⭕')
#            if react_user is member:
#                await ctx.send(ctx.message.author.id)
#                await msg.clear_reactions()
#            else:
#                await ctx.send("`[REACTION EXCEPTION]`\n__**User not verified!**__")
#                await msg.clear_reactions()
#        finally:
#            await ctx.send("`[REACTION ERROR]`\n__**Global error...**__")
#            await msg.clear_reactions()


def setup(bot):
    bot.add_cog(RecoveryCog(bot))
