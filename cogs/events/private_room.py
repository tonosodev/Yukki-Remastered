from discord.ext import commands
from loguru import logger


class Privates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.CREATE_CHANNEL_ID = 769475442603196417
        self.WAITING_ROOM_ID = 769495764694335488
        self.CATEGORY_ID = 769490405711413248

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog Privates loaded")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel:
            if after.channel.guild.id != 766213910595633153:
                return

            if after.channel.id == self.CREATE_CHANNEL_ID:
                category = self.bot.get_channel(self.CATEGORY_ID)
                ch = await category.create_voice_channel(name=member.display_name, overwrites=None)
                wait = self.bot.get_channel(769495764694335488)
                await wait.set_permissions(member, move_members=True)
                await ch.set_permissions(member, move_members=True, manage_channels=True, manage_permissions=True,
                                         connect=True, speak=True)
                await member.move_to(ch)

        if before.channel:
            if before.channel.guild.id != 766213910595633153:
                return

            if before.channel.category.id == self.CATEGORY_ID:
                wait = self.bot.get_channel(769495764694335488)
                if not after.channel:
                    await wait.set_permissions(member, move_members=False)
                elif after.channel.category.id != self.CATEGORY_ID:
                    await wait.set_permissions(member, move_members=False)

                if len(before.channel.members) <= 0:
                    await before.channel.delete()


def setup(bot):
    bot.add_cog(Privates(bot))
