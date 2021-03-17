"""
Today is 3/17/2021
Session by: https://github.com/DevilDesigner
Create Time: 8:56 PM
This Class: new_mute_system
"""

import discord
import config
import time
from utils import DB
from discord.ext import commands


# Код
class Moder(commands.Cog):
    @commands.command(
        aliases=["mute", "Mute"],
        description="Issue mute to member",
        usage="mute <member> <time> <type time> <reason>")
    @commands.has_permissions(manage_messages=True)
    async def mutes(self, ctx, member: discord.Member, timenumber: int, typetime, *, reason):

        timed = 0

        if typetime == "s" or typetime == "sec" or typetime == "seconds":
            timed = timenumber
        elif typetime == "m" or typetime == "min" or typetime == "minutes":
            timed = timenumber * 60
        elif typetime == "h" or typetime == "hour" or typetime == "hours":
            timed = timenumber * 60 * 60
        elif typetime == "d" or typetime == "day" or typetime == "days":
            timed = timenumber * 60 * 60 * 24

        times = time.time()
        times += timed

        mute_role = discord.utils.get(ctx.message.guild.roles, name="MUTED")

        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")

        if mute_role in member.roles:
            await ctx.send(
                embed=discord.Embed(description=f'**:warning: Member {member.mention} already muted!**', ))
        else:
            DB.Set().mute(member, times)

            await member.add_roles(mute_role,
                                   reason=f"Member {ctx.author.display_name} issued mute on {timenumber} {typetime} because of {reason}",
                                   atomic=True)
            await ctx.send(
                embed=discord.Embed(
                    description=f'**:shield: Mute to user {member.mention} successfully issued due to {reason}!**', ))

    @mutes.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                description=f'**:grey_exclamation: {ctx.author.name}, be sure to specify the user and time!**\n'
                            f'{config.bot_settings["bot_prefix"]}mute <member> <time> <type time> <reason>', ))

    # Размьют
    @commands.command(
        aliases=["unmute", "Unmute"],
        description="Remove mute from the member",
        usage="unmute <member>")
    @commands.has_permissions(manage_messages=True)
    async def unmutes(self, ctx, member: discord.Member):

        mutes = DB.Get().mute(member)
        mute = mutes[1]

        mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")

        if mute != 0:
            DB.Set().mute(member, 0)

            await member.remove_roles(mute_role)
            await ctx.send(embed=discord.Embed(
                description=f'**:white_check_mark: Mute by {member.mention} Successfully removed!**', ))
        else:
            await ctx.send(
                embed=discord.Embed(description=f'**:warning: member {member.mention} Not muted!**', ))

    @unmutes.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                description=f'**:grey_exclamation: {ctx.author.name}, be sure to specify the member!**\n{config.bot_settings["bot_prefix"]}unmute <member>',
                color=0x0c0c0c))
