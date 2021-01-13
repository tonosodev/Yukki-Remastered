import discord
import random
from discord.ext import commands

from config import bot_initialize


class OnMemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id == 766213910595633153:
            role = discord.utils.get(member.guild.roles, name='✖ not verified')
            await member.add_roles(role)
            user = member.mention

            JoinMessages = (
                '{} здравствуй!\nПоддержите команду - позовите друзей, знакомых, близких, захватите с собой еще кота...'.format(
                    user),
                '{}, ну, жалуйтесь...'.format(user), '{}, проходите, не стесняйтесь!'.format(user),
                '{} мы в Вашем распоряжении.'.format(user),
                '{} был из тех, кто просто любит жизнь...'.format(user),
                '{} присоединяясь обещал, что матершинные слова не будет он употре...\n...блять.'.format(user),
                '{}, располагайтесь, мы здесь не кусаемся! 💜'.format(user), '{}, рады видеть Вас!'.format(user),
                '{} доброго времени суток!'.format(user),
                '{} проскальзывает на сервер.'.format(user), '{}, кажется, принёс нам пиццу!'.format(user),
                'Вот это врыв!\n{}, это было превосходно!'.format(user), '{} - Вы прекрасны.'.format(user),
                '{}, мя! 💕'.format(user), 'Последняя надежда человечества, {}, присоеденился!'.format(user),
                '{}, заходи, не бойся - находясь не плачь...'.format(user),
                '{}?\nЛюбопытно...'.format(user), '{}, улыбнись! 😸'.format(user),
                '{}, добро пожаловать на борт!'.format(user), 'Что нового расскажете, {}?'.format(user),
                '{}, сквозь эту ночь летим стрелой к началу...'.format(user),
                '{}, захватите с собой немного здравого смысла...'.format(user),
                '{}...\nИли просто - Царь.'.format(user), '{} присоединился к вечеринке!'.format(user),
                'Это птица? Это самолёт? Нет!\nЭто {} влетел в нашу дверь! И именно он будет покупать новую.'.format(
                    user), 'Ещё никогда {} не был так близок к провалу,\nрешив незаметно войти на сервер.'.format(user),
                'Никто:\nАбсолютно никто:\n{}: МНЕ СКАЗАЛИ ЧТО ТУТ ЕСТЬ ФУРРРИ!'.format(user))

            message_channel = self.bot.get_channel(767819023178006569)
            embed = discord.Embed(description=f'{random.choice(JoinMessages)}',
                                  color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                               random.randint(1, 255)))
            embed.set_author(name='Приветствуем!', icon_url=member.avatar_url)
            embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
                             icon_url=self.bot.user.avatar_url)
            await message_channel.send(embed=embed)
        else:
            pass


def setup(bot):
    bot.add_cog(OnMemberJoinCog(bot))
