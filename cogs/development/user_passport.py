"""
Today is 3/18/2021
Session by: https://github.com/DevilDesigner
Create Time: 10:57 AM
This Class: user_passport
"""
import io
import discord
import requests
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
from loguru import logger
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://NeverMind:3Ctj5eEMI0vzwRY8@nevermindcluster.hfbwn.mongodb.net/YukkiModeration?retryWrites=true&w=majority")


class UserPassportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog UserPassports loaded!")

    @commands.command(aliases=['паспорт'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def passport(self, ctx, ):
        msg = await ctx.reply("`Печатаем паспорт, пожалуйста, подождите. . .`")
        # start_time = time.time()
        member = ctx.author
        warns = client.YukkiModeration.WarnCollection.find_one({"_id": member.id})

        def is_warn():
            if warns:
                return len(warns['warns'])
            else:
                return "0"

        def is_nitro():
            if member.premium_since:
                return f'{member.premium_since.strftime("%d/%m/%Y")}'
            else:
                return 'Подписка отсутствует'

        def is_nick():
            if member.nick:
                return f'{member.nick}'
            else:
                return f'{member.name}'

        def is_activity():
            desc = ""
            if not member.activity:
                desc += 'Отсутствует'
            else:
                current_activity = member.activities[0]
                if current_activity.type:
                    if current_activity.type == discord.ActivityType.listening and not isinstance(current_activity,
                                                                                                  discord.Spotify):
                        desc += "Прослушивает музыку"

                    elif current_activity.type == discord.ActivityType.listening and isinstance(current_activity,
                                                                                                discord.Spotify):
                        desc += f"Слушает Spotify - композиция '{current_activity.title}' от '{', '.join(current_activity.artists)}'"


                    elif current_activity.type == discord.ActivityType.watching:
                        desc += "Просматривает трансляцию"

                    else:
                        desc += f"Статус: {current_activity.name} | Создан: {current_activity.created_at.strftime('%d-%m-%Y')}"
            return desc

        # ROLES
        owner_role = 766231587104620554
        support_role = 766233124681547776
        head_tech_spec_role = 766293535832932392
        press_role = 818715004671885314
        favourite_role = 773291689514106920
        muted_role = 802170065860296744
        sponsor_role = 791227395331457047
        member_role = 766232996285775903

        # PERSONAL MEMBER PASSPORT
        member_jabka_id = 679691974663733363

        def checkTopRole():
            if member.id == member_jabka_id:
                return "./pillow/profiles/jabka_profile.png"
            if member.top_role.id == member_role:
                return "./pillow/profiles/member_profile.png"
            elif member.top_role.id == sponsor_role:
                return "./pillow/profiles/sponsor_profile.png"
            elif member.top_role.id == muted_role:
                return "./pillow/profiles/muted_profile.png"
            elif member.top_role.id == favourite_role:
                return "./pillow/profiles/favourite_profile.png"
            elif member.top_role.id == press_role:
                return "./pillow/profiles/press_profile.png"
            elif member.top_role.id == head_tech_spec_role:
                return "./pillow/profiles/tech_spec_profile.png"
            elif member.top_role.id == support_role:
                return "./pillow/profiles/support_profile.png"
            elif member.top_role.id == owner_role:
                return "./pillow/profiles/owner_profile.png"
            else:
                return "./pillow/profiles/member_profile.png"

        url = str(member.avatar_url)[:-10]
        url = requests.get(url, stream=True)
        avatar = Image.open(io.BytesIO(url.content))

        ico = str(ctx.guild.icon_url)[:-10]
        ico = requests.get(ico, stream=True)
        server_icon = Image.open(io.BytesIO(ico.content))

        img_source = checkTopRole()

        welcome = Image.open(img_source)
        welcome = welcome.convert('RGBA')
        avatar = avatar.convert('RGBA')

        server_icon = server_icon.convert('RGBA')
        # Размер аватарки
        avatar = avatar.resize((90, 90))
        server_icon = server_icon.resize((50, 50))
        # Маска
        mask = Image.new('L', (250, 230), 0)
        ico_mask = Image.new('L', (250, 250), 0)
        draw = ImageDraw.Draw(mask)
        draw_ico = ImageDraw.Draw(ico_mask)
        idraw = ImageDraw.Draw(welcome)

        # Шрифты
        headline_username = ImageFont.truetype(r".\pillow\fonts\VAG World.otf", size=25)
        headline_copyright = ImageFont.truetype(r".\pillow\fonts\BlenderPro-Book.ttf", size=25)
        other = ImageFont.truetype(r".\pillow\fonts\Slot Cyrillic.ttf", size=23)
        actvity = ImageFont.truetype(r".\pillow\fonts\Slot Cyrillic.ttf", size=21)
        # Тексты
        text_username = idraw.text((312, 48), f'{member.name}#{member.discriminator}', anchor="ms",
                                   font=headline_username, fill='#FFFFFF')
        text_copyright = idraw.text((950, 48), f'{ctx.guild.name}', anchor="ms", font=headline_copyright,
                                    fill='#FFFFFF')
        text_nitro = idraw.text((147, 447), f'{is_nitro()}', anchor="ms", font=other, fill="#FFFFFF")
        text_joined = idraw.text((115, 252), f'{member.joined_at.strftime("%d/%m/%Y")}', anchor="ms", font=other,
                                 fill="#FFFFFF")
        text_account_registered = idraw.text((115, 300), f'{member.created_at.strftime("%d/%m/%Y")}', anchor="ms",
                                             font=other, fill="#FFFFFF")
        text_id = idraw.text((123, 350), f'{member.id}', anchor="ms", font=other, fill="#FFFFFF")
        text_nick = idraw.text((550, 527), f'{is_nick()}', anchor="ms", font=other, fill="#FFFFFF")
        text_activity = idraw.text((550, 575), f'{is_activity()}', anchor="ms", font=actvity, fill="#FFFFFF")
        text_warns = idraw.text((905, 447), f"{is_warn()} / 5", anchor="ms", font=actvity, fill="#FFFFFF")

        # Маска для картинки
        draw.ellipse((0, 0) + (250, 230), fill=255)
        draw_ico.ellipse((0, 0) + (150, 150), fill=255)
        # Изменять вместе с размером аватарки
        mask = mask.resize((90, 90))
        ico_mask = ico_mask.resize((50, 50))
        avatar.putalpha(mask)
        server_icon.putalpha(ico_mask)
        # Размер заднего фона (картинки)
        welcome = welcome.resize((1100, 600))
        # Размещение аватара на фоне
        welcome.paste(avatar, (40, 80), avatar)
        welcome.paste(server_icon, (820, 28), server_icon)
        # Сохранение картинки из буфера
        _buffer = io.BytesIO()
        welcome.save(_buffer, "png", quality=95)
        _buffer.seek(0)

        if member.id == 679691974663733363:
            await msg.delete()
            await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)

        else:
            if member.top_role is member_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                # await ctx.send(f"Выполнено за {time.time() - start_time} секунд")
            elif member.top_role is sponsor_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            elif member.top_role is muted_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            elif member.top_role is favourite_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            elif member.top_role is press_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            elif member.top_role is head_tech_spec_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            elif member.top_role is support_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            elif member.top_role is owner_role:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
            else:
                await msg.delete()
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)


def setup(bot):
    bot.add_cog(UserPassportCog(bot))
