import discord
import os

from discord.ext import commands
from discord.ext.commands import when_mentioned_or
from pymongo import MongoClient
from config import bot_settings, mongo_db, bot_initialize

queue = []
PREFIX = bot_settings['bot_prefix']
TOKEN = bot_settings['bot_token']
yukki = commands.Bot(command_prefix=when_mentioned_or(bot_settings['bot_prefix']), intents=discord.Intents.all())
yukki.remove_command("help")

error_logs = yukki.get_channel(bot_settings['system_log_channel'])


# ----------------------------- #
#         YUKKI COGS            #
# ----------------------------- #
@yukki.command()  # Load command
async def load(ctx, extensions):
    yukki.load_extension(f'cogs.{extensions}')
    await ctx.send("Yukki loaded success!")


@yukki.command()  # Unload command
@commands.has_permissions(administrator=True)
async def unload(ctx, extensions):
    yukki.unload_extension(f'cogs.{extensions}')
    await ctx.send("Yukki unloaded success!")


@yukki.command()  # Reload command
async def reload(ctx, extensions):
    yukki.unload_extension(f'cogs.{extensions}')
    yukki.load_extension(f'cogs.{extensions}')
    await ctx.send("Yukki reloaded success!")


# @yukki.command()
# async def welcome(ctx):
#    emb = discord.Embed(color=0xFF69B4)
#    emb.set_image(url="https://imagizer.imageshack.com/v2/xq90/924/94Box3.png")
#    await ctx.send(embed=emb)
#    a = await ctx.send(
#        "```fix\nПройдите быструю верификацию кликнув на эмодзи под данным сообщением, чтобы получить доступ к основному функционалу сервера!\n```")
#    await a.add_reaction('<a:verify:768537178221051944>')


try:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.{filename[:-3]}')

    for filename in os.listdir('./cogs/commands'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.commands.{filename[:-3]}')

    for filename in os.listdir('./cogs/events'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.events.{filename[:-3]}')

    # for filename in os.listdir('./cogs/phrases'):
    #    if filename.endswith('.py'):
    #        yukki.load_extension(f'cogs.phrases.{filename[:-3]}')

    for filename in os.listdir('./cogs/development'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.development.{filename[:-3]}')
except:
    print(
        f"\n##################################################\nFile '{filename[:-3]}' " + bot_initialize[
            'cog_load_error'] + "\n##################################################\n" + bot_initialize[
            'copyright_message'])


# -------------------------------#
#         Yukki Exceptions       #
# -------------------------------#
@yukki.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.reply(embed=discord.Embed(
            description=f'❗️ {ctx.author.mention}, команда не найдена!\nПропишите " ' + bot_settings[
                'bot_prefix'] + 'помощь ", для вывода доступных возможностей'), delete_after=10)

    elif isinstance(error, commands.MissingPermissions) or isinstance(error, discord.Forbidden) or isinstance(error,
                                                                                                              commands.MissingRole) or \
            isinstance(error, commands.MissingAnyRole):
        return await ctx.reply(embed=discord.Embed(description=f'❗️ {ctx.author.name}, у Вас недостаточно прав!'), delete_after=10)

    #elif isinstance(error, commands.MissingRequiredArgument):
    #    return await ctx.reply(
    #        embed=discord.Embed(description=f'❗️ {ctx.author.name}, при выполнении команды ожидался аргумент.'), delete_after=10)

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(embed=discord.Embed(
            description=f"У Вас еще не прошел кулдаун на команду {ctx.command}!\nПодождите еще {error.retry_after:.2f} сек.!"), delete_after=5)
    else:
        if "Command raised an exception: UnboundLocalError:" in str(error):
            return

        else:
            try:
                log = open('log.txt', 'a', encoding='cp1251')
                print(
                    '*****************************\nЗапишу ошибку в файл ' + log.name + '\n*****************************\n')
                log.write(f"[ERROR] " + f"Пользователь: {ctx.author.name}\n")
                log.write(f"[ERROR] " + f"Команда: {ctx.message.content}\n")
                log.write(f"[ERROR] " + f"Сервер:  {ctx.message.guild}\n")
                log.write(f"[ERROR] " + f"Ошибка:  {error}\n")
                log.write("...\n")
                log.close()
            except FileNotFoundError:
                log = open('log.txt', 'w', encoding='cp1251')
                print(
                    '#############################\nФайл ' + log.name + ' не существует!\nСоздаю новый...\n#############################\n')
                log.write(f"[ERROR] " + f"Пользователь: {ctx.author.name}\n")
                log.write(f"[ERROR] " + f"Команда: {ctx.message.content}\n")
                log.write(f"[ERROR] " + f"Сервер:  {ctx.message.guild}\n")
                log.write(f"[ERROR] " + f"Ошибка:  {error}\n")
                log.write("...\n")
                log.close()

            await yukki.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                description=f'❗️ Ошибка при выполнении команды пользователя {ctx.author.mention}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n**`КОМАНДА:`**\n{ctx.message.content}\n**`ОШИБКА:`**\n{error}'))
            #raise error

# ----------------------------- #
#          YUKKI RUN            #
# ----------------------------- #
try:
    yukki.run(bot_settings['bot_token'])
except:
    print(bot_initialize['token_error'])
finally:
    pass
