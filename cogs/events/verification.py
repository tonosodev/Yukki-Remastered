import discord
from discord import utils
from discord.ext import commands
from config import verification, verification_roles, bot_settings, server_roles


class VerificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        channel = self.bot.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = utils.get(message.guild.members, id=payload.user_id)  # получаем объект пользователя который поставил реакцию

        try:
            if payload.message_id == verification['verification_post_id'] and payload.channel_id \
                    == verification['verification_channel_id']:
                emoji = str(payload.emoji)
                role = utils.get(message.guild.roles, id=verification_roles[
                    '<a:verify:768537178221051944>'])
                role_1 = utils.get(message.guild.roles, id=server_roles['member_role'])

                role_old = discord.utils.get(member.guild.roles, id=server_roles['not_verified_role'])
                await member.remove_roles(role_old)
                await member.add_roles(role)
                await member.add_roles(role_1)
                await message.remove_reaction(payload.emoji, member)
                log = open('log.txt', 'a')
                log.write(f'[АВТОРИЗАЦИЯ] ' + f'Пользователь {member} успешно прошел авторизацию!\n')
                log.write('...\n')
                log.close()
                await self.bot.get_channel(bot_settings['system_log_channel']).send(embed=discord.Embed(
                    description=f'🟢 Пользователь **{member}** успешно прошел авторизацию!\n\n**`Выданы роли:`**\n- ( {role} )\n- ( {role_1} )'))

        except KeyError as e:
            print('[VERIFICATION COG ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print('[VERIFICATION COG EXCEPTION] ' + repr(e))
        except UnboundLocalError as e:
            print('[VERIFICATION COG EXCEPTION] ' + repr(e))


def setup(bot):
    bot.add_cog(VerificationCog(bot))
