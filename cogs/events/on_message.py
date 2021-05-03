"""
Today is 4/13/2021
Session by: https://github.com/DevilDesigner
Create Time: 9:59 AM
This Class: on_message
"""
import asyncio
import time

from discord.ext import commands

from cogs.events.data.SwearWords import BAN_WORDS
from config import BAN_URL


class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        for word in message.content.split():
            if word.startswith('https://discord.gg/') or word.startswith('discord.gg/'):
                '''Если есть инвайт дискорда'''
                if not word.split('/')[-1] in [inv.code for inv in await message.guild.invites()]:
                    await message.delete()
                    await message.author.send('Я тебе сейчас попиарюсь нахуй, дебилоид...')
                return

            for link in BAN_URL:
                if link in word:
                    '''Если есть запрещенная ссылка'''
                    # await message.delete()
                    await message.reply('Запрещенные ссылки в чат')

                return

            for swear in BAN_WORDS:
                if swear in word:
                    '''Если есть запрещенные слова'''
                    await message.reply('НЕ РУГАЙСЯ ЗДЕСЬ, БЛЯДЕНЫШЬ!')

                return


def setup(bot):
    bot.add_cog(OnMessageCog(bot))
