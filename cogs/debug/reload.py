# @yukki.command()
# async def welcome(ctx):
#    emb = discord.Embed(color=0xFF69B4)
#    emb.set_image(url="https://imagizer.imageshack.com/v2/xq90/924/94Box3.png")
#    await ctx.send(embed=emb)
#    a = await ctx.send(
#        "```fix\nПройдите быструю верификацию кликнув на эмодзи под данным сообщением, чтобы получить доступ к основному функционалу сервера!\n```")
#    await a.add_reaction('<a:verify:768537178221051944>')


@yukki.command(
    name='reload', description="Reload all/one of the bots cogs!"
)
@commands.has_any_role(*commands_permission['reload_command_permission'])
async def reload(ctx, cog=None):
    await ctx.message.delete()
    error_logs = yukki.get_channel(bot_settings['system_log_channel'])
    if not cog:
        # No cog, means we reload all cogs
        async with ctx.typing():
            embed = discord.Embed(
                title="Перезапуск. . .",
                color=0x808080,
                timestamp=ctx.message.created_at,
            )
            for filename in os.listdir("./cogs/administration_commands"):
                if filename.endswith(".py") and not filename.startswith("_"):
                    try:
                        yukki.unload_extension(f'cogs.administration_commands.{filename[:-3]}')
                        yukki.load_extension(f'cogs.administration_commands.{filename[:-3]}')
                        embed.add_field(
                            name=f"[administration_commands] Перезапущено: `{filename}`",
                            value=' | ',
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
                        yukki.unload_extension(f"cogs.commands.{filename[:-3]}")
                        yukki.load_extension(f"cogs.commands.{filename[:-3]}")
                        embed.add_field(
                            name=f"[commands] Перезапущено: `{filename}`",
                            value=' | ',
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
                        yukki.unload_extension(f'cogs.events.{filename[:-3]}')
                        yukki.load_extension(f'cogs.events.{filename[:-3]}')
                        embed.add_field(
                            name=f"[events] Перезапущено: `{filename}`",
                            value=' | ',
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
                        yukki.unload_extension(f'cogs.economy.{filename[:-3]}')
                        yukki.load_extension(f'cogs.economy.{filename[:-3]}')
                        embed.add_field(
                            name=f"[economy] Перезапущено: `{filename}`",
                            value=' | ',
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
                        yukki.unload_extension(f'cogs.development.{filename[:-3]}')
                        yukki.load_extension(f'cogs.development.{filename[:-3]}')
                        embed.add_field(
                            name=f"[development] Перезапущено: `{filename}`",
                            value=' | ',
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
                        yukki.unload_extension(f'cogs.phrases.{filename[:-3]}')
                        yukki.load_extension(f'cogs.phrases.{filename[:-3]}')
                        embed.add_field(
                            name=f"[phrases] Перезапущено: `{filename}`",
                            value=' | ',
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
                        yukki.unload_extension(f'cogs.recovery.{filename[:-3]}')
                        yukki.load_extension(f'cogs.recovery.{filename[:-3]}')
                        embed.add_field(
                            name=f"[recovery] Перезапущено: `{filename}`",
                            value=' | ',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Ошибка при загрузке файла: `{filename}`",
                            value=str(e),
                            inline=False
                        )
                    await asyncio.sleep(0.5)
            await error_logs.send(embed=embed)

