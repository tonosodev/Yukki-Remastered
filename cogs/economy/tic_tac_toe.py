"""
Today is 3/16/2021
Session by: https://github.com/DevilDesigner
Create Time: 2:49 PM
This Class: tic_tac_toe
"""
import random
import time

import discord
from discord.ext import commands
import asyncio
from loguru import logger
import emoji

from config import tic_tac_toe_command_aliases, mini_games


class TicTacToe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.playing = []

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog TicTacToe loaded!")

    def GetNextTurn(self, member1, member2, now):
        if now == member1.id:
            return member2.id

        return member1.id

    def GetKeyByValue(self, dict, value):
        for k, v in dict.items():
            if value == v:
                return k

        return None

    def GetBoard(self, board):
        return f"{board[0]} | {board[1]} | {board[2]}\n{'-' * 14}\n{board[3]} | {board[4]} | {board[5]}\n{'-' * 14}\n{board[6]} | {board[7]} | {board[8]}"

    def CheckWin(self, board, sym):
        if (board[0] == board[1] == board[2]) and board[0] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[0])
        elif (board[3] == board[4] == board[5]) and board[3] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[3])
        elif (board[6] == board[7] == board[8]) and board[6] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[6])

        if (board[0] == board[3] == board[6]) and board[0] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[0])
        elif (board[1] == board[4] == board[7]) and board[1] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[1])
        elif (board[2] == board[5] == board[8]) and board[2] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[2])

        if (board[0] == board[4] == board[8]) and board[0] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[0])
        elif (board[2] == board[4] == board[6]) and board[2] != ":black_large_square:":
            return self.GetKeyByValue(sym, board[2])

        if board[0] != ":black_large_square:" \
                and board[1] != ":black_large_square:" \
                and board[2] != ":black_large_square:" \
                and board[3] != ":black_large_square:" \
                and board[4] != ":black_large_square:" \
                and board[5] != ":black_large_square:" \
                and board[6] != ":black_large_square:" \
                and board[7] != ":black_large_square:" \
                and board[8] != ":black_large_square:":
            return "DRAW"
        return False

    @commands.command(aliases=tic_tac_toe_command_aliases)
    async def t_start(self, ctx: commands.Context, member: discord.Member = None):
        logs = self.bot.get_channel(mini_games['notification_channel'])
        if not member:
            return await ctx.reply("Укажите, с кем хотите играть!")

        elif member.id == ctx.author.id:
            return await ctx.reply("Вы не можете играть с самии собой!")

        elif member.bot:
            if ctx.message.author == ctx.guild.owner:
                return await ctx.reply("Папочка, ты снова меня обыграешь...")
            else:
                return await ctx.reply("Папа запретил мне играть с незнакомцами.")

        if ctx.author.id in self.playing:
            return await ctx.reply("Вы уже играете!")

        elif member.id in self.playing:
            return await ctx.reply("Данный пользователь уже играет!")

        waiting_game_embed = discord.Embed(title="Крестики-нолики <:ttt:821377566870339614>",
                                           description=f"Ожидаем согласия {member.mention} на игру...")
        reject_game_embed = discord.Embed(title="Крестики-нолики <:ttt:821377566870339614>",
                                          description=f"{member.mention} отказался от игры.")
        timeout_game_embed = discord.Embed(title="Крестики-нолики <:ttt:821377566870339614>",
                                           description=f"Время ожидания {member.mention} вышло.")
        msg = await ctx.reply(embed=waiting_game_embed)
        await msg.add_reaction("<:confirm:821318653563502612>")
        await msg.add_reaction("<:reject:821318659162243103>")

        try:
            r, _ = await self.bot.wait_for("reaction_add", timeout=60.0,
                                           check=lambda r, u: r.message.id == msg.id and str(r.emoji) in [
                                               "<:confirm:821318653563502612>",
                                               "<:reject:821318659162243103>"] and not u.bot and u.id == member.id)
            if str(r.emoji) == "<:reject:821318659162243103>":
                return await msg.edit(embed=reject_game_embed, delete_after=10)
        except asyncio.TimeoutError:
            return await msg.edit(embed=timeout_game_embed, delete_after=10)

        self.playing.append(member.id)
        self.playing.append(ctx.author.id)
        category: discord.CategoryChannel = self.bot.get_channel(820376219945795584)
        channel: discord.TextChannel = await category.create_text_channel(name=f"{member.name} vs {ctx.author.name}")
        confirm_game_embed = discord.Embed(title="Крестики-нолики <:ttt:821377566870339614>",
                                           description=f"{member.mention} принял вызов!\n\n"
                                                       f"Играйте в канале: {channel.mention}")
        await msg.edit(embed=confirm_game_embed, delete_after=10)
        await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=False)
        await channel.set_permissions(member, read_messages=True, send_messages=False)
        msg: discord.Message = await channel.send(
            embed=discord.Embed(title=f"Играют:\n{ctx.author}\nпротив\n{member}", color=0x00ff00,
                                description=f"""{ctx.author.mention} - <:tttmark:821379069928013874>
        {member.mention} - <:tttround:821381104183279616>

        Сейчас ход: {ctx.author}
        :black_large_square: | :black_large_square: | :black_large_square:
        --------------
        :black_large_square: | :black_large_square: | :black_large_square:
        --------------
        :black_large_square: | :black_large_square: | :black_large_square:
        """))

        board = [":black_large_square:" for _ in range(9)]
        sym = {ctx.author.id: "<:tttmark:821379069928013874>", member.id: "<:tttround:821381104183279616>"}
        now = ctx.author.id

        reactions = [emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":one:"], emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":two:"],
                     emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":three:"], emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":four:"],
                     emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":five:"], emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":six:"],
                     emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":seven:"], emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":eight:"],
                     emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":nine:"]]
        boardIndex = {
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":one:"]: 0,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":two:"]: 1,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":three:"]: 2,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":four:"]: 3,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":five:"]: 4,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":six:"]: 5,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":seven:"]: 6,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":eight:"]: 7,
            emoji.EMOJI_ALIAS_UNICODE_ENGLISH[":nine:"]: 8
        }

        for r in reactions:
            await msg.add_reaction(r)

        while True:
            react, user = await self.bot.wait_for("reaction_add",
                                                  check=lambda r, u: r.message.id == msg.id and not u.bot)

            if str(react.emoji) not in reactions:
                await msg.clear_reaction(react)
                continue

            elif user.id != now:
                await msg.remove_reaction(react, user)
                continue

            reactions.remove(str(react.emoji))
            await msg.clear_reaction(react)

            board[boardIndex[str(react.emoji)]] = sym[now]

            now = self.GetNextTurn(ctx.author, member, now)
            check = self.CheckWin(board, sym)
            if check == "DRAW":
                self.playing.remove(ctx.author.id)
                self.playing.remove(member.id)
                await channel.delete()
                return await logs.send(
                    embed=discord.Embed(title=f"Крестики-нолики <:ttt:821377566870339614>",
                                        color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                     random.randint(1, 255)),
                                        description=f"{member.mention} - <:tttround:821381104183279616>\n{ctx.author.mention} - <:tttmark:821379069928013874>\n\n__**Ничья**__\n\n{self.GetBoard(board)}"))
            elif check == ctx.author.id:
                self.playing.remove(ctx.author.id)
                self.playing.remove(member.id)
                await channel.delete()
                return await logs.send(
                    embed=discord.Embed(title=f"Крестики-нолики <:ttt:821377566870339614>",
                                        color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                     random.randint(1, 255)),
                                        description=f"{member.mention} - <:tttround:821381104183279616>\n{ctx.author.mention} - <:tttmark:821379069928013874>\n\n__**Победил**__: {ctx.author.mention}\n\n{self.GetBoard(board)}"))
            elif check == member.id:
                self.playing.remove(ctx.author.id)
                self.playing.remove(member.id)
                await channel.delete()
                return await logs.send(
                    embed=discord.Embed(title=f"Крестики-нолики <:ttt:821377566870339614>",
                                        color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                                     random.randint(1, 255)),
                                        description=f"{member.mention} - <:tttround:821381104183279616>\n"
                                                    f"{ctx.author.mention} - <:tttmark:821379069928013874>\n\n"
                                                    f"__**Победил**__: {member.mention}\n\n{self.GetBoard(board)}"))

            await msg.edit(embed=discord.Embed(title=f"Играют {ctx.author} против {member}", color=0x00ff00,
                                               description=f"""{ctx.author} - <:tttmark:821379069928013874>
                                                                {member} - <:tttround:821381104183279616>\n
            __**Сейчас ходит**__: {self.bot.get_user(now).mention}\n
            {self.GetBoard(board)}
            """))


def setup(bot):
    bot.add_cog(TicTacToe(bot))
