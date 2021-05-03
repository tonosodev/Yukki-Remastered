import discord

import random
from discord.ext import commands
from loguru import logger

from config import commands_permission, hug_command_aliases, bot_initialize


class HugCommentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog Hugs loaded!")

    @commands.command(aliases=hug_command_aliases)
    @commands.has_any_role(*commands_permission['hug_command_permission'])
    async def hug(self, ctx, member: discord.Member):
        hug_img = (
            "https://cdn.discordapp.com/attachments/824337879198466049/826155991367680070/hug_1.gif",
            "https://cdn.discordapp.com/attachments/824337879198466049/826155991967989811/hug_2.gif",
            "https://cdn.discordapp.com/attachments/824337879198466049/826155999835586611/hug_3.gif",
            "https://cdn.discordapp.com/attachments/824337879198466049/826156000696205362/hug_7.gif",
            "https://cdn.discordapp.com/attachments/824337879198466049/826156002113224774/hug_5.gif",
            "https://cdn.discordapp.com/attachments/824337879198466049/826156002352037898/hug_4.gif",
            "https://cdn.discordapp.com/attachments/824337879198466049/826156005053825024/hug_6.gif"
        )
        if not member:
            await ctx.message.delete()
            embed = discord.Embed(description='{} обнял всех 💜'.format(ctx.author.mention))
            embed.set_image(url=random.choice(hug_img))
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            embed = discord.Embed(description='{} обнимает {} 💜'.format(ctx.author.mention, member.mention))
            embed.set_image(url=random.choice(hug_img))
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HugCommentCog(bot))
