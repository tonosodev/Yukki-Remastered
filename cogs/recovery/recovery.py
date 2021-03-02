import asyncio
import os

import discord
from discord.ext import commands
from config import commands_permission, bot_initialize, bot_settings


class RecoveryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*commands_permission['recovery_command_permission'])
    async def recovery(self, ctx):
        system_log = self.bot.get_channel(bot_settings['system_log_channel'])

        await ctx.message.delete()

        member = discord.Member = "641398600727003197"
        embed_recovery = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
        embed_recovery.set_thumbnail(url=ctx.author.avatar_url)

        embed_recovery.add_field(name='WARNING:',
                                 value="Make sure you are going to make the right choice of action before use.\n"
                                       "**Attention!**\n"
                                       "*protocol: Self-Destruction was created in case of 'hopelessness'.* \n"
                                       "*Don't forget - this will destroy the entire project...*",
                                 inline=False)
        embed_recovery.add_field(name='Select action:', value=f'⭕ __**Reload**__\n'
                                                              f'❌ __**Shutdown**__\n'
                                                              f'========================\n'
                                                              f'♦ __**Recovery**__\n'
                                                              f'========================\n'
                                                              f'💥 __**protocol: Self-Destruction**__', inline=False)
        embed_recovery.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                  icon_url=self.bot.user.avatar_url)
        msg = await ctx.send(embed=embed_recovery)
        await msg.add_reaction("⭕")
        await msg.add_reaction("❌")
        await msg.add_reaction("♦")
        await msg.add_reaction("💥")

        def reload_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '⭕'

        try:
            await self.bot.wait_for('reaction_add', timeout=60.0, check=reload_reaction)
        except asyncio.TimeoutError:
            await msg.clear_reactions()
        else:
            embed_reload = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_reload.set_thumbnail(url=ctx.author.avatar_url)
            embed_reload.add_field(name="⭕ __**Reload**__", value=f"{ctx.author.mention}, начинаю перезапуск. . .")
            embed_reload.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                    icon_url=self.bot.user.avatar_url)

            embed_reload_complete = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_reload_complete.set_thumbnail(url=ctx.author.avatar_url)
            embed_reload_complete.add_field(name="⭕ __**Reload**__",
                                            value=f"{ctx.author.mention}, перезапуск завершен!", inline=False)
            embed_reload_complete.add_field(name="__**Совет**__:", value="для подробностей проверьте «Журнал Системы».",
                                            inline=False)
            embed_reload_complete.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                             icon_url=self.bot.user.avatar_url)

            await msg.edit(embed=embed_reload)
            await msg.clear_reactions()
            embed = discord.Embed(
                title="Перезапуск. . .",
                color=0x808080,
                timestamp=ctx.message.created_at
            )
            for filename in os.listdir("./cogs/administration_commands"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:

                        self.bot.unload_extension(f'cogs.administration_commands.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.administration_commands.{filename[:-3]}')
                        embed.add_field(
                            name=f"[administration_commands] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)

            for filename in os.listdir("./cogs/commands"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.commands.{filename[:-3]}")
                        self.bot.load_extension(f"cogs.commands.{filename[:-3]}")
                        embed.add_field(
                            name=f"[commands] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)

            for filename in os.listdir("./cogs/events"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        self.bot.unload_extension(f'cogs.events.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.events.{filename[:-3]}')
                        embed.add_field(
                            name=f"[events] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)

            for filename in os.listdir("./cogs/economy"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        self.bot.unload_extension(f'cogs.economy.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.economy.{filename[:-3]}')
                        embed.add_field(
                            name=f"[economy] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)

            for filename in os.listdir("./cogs/development"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        self.bot.unload_extension(f'cogs.development.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.development.{filename[:-3]}')
                        embed.add_field(
                            name=f"[development] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)

            for filename in os.listdir("./cogs/phrases"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        self.bot.unload_extension(f'cogs.phrases.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.phrases.{filename[:-3]}')
                        embed.add_field(
                            name=f"[phrases] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)

            for filename in os.listdir("./cogs/recovery"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        self.bot.unload_extension(f'cogs.recovery.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.recovery.{filename[:-3]}')
                        embed.add_field(
                            name=f"[recovery] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)
        await msg.edit(embed=embed_reload_complete, delete_after=15)
        print("\n[RECOVERY] System has been reloaded!\n")
        await system_log.send(embed=embed)

        ############################################################################################################

    """
        def shutdown_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '❌'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=shutdown_reaction)
        except asyncio.TimeoutError:
            pass
        else:
            await ctx.channel.send(ctx.message.author.mention + ", завершение работы...", delete_after=10)
            await msg.delete()

        ############################################################################################################

        def recovery_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '♦'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=recovery_reaction)
        except asyncio.TimeoutError:
            pass
        else:
            await ctx.channel.send(ctx.message.author.mention + ", начинаю процесс восстановления...\nПроверьте лог.",
                                   delete_after=10)
            await msg.delete()

        ############################################################################################################

        def protocol_reaction(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '💥'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=protocol_reaction)
        except asyncio.TimeoutError:
            pass
        else:
            await ctx.channel.send(
                ctx.message.author.mention + ", ты все же решился?\nПротокол самоуничтожения приведен в исполнение.\nВсего хорошего, папочка...",
                delete_after=10)
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

"""


def setup(bot):
    bot.add_cog(RecoveryCog(bot))
