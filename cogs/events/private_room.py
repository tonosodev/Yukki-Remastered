import discord
from discord.ext import commands

from config import private_room_category


class PrivateRoom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, channel, after):
        if after.channel is not None:
            if after.channel.id == 769475442603196417:
                # print(f"[DEBUG]: {member} создаёт приватный канал! ")
                for guild in self.bot.guilds:
                    mainCategory = discord.utils.get(guild.categories, id=private_room_category)
                    personal_channel = await guild.create_voice_channel(name=f"🔐 Комната {member.display_name}",
                                                                        category=mainCategory)
                await personal_channel.set_permissions(member, connect=True, mute_members=True, move_members=True,
                                                       manage_channels=True)
                await member.move_to(personal_channel)

                def check(x, y, z):
                    return len(personal_channel.members) == 0

                await self.bot.wait_for('voice_state_update', check=check)
                await personal_channel.delete()


def setup(bot):
    bot.add_cog(PrivateRoom(bot))
