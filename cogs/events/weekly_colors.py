"""
Today is 3/9/2021
Session by: https://github.com/DevilDesigner
Create Time: 6:12 PM
This Class: weekly_сolors
"""

import discord
from discord.ext import commands, tasks
import ujson
import datetime


class WeekColor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=1.0)
    async def main(self):
        now = datetime.datetime.now()
        with open("./cogs/events/data/WeekColor.json", "r") as file:
            db = ujson.load(file)

        if len(list(db.keys())) <= 0:
            print("\n##################################################\n"
                  "[WARNING] WeeklyColors database is empty! Updating . . ."
                  "\n##################################################\n")
            need = now + datetime.timedelta(days=7)
            with open("./cogs/events/data/WeekColor.json", "w") as file:
                ujson.dump({"date": need.strftime("%d.%m.%Y %H:%M:%S")}, file, indent=4, ensure_ascii=False)
        else:
            need = datetime.datetime.strptime(db["date"], "%d.%m.%Y %H:%M:%S")
        if now >= need and now.minute >= need.minute:
            print('\n##################################################\n'
                  f'[NOTE] Next WeeklyColors update after {need - now}'
                  '\n##################################################\n')

            need += datetime.timedelta(days=7)
            with open("./cogs/events/data/WeekColor.json", "w") as file:
                ujson.dump({"date": need.strftime("%d.%m.%Y %H:%M:%S")}, file, indent=4, ensure_ascii=False)

            channel = self.bot.get_channel(767917902791311370)
            message = await channel.fetch_message(823524487592935445)
            reacts = ["<:dark_orchid:823521827372531762>", "<:purple:823521835869536306>",
                      "<:hot_pink:823521827329933313>",
                      "<:indian_red:823521832396128276>", "<:sandy_brown:823521835652087808>",
                      "<:light_salmon:823521833310879757>", "<:light_sea:823521835785781288>",
                      "<:medium_sea:823521835345117204>", "<:silver:823521835651694612>"]
            reactions = list(filter(lambda react: str(react.emoji) in reacts, message.reactions))
            reactions = {str(react.emoji): react.count for react in reactions}
            if len(reactions) <= 0:
                return

            colors = {"<:dark_orchid:823521827372531762>": 0x9932CC,
                      "<:purple:823521835869536306>": 0x9370DB,
                      "<:hot_pink:823521827329933313>": 0xFF69B4,
                      "<:indian_red:823521832396128276>": 0xCD5C5C,
                      "<:sandy_brown:823521835652087808>": 0xF4A460,
                      "<:light_salmon:823521833310879757>": 0xFFA07A,
                      "<:light_sea:823521835785781288>": 0x20B2AA,
                      "<:medium_sea:823521835345117204>": 0x3CB371,
                      "<:silver:823521835651694612>": 0xC0C0C0
                      }
            maxReact = max(reactions.items(), key=lambda arg: arg[-1])
            currentColor = colors[maxReact[0]]
            guild = self.bot.get_guild(766213910595633153)
            role = guild.get_role(766232996285775903)
            await role.edit(color=currentColor)
            colors_embed = discord.Embed(title='Голосование за цвет недели <:colors:823504262168051764>',
                                         description='__**Оставляйте свои пожелания, выбирая доступные эмодзи!**__\n\n'
                                                     f'Последнее обновление:\n'
                                                     f'**{db["date"]} | GMT+6**',
                                         color=0x9400D3)
            await message.edit(embed=colors_embed)
            await message.clear_reactions()
            for react in reacts:
                await message.add_reaction(react)


def setup(bot):
    bot.add_cog(WeekColor(bot))
