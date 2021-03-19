import discord
import random
import requests
import io
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw


class OnMemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id == 766213910595633153:
            role = discord.utils.get(member.guild.roles, id=768118967759405056)
            await member.add_roles(role)
            user = member.mention
            message_channel = self.bot.get_channel(767819023178006569)

            url = str(member.avatar_url)[:-10]
            url = requests.get(url, stream=True)
            avatar = Image.open(io.BytesIO(url.content))

            ico = str(self.bot.get_guild(766213910595633153).icon_url)[:-10]
            ico = requests.get(ico, stream=True)
            server_icon = Image.open(io.BytesIO(ico.content))

            welcome = Image.open(r".\pillow\hi_pillow.png")
            welcome = welcome.convert('RGBA')
            avatar = avatar.convert('RGBA')

            server_icon = server_icon.convert('RGBA')
            # Размер аватарки
            avatar = avatar.resize((245, 234))
            server_icon = server_icon.resize((150, 150))
            # Маска
            mask = Image.new('L', (250, 230), 0)
            ico_mask = Image.new('L', (250, 230), 0)

            draw = ImageDraw.Draw(mask)
            draw_ico = ImageDraw.Draw(ico_mask)

            idraw = ImageDraw.Draw(welcome)
            name = member.name
            # tag = member.discriminator
            at = member.created_at
            random_choice = ("добро пожаловать!",
                             "рады видеть Вас!",
                             "приятного времяпрепровождения!",
                             'вот Вас то мы и ждали!', 'проходите, не стесняйтесь!', 'располагайтесь!',
                             'или просто - Царь.', 'что нового расскажете?', 'улыбнись!', 'мяяя! :3',
                             'был их тех, кто просто любит жизнь...')
            # Шрифты
            headline = ImageFont.truetype(r".\pillow\VAG World.otf", size=70)
            headline2 = ImageFont.truetype(r".\pillow\VAG World.otf", size=45)
            footer = ImageFont.truetype(r".\pillow\BlenderPro-Book.ttf", size=46)
            # Тексты
            idraw.text((718.5, 400), f'{name},', anchor="ms", font=headline, fill='#FFFFFF')
            idraw.text((718.5, 500), f'{random.choice(random_choice)}', anchor="ms", font=headline2, fill='#FFFFFF')
            idraw.text((755.5, 680), f'{self.bot.get_guild(766213910595633153).name}', anchor="ms", font=footer,
                       fill='#FFFFFF')
            # Маска для картинки
            draw.ellipse((0, 0) + (250, 230), fill=255)
            draw_ico.ellipse((0, 0) + (100, 100), fill=255)
            # Изменять вместе с размером аватарки
            mask = mask.resize((245, 234))
            ico_mask = ico_mask.resize((150, 150))
            avatar.putalpha(mask)
            server_icon.putalpha(ico_mask)
            # Размер заднего фона
            welcome = welcome.resize((1437, 816))
            # Размещение аватара на фоне
            welcome.paste(avatar, (597, 51), avatar)
            welcome.paste(server_icon, (510, 637), server_icon)

            _buffer = io.BytesIO()
            welcome.save(_buffer, "png", quality=95)
            _buffer.seek(0)


            await message_channel.send(f"__**Приветствуем нового участника**__: {member.mention}!",
                                       file=discord.File(fp=_buffer, filename=f'{member.name}welcome.png'))

            # JoinMessages = (
            #    '{} здравствуй!\nПоддержите команду - позовите друзей, знакомых, близких, захватите с собой еще кота...'.format(
            #        user),
            #    '{}, ну, жалуйтесь...'.format(user), '{}, проходите, не стесняйтесь!'.format(user),
            #    '{} мы в Вашем распоряжении.'.format(user),
            #    '{} был из тех, кто просто любит жизнь...'.format(user),
            #    '{} присоединяясь обещал, что матершинные слова не будет он употре...\n...блять.'.format(user),
            #    '{}, располагайтесь, мы здесь не кусаемся! 💜'.format(user), '{}, рады видеть Вас!'.format(user),
            #    '{} доброго времени суток!'.format(user),
            #    '{} проскальзывает на сервер.'.format(user), '{}, кажется, принёс нам пиццу!'.format(user),
            #    'Вот это врыв!\n{}, это было превосходно!'.format(user), '{} - Вы прекрасны.'.format(user),
            #    '{}, мя! 💕'.format(user), 'Последняя надежда человечества, {}, присоеденился!'.format(user),
            #    '{}, заходи, не бойся - находясь не плачь...'.format(user),
            #    '{}?\nЛюбопытно...'.format(user), '{}, улыбнись! 😸'.format(user),
            #    '{}, добро пожаловать на борт!'.format(user), 'Что нового расскажете, {}?'.format(user),
            #    'Это же тот самый {}, который всегда приходит с пустыми руками!'.format(user),
            #    '{}, захватите с собой немного здравого смысла...'.format(user),
            #    '{}...\nИли просто - Царь.'.format(user), '{} присоединился к вечеринке!'.format(user),
            #    'Это птица? Это самолёт? Нет!\nЭто {} влетел в нашу дверь! И именно он будет покупать новую.'.format(
            #        user), 'Ещё никогда {} не был так близок к провалу,\nрешив незаметно войти на сервер.'.format(user),
            #    'Никто:\nАбсолютно никто:\n{}: МНЕ СКАЗАЛИ ЧТО ТУТ ЕСТЬ ФУРРРИ!'.format(user))

            # embed = discord.Embed(description=f'{random.choice(JoinMessages)}',
            #                      color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
            #                                                   random.randint(1, 255)))
            # embed.set_author(name='Приветствуем!', icon_url=member.avatar_url)
            # embed.set_footer(text=f'{self.bot.user.name}' + bot_initialize['embeds_footer_message'],
            #                 icon_url=self.bot.user.avatar_url)
            # await message_channel.send(embed=embed)
        else:
            pass


def setup(bot):
    bot.add_cog(OnMemberJoinCog(bot))
