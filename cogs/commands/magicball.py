import discord
import random
from discord.ext import commands

from config import magicball_command_aliases, commands_permission


class MagicballCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=magicball_command_aliases)
    @commands.has_any_role(*commands_permission['magicball_command_permission'])
    async def ball(self, ctx, *, message=None):
        member = ctx.author.mention
        if message is None:
            embed = discord.Embed(title="🔮 Магический шар 🧙‍♀️")
            embed.add_field(name="Невозможно получить вопрос",
                            value="{}, Вам необходимо указать вопрос, на который хотите получить ответ.".format(member))
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            answers = [
                "🎃 Секрет... 🕯",
                "🎃 Большие города... Пустые поезда... Ни берега ни дна...\nДа-да, Вы что-то спросили?\nИзвините, отвлеклась... 🕯️",
                "🎃 Несомненно! 🕯️",
                "🎃 Можете быть уверены! 🕯️",
                "🎃 Сомневаюсь в этом... 🕯️",
                "🎃 Спроси позже... 🕯️",
                "🎃 Я думаю, что ты думаешь, что мы думаем, что да. 🕯️",
                "🎃 Хм..... хм........хм......... нет. 🕯️",
                "🎃 Ты заставляешь девушку отвечать и думать за тебя, тебе не стыдно? 🕯️",
                "🎃 Шар временно сдулся, спросите позже. 🕯️",
                "🎃 Я знаю лишь то, что я знаю, и я знаю, что это нет. 🕯️",
                "🎃 Конечно, что за вопрос? 🕯️",
                "🎃 Конечно, нет) 🕯️",
                "🎃 Просто нет. Вот и все! 🕯️",
                "🎃 Дай мне 5 минуточек на раздумье. 🕯️",
                "🎃 Нууу... затрудняюсь ответить. 🕯️",
                "🎃 А ты?/А тебе? 🕯️",
                "🎃 Точно да. 🕯️",
                "🎃 Точно нет. 🕯️",
                "🎃 Не точно. 🕯️",
                "🎃 Хочу спатки... сам отвечай себе. 🕯️",
                "🎃 Умри. Хватит меня спрашивать. 🕯️",
                "🎃 Перефразируй вопрос. 🕯️",
                "🎃 Лучше бы ты не спрашивал об этом.... 🕯️",
                "🎃 Спроси другое... 🕯️",
                "🎃 Верь мне, это 100% да. 🕯️",
                "🎃 Я не отвечаю таким дуракам как ты. 🕯️",
                "🎃 Мейби. 🕯️",
                "🎃 Ответ на этот вопрос ты найдешь в песнях Гражданской Обороны. 🕯️",
                "🎃 Я не хочу тебя расстраивать, а нет хочу! Ответ положительный. 🕯️",
                "🎃 Ответ отрицательный. 🕯️",
                "🎃 Авадакедабра! Ты умер! Нет человека, нет вопроса, а значит и отвечать не надо) 🕯️",
                "🎃 Мне лень думать, но я думаю нет. 🕯️",
                "🎃 Мхм 🕯️",
                "🎃 Угу. 🕯️",
                "🎃 Не-а! 🕯️",
                "🎃 Ахахахаха, смешной вопрос, на который я не знаю ответа. 🕯️",
                "🎃 Серьезно? Кто такое задает? 🕯️",
                "🎃 Зуб даю, папой клянусь, что да! 🕯️",
                "🎃 Нет-неееееет-неа-не-а. 🕯️",
                "🎃 Ноуп. 🕯️",
                "🎃 Yes! 🕯️",
                "🎃 Так... сложный вопрос... надо подумать... задай позже. 🕯️",
                "🎃 Все возможно.... 🕯️",
                "🎃 Я таким как ты не отвечаю. 🕯️",
                "🎃 Дыыыы :3 🕯️",
                "🎃 Я не знаю, ответ на этот вопрос, но знаю точно, что кое-кто - зоофил. 🕯️",
                "🎃 Ответ: Вряд ли. 🕯️",
                "🎃 Навряд ли. 🕯️",
                "🎃 Да? Я не уверенна. 🕯️",
                "🎃 Хочу, чтобы ответ был «нет», если это не так, не моя проблема! 🕯️",
                "🎃 Я с тобой согласна. 🕯️",
                "🎃 Так оно и есть. 🕯️",
                "🎃 Невозможно. 🕯️",
                "🎃 Ты о чем?) 🕯️",
                "🎃 Нет 🕯️",
                "🎃 Я подумаю над этим вопросом. 🕯️",
                "🎃 Да. 🕯️",
                "🎃 Знаешь, я думаю тебе стоит не задавать такие вопросы. 🕯️",
                "🎃 Бог покинул тебя. 🕯️",
                "🎃 Не сомневаюсь в этом, а ты сомневайся. 🕯️",
                "🎃 Думаю, да. 🕯️",
                "🎃 Думаю, нет. 🕯️",
                "🎃 Может быть... 🕯️",
                "🎃 Определенно. 🕯️",
                "🎃 Не знаю. 🕯️",
                "🎃 Не знаю и знать не хочу. 🕯️",
                "🎃 Сам подумай. 🕯️",
                "🎃 Взгляни глубоко в себя и сам найди ответ на свой вопрос. 🕯️",
                "🎃 Чтобы узнать ответ на вопрос, заплати мне 10 долларов. 🕯️",
                "🎃 А тебе оно надо? 🕯️",
                "🎃 По моему скромному мнению, которое очень важно учитывать в данном контексте, поскольку я решаю, что за ответ будет на данный вопрос, я с уверенностью могу утвердить то, что мой ответ да. 🕯️",
                "🎃 По моему скромному мнению, которое очень важно учитывать в данном контексте, поскольку я решаю, что за ответ будет на данный вопрос, я с уверенностью могу утвердить то, что мой ответ нет. 🕯️",
                "🎃 По моему скромному мнению, которое очень важно учитывать в данном контексте, поскольку я решаю, что за ответ будет на данный вопрос, я с уверенностью могу утвердить то, что мой ответ «я не знаю». 🕯️",
                "🎃 Мой ответ: 4. 🕯️",
                "🎃 Спроси у другого человека, существо. 🕯️",
                "🎃 Хз. 🕯️",
                "🎃 Нет. Определенно нет. 🕯️",
                "🎃 ДА ДА ДА! 🕯️",
                "🎃 Умей задавать правильные вопросы. 🕯️",
                "🎃 Не хочу тебя огорчать, но я сомневаюсь в этом. 🕯️",
                "🎃 Да. Это железное «Да». 🕯️",
                "🎃 Почему ты спрашиваешь это? 🕯️",
                "🎃 Хм, расчитывай на это. 🕯️",
                "🎃 Хм......... Нет. 🕯️",
                "🎃 А почему бы и нет? 🕯️",
                "🎃 А почему бы и да. 🕯️",
                "🎃 Спроси, что-нибудь другое... 🕯️",
                "🎃 Ангелы с небес пролили свет на ответ «Да». 🕯️",
                "🎃 Может быть, да. 🕯️",
                "🎃 Да нет. 🕯️",
                "🎃 Нет да. 🕯️",
                "🎃 Извините, я до сих пор высчитываю ваш ответ. 🕯️",
                "🎃 Знать не знаю, но спроси моего папу, он точно знает. 🕯️",
                "🎃 Я знаю, что ты хочешь, чтобы ответ был «Да», но ответ «Нет». 🕯️",
                "🎃 Я знаю, что ты хочешь, чтобы ответ был «Нет», но ответ «Да». 🕯️",
                "🎃 Я котик, у меня лапки! А котики не знают. 🕯️",
                "🎃 Великое «Может быть!» 🕯️",
                "🎃 Няяя! То-есть, дааа! 🕯️",
                "🎃 Окей. Как скажешь. Я вообще не при делах. 🕯️",
                "🎃 NOOOOOOO! 🕯️",
                "🎃 Ну, ну! 🕯️",
                "🎃 Верь в это. 🕯️",
                "🎃 Дыа. 🕯️",
                "🎃 Не знаю, но думаю, что ты не имеешь права спрашивать об этом. 🕯️"
            ]

            embed = discord.Embed(
                title="🔮 Магический шар 🧙‍♀️",
                description=random.choice(answers),
                color=0xf5ce42  # Цвет эмбеда
            )
            embed.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены',
                             icon_url=self.bot.user.avatar_url)

            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(MagicballCog(bot))
