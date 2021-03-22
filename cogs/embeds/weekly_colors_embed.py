"""
Today is 3/22/2021
Session by: https://github.com/DevilDesigner
Create Time: 4:15 PM
This Class: weekly_colors_embed
"""

import discord
import ujson
from discord.ext import commands
from config import commands_permission


class MetaPeaceRulesEmbedsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*commands_permission['server_status_permission'])
    async def colors_embed(self, ctx):

        with open("./cogs/events/data/WeekColor.json", "r") as file:
            db = ujson.load(file)

        await ctx.message.delete()
        colors_embed = discord.Embed(title='Голосование за цвет недели <:colors:823504262168051764>',
                                     description='__**Оставляйте свои пожелания, выбирая доступные эмодзи!**__\n\n'
                                                 f'Последнее обновление:\n'
                                                 f'**{db["date"]}**',
                                                 color=0x9400D3)

        await ctx.send(file=discord.File(r".\cogs\embeds\colors.gif"))
        msg = await ctx.send(embed=colors_embed)
        reacts = ["<:dark_orchid:823521827372531762>", "<:purple:823521835869536306>", "<:hot_pink:823521827329933313>",
                  "<:indian_red:823521832396128276>", "<:sandy_brown:823521835652087808>",
                  "<:light_salmon:823521833310879757>", "<:light_sea:823521835785781288>",
                  "<:medium_sea:823521835345117204>", "<:silver:823521835651694612>"]
        for react in reacts:
            await msg.add_reaction(react)


def setup(bot):
    bot.add_cog(MetaPeaceRulesEmbedsCog(bot))
