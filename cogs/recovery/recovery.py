import asyncio
import os
import sys

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
        embed_recovery.set_thumbnail(url=self.bot.user.avatar_url)

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

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=lambda react,
                                                                                                user: user.id == ctx.author.id and react.message.id == msg.id and str(
                react.emoji) in ["⭕", "❌", "♦", "💥"])
        except asyncio.TimeoutError:
            return await msg.clear_reactions()

            #
            # RELOAD REACTION
            #

        if str(reaction.emoji) == "⭕":
            embed_reload = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_reload.set_thumbnail(url=self.bot.user.avatar_url)
            embed_reload.add_field(name="⭕ __**Reload**__", value=f"{ctx.author.mention}, начинаю перезапуск . . .")
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
            embed_reloading = discord.Embed(
                title="Перезапуск. . .",
                color=0x808080,
                timestamp=ctx.message.created_at
            )
            for filename in os.listdir("./cogs/administration_commands"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:

                        self.bot.unload_extension(f'cogs.administration_commands.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.administration_commands.{filename[:-3]}')
                        embed_reloading.add_field(
                            name=f"[administration_commands] Перезапущено: {filename}",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
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
                        embed_reloading.add_field(
                            name=f"[commands] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
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
                        embed_reloading.add_field(
                            name=f"[events] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
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
                        embed_reloading.add_field(
                            name=f"[economy] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
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
                        embed_reloading.add_field(
                            name=f"[development] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
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
                        embed_reloading.add_field(
                            name=f"[phrases] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
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
                        embed_reloading.add_field(
                            name=f"[recovery] Перезапущено:",
                            value=f'`{filename}`',
                            inline=False
                        )
                    except Exception as e:
                        embed_reloading.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)
            await msg.edit(embed=embed_reload_complete, delete_after=15)
            print("\n[RECOVERY] System has been reloaded!\n")
            await system_log.send(embed=embed_reloading)

            #
            # SHUTDOWN REACTION
            #

        elif str(reaction.emoji) == "❌":
            embed_shutdown = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_shutdown.set_thumbnail(url=self.bot.user.avatar_url)
            embed_shutdown.add_field(name="❌ __**Shutdown**__",
                                     value=f"{ctx.author.mention}, завершение работы . . .\nПри необходимости запустите систему в ручном режиме.")
            embed_shutdown.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                      icon_url=self.bot.user.avatar_url)

            await msg.edit(embed=embed_shutdown)
            await msg.clear_reactions()

            embed_shutdown = discord.Embed(
                title="Юкки успешно ушла спатки!",
                description="Ну всё, теперь запуск только ручками...",
                color=0x808080,
                timestamp=ctx.message.created_at
            )
            await system_log.send(embed=embed_shutdown)
            sys.exit(0)

            #
            # RECOVERY REACTION
            #

        elif str(reaction.emoji) == "♦":
            embed_recovery = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_recovery.set_thumbnail(url=self.bot.user.avatar_url)
            embed_recovery.add_field(name="♦ __**Recovery**__",
                                     value=f"{ctx.author.mention}, начался процесс восстановления конфигурации системы. . .")
            embed_recovery.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                      icon_url=self.bot.user.avatar_url)

            embed_recovery_complete = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_recovery_complete.set_thumbnail(url=ctx.author.avatar_url)
            embed_recovery_complete.add_field(name="♦ __**Recovery**__",
                                              value=f"{ctx.author.mention}, восстановление завершено!", inline=False)
            embed_recovery_complete.add_field(name="__**Совет**__:",
                                              value="для подробностей проверьте «Журнал Системы».",
                                              inline=False)
            embed_recovery_complete.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                               icon_url=self.bot.user.avatar_url)

            await msg.edit(embed=embed_recovery)
            await msg.clear_reactions()

            embed_recovering = discord.Embed(
                title="Восстановление конфигурации системы . . .",
                description="Файл config.py успешно восстановлен!",
                color=0x808080,
                timestamp=ctx.message.created_at
            )
            await system_log.send(embed=embed_recovering)

            #
            # PROTOCOL REACTION
            #

        elif str(reaction.emoji) == "💥":
            embed_protocol = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_protocol.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol.add_field(name="💥 __**protocol: Self-Destruction**__",
                                     value=f"{ctx.author.mention}, начался процесс исполнения 'protocol: Self-Destruction' . . .")
            embed_protocol.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                      icon_url=self.bot.user.avatar_url)

            await msg.edit(embed=embed_protocol)


############################################################################################################


def setup(bot):
    bot.add_cog(RecoveryCog(bot))
