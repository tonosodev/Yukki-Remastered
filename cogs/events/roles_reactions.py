"""
Today is 3/11/2021
Session by: https://github.com/DevilDesigner
Create Time: 3:30 AM
This Class: roles_reactions
"""

from discord.ext import commands

class Reactions(commands.Cog, name="ReactionRoles"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        roles = {
            818868967825080330: 818003458094399508,
            818865783479599154: 818860755763331072,
            818870007810883614: 818004267084414976,
            818878406698598453: 818003143639433246,
            818877410950119434: 818002500111826978,
            818867326564565033: 818003818113269770,
            818872164823728189: 818002281172697088,
            818874039178100776: 818001571710763028,
            818848454708166707: 818748991135023125
        }


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

        if react.id not in roles.keys():
            return

        role = guild.get_role(roles[react.id])
        if not role:
            return

        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        roles = {
            818868967825080330: 818003458094399508,
            818865783479599154: 818860755763331072,
            818870007810883614: 818004267084414976,
            818878406698598453: 818003143639433246,
            818877410950119434: 818002500111826978,
            818867326564565033: 818003818113269770,
            818872164823728189: 818002281172697088,
            818874039178100776: 818001571710763028,
            818848454708166707: 818748991135023125
        }

        
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

        if react.id not in roles.keys():
            return

        role = guild.get_role(roles[react.id])
        if not role:
            return

        await member.remove_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
