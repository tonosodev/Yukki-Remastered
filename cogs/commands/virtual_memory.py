import discord
from config import virtual_ram_aliases, commands_permission
from discord.ext import commands
from psutil import virtual_memory


class VirtualMemoryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#    @commands.command(aliases=virtual_ram_aliases)
#    @commands.has_any_role(*commands_permission['virtual_ram_permission'])
#    async def ram(self, ctx):

#        ram = virtual_memory().total
#        used = virtual_memory().used

#        field = []
#        while len(field) != 5:

#            if round(used, 1) >= ram / 5:
#                used -= ram / 5
#                field.append("🟥 ")

#            elif round(used, 1) >= ram / 10:
#                used -= ram / 10
#                field.append("🟨 ")

#            elif used <= ram / 10:
#                used = 0
#            field.append("🟦 ")


#        msg = ''
#        for i in range(len(field)):
#            msg += field[i]

#        embed = discord.Embed(title="Использовано RAM", description=msg)
#        embed.set_footer(
#            text=f"{round(virtual_memory().used / 1024 / 1024 / 1024, 2)} GB из {round(ram / 1024 / 1024 / 1024, 2)} GB")
#        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(VirtualMemoryCog(bot))
