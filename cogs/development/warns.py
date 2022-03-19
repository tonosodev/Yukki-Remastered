"""
Today is 3/21/2021
Session by: https://github.com/DevilDesigner
Create Time: 11:40 PM
This Class: warns
"""

import discord
from discord.ext import commands
from loguru import logger
import datetime

from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://NeverMind:3Ctj5eEMI0vzwRY8@nevermindcluster.hfbwn.mongodb.net/YukkiModeration?retryWrites=true&w=majority")


class WarnSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog WarnSystem loaded")

    @commands.command()
    async def warn(self, ctx, member: discord.Member = None, *, reason: str = None):
        if not member:
            return await ctx.send("Укажите кому выдать предупреждение")

        elif member.id == ctx.author.id:
            return await ctx.send("Вы не можете выдать предупреждение самому себе")

        elif member.bot:
            return await ctx.send("Вы не можете выдать предупреждение боту")

        elif member.top_role and ctx.author.top_role:
            if member.top_role.position >= ctx.author.top_role.position:
                return await ctx.send("Данный пользователь выше вас или равен вам по ролям")

        found = client.YukkiModeration.WarnCollection.find_one({"_id": member.id})
        if not found:
            await ctx.send(f"Выдан варн `#1` пользователю `{member}`")
            return client.YukkiModeration.WarnCollection.insert_one({"_id": member.id, "warns": [
                {"reason": reason, "date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                 "by": ctx.author.id}]})

        await ctx.send(f"Выдано предупреждение `#{len(found['warns']) + 1}` пользователю `{member}`")
        client.YukkiModeration.WarnCollection.update_one({"_id": member.id}, {"$push": {
            "warns": {"reason": reason, "date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                      "by": ctx.author.id}}})

        warns = len(found["warns"]) + 1
        if warns == 3:
            await ctx.send("Допустим тут наказание за 3 предупреждения")
            ...

        elif warns == 5:
            await ctx.send("Допустим тут наказание за 5 предупреждений")
            ...

            await ctx.send(
                f"Пользователь `{member}` достиг последнего уровня наказаний, его предупреждения были сброшены")
            client.YukkiModeration.WarnCollection.delete_one({"_id": member.id})


def setup(bot):
    bot.add_cog(WarnSystem(bot))
