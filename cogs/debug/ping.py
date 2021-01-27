from discord.ext import commands
from config import ping_aliases, commands_permission


class PingCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # items = [766293535832932392, 766233124681547776, 766231587104620554]

    @commands.command(aliases=ping_aliases)
    @commands.has_any_role(*commands_permission['ping_permission'])
    async def ping(self, ctx):
        await ctx.message.delete()
        ping = self.bot.ws.latency

        if ping < 0.10000000000000000:
            ping_emoji = "🟩 🔳 🔳 🔳 🔳"

        if ping > 0.10000000000000000:
            ping_emoji = "🟧🟩 🔳 🔳 🔳"

        if ping > 0.15000000000000000:
            ping_emoji = "🟥🟧🟩 🔳 🔳"

        if ping > 0.20000000000000000:
            ping_emoji = "🟥🟥🟧🟩 🔳"

        if ping > 0.25000000000000000:
            ping_emoji = "🟥🟥🟥🟧🟩"

        if ping > 0.30000000000000000:
            ping_emoji = "🟥🟥🟥🟥🟧"

        if ping > 0.35000000000000000:
            ping_emoji = "🟥🟥🟥🟥🟥"

        message = await ctx.send("Пожалуйста, подождите. . .")
        await message.edit(content=f"Понг!\n{ping_emoji} `{ping * 1000:.0f}ms`", delete_after=10)


def setup(bot):
    bot.add_cog(PingCommandCog(bot))
