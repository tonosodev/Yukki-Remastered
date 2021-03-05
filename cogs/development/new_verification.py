import discord
import secrets
from discord.ext import commands
from config import verification, verification_roles, bot_settings, server_roles


class NewVerificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        everyone_role = server_roles['everyone_role']
        # not_verified_role = server_roles['not_verified_role']
        verified_role = server_roles['verified_role']
        # member_role = server_roles['member_role']
        tech_support_role = server_roles['tech.support_role'],
        support_role = server_roles['support_role'],
        not_verified_role = discord.utils.get(member.guild.roles, id=server_roles['not_verified_role'])
        member_role = discord.utils.get(member.guild.roles, id=server_roles['member_role'])
        verification_log_channel = self.bot.get_channel(verification['verification_log_id'])

        token = secrets.token_urlsafe(5)

        welcome_msg = f'{member.mention}, пройдите капчу для авторизации на сервере.\n' \
                      f'Вашему вниманию представлен небольшой ГИД по возможным проблемам при вводе и их решению:\n\n' \
                      f'1. Не видна картинка, но виден текст, с просьбой ввести с неё код\n' \
                      f'- Перейдите в "Настройки пользователя"\n' \
                      f'- Выберите вкладку "Текст изображения"\n' \
                      f'- Активируйте опцию "При публикации ссылки в чате."\n\n' \
                      f'2. Виден только данный текст\n' \
                      f'- Перейдите в "Настройки пользователя"\n' \
                      f'- Выберите вкладку "Текст изображения"\n' \
                      f'- Активируйте опцию "Отображать предпросмотр сайта для ссылок."\n\n' \
                      f'3. Код отправлен, но ничего не произошло\n' \
                      f'- Пожалуйста, перезайдите на сервер.\n' \
                      f'В слачае, если ошибка повторилась, отпишите об этом управляющему составу на сервере, который отображается в правом верхнем углу: `Owner`'

        verification_embed = discord.Embed(title='Напишите сюда код, указанный на картинке:')
        verification_embed.add_field(name='Debug', value=f'{token}')
        # verification_embed.set_image(url='')

        if member.guild.id == everyone_role:
            await member.add_roles(not_verified_role)
            await member.send(content=welcome_msg, embed=verification_embed)
        else:
            pass


def setup(bot):
    bot.add_cog(NewVerificationCog(bot))
