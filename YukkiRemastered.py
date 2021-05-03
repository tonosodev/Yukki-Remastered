##### POWERED BY NeverMind#4082 #################################################
import discord
import os
import io

from discord.ext import commands
from discord.ext.commands import when_mentioned_or
from config import bot_settings, bot_initialize

queue = []
yukki = commands.Bot(
    command_prefix=when_mentioned_or(bot_settings['bot_prefix']),
    intents=discord.Intents.all(),
    help_command=None
)

# ----------------------------- #
#         YUKKI COGS            #
# ----------------------------- #
try:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.{filename[:-3]}')

    for filename in os.listdir('./cogs/commands'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.commands.{filename[:-3]}')

    for filename in os.listdir('./cogs/administration_commands'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.administration_commands.{filename[:-3]}')

    for filename in os.listdir('./cogs/events'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.events.{filename[:-3]}')

    for filename in os.listdir('./cogs/economy'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.economy.{filename[:-3]}')

    for filename in os.listdir('./cogs/development'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.development.{filename[:-3]}')

    for filename in os.listdir('cogs/phrases'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.phrases.{filename[:-3]}')

    for filename in os.listdir('./cogs/recovery'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.recovery.{filename[:-3]}')

    for filename in os.listdir('./cogs/embeds'):
        if filename.endswith('.py'):
            yukki.load_extension(f'cogs.embeds.{filename[:-3]}')
except:
    # noinspection PyUnboundLocalVariable
    print(
        f"\n##################################################\n\t\t\tWARNING!\nFILE >> {filename[:-3]} << " +
        bot_initialize['cog_load_error'] + "\n##################################################\n" + bot_initialize[
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
        return await ctx.reply(embed=discord.Embed(description=f'❗️ {ctx.author.name}, у Вас недостаточно прав!'),
                               delete_after=10)

    elif isinstance(error, commands.MissingRequiredArgument):
        return await ctx.reply(
            embed=discord.Embed(description=f'❗️ {ctx.author.name}, при выполнении команды ожидался аргумент.'),
            delete_after=10)

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(embed=discord.Embed(
            description=f"У Вас еще не прошел кулдаун на команду {ctx.command}!\nПодождите еще {error.retry_after:.2f} сек.!"),
            delete_after=5)
    else:
        if isinstance(error, UnboundLocalError):
            return "UnboundLocalError in file " + filename

        else:
            try:
                try:
                    msg = (f"[ERROR] Пользователь: {ctx.author.name}\n"
                           f"[ERROR] ID Пользователя: {ctx.author.id}\n"
                           f"[ERROR] Команда: {ctx.message.content}\n"
                           f"[ERROR] Сервер: {ctx.message.guild}\n"
                           f"[ERROR] Ошибка: {error}\n"
                           f". . .\n"
                           )

                    with io.open('log.txt', 'a', encoding='utf-8') as log:
                        print(
                            '*****************************\n'
                            'Запишу ошибку в файл ' + log.name +
                            '\n*****************************\n'
                        )
                        log.write(msg)
                except UnicodeEncodeError:
                    print(f"[ERROR] UnicodeEncodeError\n {error}")

            except FileNotFoundError:
                with io.open('log.txt', 'w', encoding='utf-8') as log:
                    print(
                        '#############################\n'
                        'Файл ' + log.name + ' не существует!\n'
                        'Создаю новый...\n'
                        '#############################\n'
                    )

        await yukki.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
            description=f'❗️ Ошибка при выполнении команды пользователя {ctx.author.mention}\n\n**`СЕРВЕР:`**\n{ctx.message.guild}\n**`КОМАНДА:`**\n{ctx.message.content}\n**`ОШИБКА:`**\n{error}'))

    raise error


# ----------------------------- #
#          YUKKI RUN            #
# ----------------------------- #
try:
    yukki.run(bot_settings['bot_token'])
except:
    print(bot_initialize['token_error'])
finally:
    print("Ошибка инициализации или иницализация завершения работы Yukki.")
