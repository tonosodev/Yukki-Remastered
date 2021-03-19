"""
Today is 3/9/2021
Session by: https://github.com/DevilDesigner
Create Time: 6:12 PM
This Class: weekly_сolors
"""

from discord.ext import commands, tasks
import ujson
import datetime
from loguru import logger


class WeekColor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog WeekColor loaded!")
        await self.bot.wait_until_ready()
        self.main.start()

    @tasks.loop(minutes=1.0)
    async def main(self):
        now = datetime.datetime.now()
        with open("./data/WeekColor.json", "r") as file:
            db = ujson.load(file)

        if len(list(db.keys())) <= 0:
            need = now + datetime.timedelta(minutes=2)
            with open("./cogs/events/data/WeekColor.json", "w") as file:
                ujson.dump({"date": need.strftime("%d.%m.%Y %H:%M:%S")}, file, indent=4, ensure_ascii=False)
        else:
            need = datetime.datetime.strptime(db["date"], "%d.%m.%Y %H:%M:%S")

        if now >= need and now.minute >= need.minute:
            need += datetime.timedelta(minutes=2)
            with open("./cogs/events/data/WeekColor.json", "w") as file:
                ujson.dump({"date": need.strftime("%d.%m.%Y %H:%M:%S")}, file, indent=4, ensure_ascii=False)

            channel = self.bot.get_channel(767917902791311370)
            message = await channel.fetch_message(767920097854881803)
            reacts = ["🔴", "🟢", "🔵", "🟡", "🟣", "🟤", "⚫"]
            reactions = list(filter(lambda react: str(react.emoji) in reacts, message.reactions))
            reactions = {str(react.emoji): react.count for react in reactions}
            if len(reactions) <= 0:
                return

            colors = {"🔴": 0xff0000, "🟢": 0x00ff00, "🔵": 0x0000ff, "🟡": 0xffff00, "🟣": 0x7f00ff, "🟤": 0x6b3900,
                      "⚫": 0x000001}
            maxReact = max(reactions.items(), key=lambda arg: arg[-1])
            currentColor = colors[maxReact[0]]
            guild = self.bot.get_guild(766213910595633153)
            role = guild.get_role(766232996285775903)
            await role.edit(color=currentColor)
            await message.clear_reactions()
            for react in reacts:
                await message.add_reaction(react)


def setup(bot):
    bot.add_cog(WeekColor(bot))
