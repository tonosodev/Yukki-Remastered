"""
Today is 3/11/2021
Session by: https://github.com/DevilDesigner
Create Time: 3:30 AM
This Class: roles_reactions
"""

from discord.ext import commands

from config import roles_for_members


class Reactions(commands.Cog, name="ReactionRoles"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        if payload.guild_id != 766213910595633153 or payload.channel_id != 768556053682978816:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member:
            return

        react = payload.emoji
        if not hasattr(react, "id"):
            return

        if react.id not in roles_for_members.keys():
            return

        role = guild.get_role(roles_for_members[react.id])
        if not role:
            return

        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        if payload.guild_id != 766213910595633153 or payload.channel_id != 768556053682978816:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member:
            return

        react = payload.emoji
        if not hasattr(react, "id"):
            return

        if react.id not in roles_for_members.keys():
            return

        role = guild.get_role(roles_for_members[react.id])
        if not role:
            return

        await member.remove_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
