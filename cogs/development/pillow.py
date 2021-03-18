import random
import time

import discord
from Cybernator import Paginator
from discord.ext import commands

import requests
from PIL import Image, ImageFont, ImageDraw
import io

from config import member_activity, bot_initialize


class PillowCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.reply("Укажите пользователя!")
        if member is not None:

            avatar = await member.avatar_url_as(format="png", static_format="png").read()
            avatar = Image.open(avatar)

            #url = str(member.avatar_url)[:-10]
            #url = requests.get(url, stream=True)
            #avatar = Image.open(io.BytesIO(url.content))

            ico = await ctx.guild.icon_url_as(format="png", static_format="png").read()
            server_icon = Image.open(ico)

           # ico = str(ctx.guild.icon_url)[:-10]
           # ico = requests.get(ico, stream=True)
           # server_icon = Image.open(io.BytesIO(ico.content))

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
            random_choice = ("добро пожаловать!", "рады видеть Вас!", "приятного времяпрепровождения!")
            # Шрифты
            headline = ImageFont.truetype(r".\pillow\VAG World.otf", size=70)
            headline2 = ImageFont.truetype(r".\pillow\VAG World.otf", size=50)
            footer = ImageFont.truetype(r".\pillow\BlenderPro-Book.ttf", size=46)
            # Тексты
            idraw.text((718.5, 400), f'{name},', anchor="ms", font=headline, fill='#FFFFFF')
            idraw.text((718.5, 500), f'{random.choice(random_choice)}', anchor="ms", font=headline2, fill='#FFFFFF')
            idraw.text((755.5, 680), f'{ctx.guild.name}', anchor="ms", font=footer, fill='#FFFFFF')
            # Маска для картинки
            draw.ellipse((0, 0) + (250, 230), fill=255)
            draw_ico.ellipse((0, 0) + (100, 100), fill=255)
            # Изменять вместе с размером аватарки
            mask = mask.resize((245, 234))
            ico_mask = ico_mask.resize((150, 150))
            avatar.putalpha(mask)
            server_icon.putalpha(ico_mask)
            # Размер заднего фона (картинки)
            welcome = welcome.resize((1437, 816))
            # Размещение аватара на фоне
            welcome.paste(avatar, (597, 51), avatar)
            welcome.paste(server_icon, (510, 637), server_icon)

            _buffer = io.BytesIO()
            welcome.save(_buffer, "png")
            _buffer.seek(0)

            await ctx.send(file=discord.File(fp=_buffer, filename=f'{member.name}welcome.png'))
            # await ctx.send(f"Выполнено за {time.time() - start_time} секунд")


def setup(bot):
    bot.add_cog(PillowCog(bot))
