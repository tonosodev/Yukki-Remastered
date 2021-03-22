"""
Today is 3/20/2021
Session by: https://github.com/DevilDesigner
Create Time: 7:28 PM
This Class: new_slot
"""

import asyncio
import random
import discord
from discord.ext import commands
from loguru import logger
from config import slot_command_aliases, mini_games, bot_initialize


class SlotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.playing = []

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog Slot-Machine loaded!")

    @commands.command()
    async def new_slot(self, ctx):

        if ctx.author.id in self.playing:
            return await ctx.reply("Вы уже играете!")

        logs = self.bot.get_channel(mini_games['notification_channel'])
        price = 0
        random_reward = random.randrange(1, 200, 1)

        waiting_game_embed = discord.Embed(title="Слот-машина :gem:️",
                                           description=f"Выберите начальную ставку или откажитесь от начала игры!\n\n"
                                                       f"<:bet_1:822838454739271721> - **80** <:yukki_dollar:816330956137824266>\n"
                                                       f"<:bet_2:822840001553104906> - **160** <:yukki_dollar:816330956137824266>\n"
                                                       f"<:bet_3:822840007114096650> - **320** <:yukki_dollar:816330956137824266>\n"
                                                       f"<:bet_4:822840006921289769> - **600** <:yukki_dollar:816330956137824266>\n\n"
                                                       f"__В случае победы Ваша ставка гарантировано утрируется!__")
        reject_game_embed = discord.Embed(title="Слот-машина :gem:️",
                                          description=f"{ctx.author.mention}, Вы отказались от игры.")
        timeout_user_embed = discord.Embed(title="Слот-машина :gem:️",
                                           description=f"Время ожидания выбора ставки {ctx.author.mention} вышло.")
        msg = await ctx.reply(embed=waiting_game_embed)
        await msg.add_reaction("<:bet_1:822838454739271721>")
        await msg.add_reaction("<:bet_2:822840001553104906>")
        await msg.add_reaction("<:bet_3:822840007114096650>")
        await msg.add_reaction("<:bet_4:822840006921289769>")
        await msg.add_reaction("<:reject:821318659162243103>")

        try:
            r, _ = await self.bot.wait_for("reaction_add", timeout=60.0,
                                           check=lambda r, u: r.message.id == msg.id and str(r.emoji) in [
                                               "<:bet_1:822838454739271721>",
                                               "<:bet_2:822840001553104906>",
                                               "<:bet_3:822840007114096650>",
                                               "<:bet_4:822840006921289769>",
                                               "<:reject:821318659162243103>"] and not u.bot and u.id == ctx.author.id)
            if str(r.emoji) == "<:reject:821318659162243103>":
                return await msg.edit(embed=reject_game_embed, delete_after=10)
            if str(r.emoji) == "<:bet_1:822838454739271721>":
                price += 80
            if str(r.emoji) == "<:bet_2:822840001553104906>":
                price += 160
            if str(r.emoji) == "<:bet_3:822840007114096650>":
                price += 320
            if str(r.emoji) == "<:bet_4:822840006921289769>":
                price += 600
        except asyncio.TimeoutError:
            return await msg.edit(embed=timeout_user_embed, delete_after=10)

        self.playing.append(ctx.author.id)

        category: discord.CategoryChannel = self.bot.get_channel(820376219945795584)
        channel: discord.TextChannel = await category.create_text_channel(name=f"slot-{ctx.author.name}")
        confirm_game_embed = discord.Embed(title="Слот-машина :gem:️",
                                           description=f"{ctx.author.mention}, ваша ставка: **{price}**\n\n"
                                                       f"Играйте в канале: {channel.mention}")
        await msg.edit(embed=confirm_game_embed, delete_after=10)
        await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=False)

        msg: discord.Message = await channel.send(
            embed=discord.Embed(title=f"Слот-машина :gem:️", color=0x00ff00,
                                description=f"""\n
        :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square:
         ——————————
        :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square:
         ——————————
        :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square:
         ——————————
        :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square:
         ——————————
        :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square: | :black_large_square:

        \n
        {ctx.author.name}, Вы готовы?...
        """))
        await msg.add_reaction("<:confirm:821318653563502612>")

        reward = price * 3 + random_reward
        #await ctx.send("Ваш выигрыш: " + str(reward))


def setup(bot):
    bot.add_cog(SlotCog(bot))
