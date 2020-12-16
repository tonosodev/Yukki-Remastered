import discord
from discord import utils
from discord.ext import commands
from config import verification, verification_roles, MAX_ROLES_PER_USER, EXCROLES


class VerificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        channel = self.bot.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = utils.get(message.guild.members,
                           id=payload.user_id)  # получаем объект пользователя который поставил реакцию

        try:
            if payload.message_id == verification['verification_channel_id'] and payload.channel_id == verification['verification_post_id']:
                emoji = str(payload.emoji)  # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=verification_roles[emoji])  # объект выбранной роли (если есть)
                role_1 = utils.get(message.guild.roles, id=766232996285775903)

            if (len([i for i in member.roles if i.id not in EXCROLES]) <= MAX_ROLES_PER_USER):
                role_old = discord.utils.get(member.guild.roles, name='✖ not verified')
                await member.remove_roles(role_old)
                await member.add_roles(role)
                await member.add_roles(role_1)
            #   print('[DEBUG] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))
        except UnboundLocalError as e:
            print(repr(e))


#    @commands.Cog.listener()
#    async def on_raw_reaction_remove(self, payload):
#        channel = self.bot.get_channel(payload.channel_id)  # получаем объект канала
#        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
#        member = utils.get(message.guild.members,
#                           id=payload.user_id)  # получаем объект пользователя который поставил реакцию
#
#        try:
#            if payload.message_id == config_channel['post_id'] and payload.channel_id == config_channel[
#                'channel_id']:
#                emoji = str(payload.emoji)  # эмоджик который выбрал юзер
#            role = utils.get(message.guild.roles, id=ROLES[emoji])  # объект выбранной роли (если есть)
#
#            await member.remove_roles(role)
#            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))
#        except KeyError as e:
#            print('[ERROR] KeyError, no role found for ' + emoji)
#        except Exception as e:
#            print(repr(e))
#        except UnboundLocalError as e:
#            print(repr(e))

def setup(bot):
    bot.add_cog(VerificationCog(bot))
