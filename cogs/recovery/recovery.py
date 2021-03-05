import asyncio
import os
import sys

import discord
from discord.ext import commands
from config import commands_permission, bot_initialize, bot_settings, user_report_reaction_permission_owner, \
    recovery_reaction_permission_head_tech, server_roles


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
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=lambda react, user:  user.id == ctx.author.id and react.message.id == msg.id and str(
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
            await msg.clear_reactions()
            embed_protocol = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_protocol.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol.add_field(name="💥 __**protocol: Self-Destruction**__",
                                     value=f"{ctx.author.mention}, начался процесс исполнения 'protocol: Self-Destruction'...")
            embed_protocol.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                                      icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol)
            await asyncio.sleep(3)
            embed_protocol_github_delete = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_github_delete.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_github_delete.add_field(name="💥 __**protocol: Self-Destruction**__",
                                                   value=f"Удаление проекта из репозиториев GitHub...")
            embed_protocol_github_delete.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_github_delete)
            await asyncio.sleep(8)
            embed_protocol_github_delete_complete = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_github_delete_complete.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_github_delete_complete.add_field(name="💥 __**protocol: Self-Destruction**__",
                                                            value=f"Удаление проекта из репозиториев GitHub...\nУспешно!")
            embed_protocol_github_delete_complete.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_github_delete_complete)
            await asyncio.sleep(3)
            embed_protocol_yukki_directory_delete = discord.Embed(title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_yukki_directory_delete.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_yukki_directory_delete.add_field(name="💥 __**protocol: Self-Destruction**__",
                                                            value=f"Удаление директории ./cogs и конфигурации проекта...")
            embed_protocol_yukki_directory_delete.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_yukki_directory_delete)
            await asyncio.sleep(6)
            embed_protocol_yukki_directory_delete_complete = discord.Embed(
                title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_yukki_directory_delete_complete.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_yukki_directory_delete_complete.add_field(name="💥 __**protocol: Self-Destruction**__",
                                                                     value=f"Удаление директории ./cogs и конфигурации проекта...\nУспешно!")
            embed_protocol_yukki_directory_delete_complete.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_yukki_directory_delete_complete)
            await asyncio.sleep(3)
            embed_protocol_shutdown = discord.Embed(
                title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_shutdown.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_shutdown.add_field(name="💥 __**protocol: Self-Destruction**__",
                                              value=f"Завершение работы перед удалением файла инициализации...")
            embed_protocol_shutdown.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_shutdown)
            await asyncio.sleep(5)
            embed_protocol_shutdown_complete = discord.Embed(
                title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_shutdown_complete.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_shutdown_complete.add_field(name="💥 __**protocol: Self-Destruction**__",
                                                       value=f"Завершение работы перед удалением файла инициализации...\nУспешно!")
            embed_protocol_shutdown_complete.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_shutdown_complete)
            await asyncio.sleep(3)
            embed_protocol_data_send = discord.Embed(
                title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_data_send.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_data_send.add_field(name="💥 __**protocol: Self-Destruction**__",
                                               value=f"Кэшируем данные запроса протокола и отправляем их разработчику для дальнейшего решения снятия Вашей управляющей роли...\nВпрочем, сделаю это сама.")
            embed_protocol_data_send.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_data_send)

            head_tech_guild_role = discord.utils.get(user.guild.roles, id=server_roles['tech.support_role'])
            try:
                await user.remove_roles(head_tech_guild_role)
                print(f"[RECOVERY] С пользователя {user} была снята роль {head_tech_guild_role}")
            except:
                print(f"[RECOVERY] Невозможно снять роль {head_tech_guild_role} с пользователя {user}.")

            await ctx.guild.owner.send(
                f"{user.mention} активировал протокол самоуничтожения Юкки.\nДля обеспечения безопасности с пользователя снята роль.")
            await asyncio.sleep(10)

            embed_protocol_goodbye = discord.Embed(
                title=f"{self.bot.user.name} | Control Panel")
            embed_protocol_goodbye.set_thumbnail(url=self.bot.user.avatar_url)
            embed_protocol_goodbye.add_field(name="💥 __**protocol: Self-Destruction**__",
                                             value=f"{user.mention} еще никогда не был так близко к совершению глупости, как в этот раз <:admin_face:769707992891129897>\nПротокол самоуничтожения отменен.\n`Пользователь не найден в списке доверенных лиц.`")
            embed_protocol_goodbye.set_footer(
                text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                icon_url=self.bot.user.avatar_url)
            await msg.edit(embed=embed_protocol_goodbye)
            await asyncio.sleep(10)
            await msg.delete()
        ############################################################################################################


def setup(bot):
    bot.add_cog(RecoveryCog(bot))
