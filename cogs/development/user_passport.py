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
        msg = await ctx.reply("`Печатаем паспорт, пожалуйста, подождите. . .`\n`Это можент занять некоторое время.`")
        # start_time = time.time()
        member = ctx.author
        warns = client.YukkiModeration.WarnCollection.find_one({"_id": member.id})
        flags = member.public_flags

        def is_hs_balance():
            if flags.hypesquad_balance:
                return "./pillow/badges/hs_balance.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_hs_brilliance():
            if flags.hypesquad_brilliance:
                return "./pillow/badges/hs_brilliance.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_hs_bravery():
            if flags.hypesquad_bravery:
                return "./pillow/badges/hs_bravery.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_boost_badge():
            if member.premium_since:
                return "./pillow/badges/booster.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_partner():
            if flags.partner:
                return "./pillow/badges/partner.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_supporter():
            if flags.early_supporter:
                return "./pillow/badges/supporter.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_bot_developer():
            if flags.verified_bot_developer or flags.early_verified_bot_developer:
                return "./pillow/badges/dev.png"
            else:
                return "./pillow/badges/none_badge.png"

        def is_nitro_badge():
            if member.premium_since:
                return "./pillow/badges/nitro.png"
            else:
                return "./pillow/badges/none_badge.png"

        # ==============================================================

        def is_warn():
            if warns:
                return len(warns['warns'])
            else:
                return "0"

        def is_boost():
            if member.premium_since:
                return f'{member.premium_since.strftime("%d/%m/%Y")}'
            else:
                return 'Не спонсирует'

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

        # Автарка пользователя
        avatar_url = str(member.avatar_url)[:-10]
        avatar_url = requests.get(avatar_url, stream=True)
        avatar = Image.open(io.BytesIO(avatar_url.content))
        avatar = avatar.convert('RGBA')
        # Размер аватара
        avatar = avatar.resize((90, 90))

        # Серверная иконка
        icon_url = str(ctx.guild.icon_url)[:-10]
        icon_url = requests.get(icon_url, stream=True)
        server_icon = Image.open(io.BytesIO(icon_url.content))
        server_icon = server_icon.convert('RGBA')
        # Размер иконки
        server_icon = server_icon.resize((50, 50))

        # Значки профиля
        hs_balance_url = is_hs_balance()
        hs_balance = Image.open(hs_balance_url)
        hs_balance = hs_balance.convert('RGBA')
        draw_hs_balance = ImageDraw.Draw(hs_balance)

        hs_brilliance_url = is_hs_brilliance()
        hs_brilliance = Image.open(hs_brilliance_url)
        hs_brilliance = hs_brilliance.convert('RGBA')
        draw_hs_brilliance = ImageDraw.Draw(hs_brilliance)

        hs_bravery_url = is_hs_bravery()
        hs_bravery = Image.open(hs_bravery_url)
        hs_bravery = hs_bravery.convert('RGBA')
        draw_hs_bravery = ImageDraw.Draw(hs_bravery)

        partner_url = is_partner()
        partner = Image.open(partner_url)
        partner = partner.convert('RGBA')
        draw_partner = ImageDraw.Draw(partner)

        supporter_url = is_supporter()
        supporter = Image.open(supporter_url)
        supporter = supporter.convert('RGBA')
        draw_supporter = ImageDraw.Draw(supporter)

        bot_developer_url = is_bot_developer()
        bot_developer = Image.open(bot_developer_url)
        bot_developer = bot_developer.convert('RGBA')
        draw_bot_developer = ImageDraw.Draw(bot_developer)

        boost_badge_url = is_boost_badge()
        boost_badge = Image.open(boost_badge_url)
        boost_badge = boost_badge.convert('RGBA')
        draw_boost_badge = ImageDraw.Draw(boost_badge)

        nitro_badge_url = is_nitro_badge()
        nitro_badge = Image.open(nitro_badge_url)
        nitro_badge = nitro_badge.convert('RGBA')
        draw_nitro_badge = ImageDraw.Draw(nitro_badge)

        # Фон профиля
        background_url = checkTopRole()
        background = Image.open(background_url)
        background = background.convert('RGBA')

        # Маска и отрисовка
        # Аватар
        avatar_mask = Image.new('L', (250, 230), 0)
        draw_avatar = ImageDraw.Draw(avatar_mask)
        draw_avatar.ellipse((0, 0) + (250, 230), fill=255)
        avatar_mask = avatar_mask.resize((90, 90))
        avatar.putalpha(avatar_mask)
        # Иконка
        ico_mask = Image.new('L', (250, 250), 0)
        draw_ico = ImageDraw.Draw(ico_mask)
        draw_ico.ellipse((0, 0) + (150, 150), fill=255)
        ico_mask = ico_mask.resize((50, 50))
        server_icon.putalpha(ico_mask)

        draw_background = ImageDraw.Draw(background)

        # Шрифты
        headline_username = ImageFont.truetype(r".\pillow\fonts\VAG World.otf", size=25)
        headline_copyright = ImageFont.truetype(r".\pillow\fonts\BlenderPro-Book.ttf", size=25)
        other = ImageFont.truetype(r".\pillow\fonts\Slot Cyrillic.ttf", size=23)
        actvity = ImageFont.truetype(r".\pillow\fonts\Slot Cyrillic.ttf", size=21)

        # Тексты
        text_username = draw_background.text((312, 48), f'{member.name}#{member.discriminator}', anchor="ms",
                                             font=headline_username, fill='#FFFFFF')
        text_copyright = draw_background.text((950, 48), f'{ctx.guild.name}', anchor="ms", font=headline_copyright,
                                              fill='#FFFFFF')
        text_nitro = draw_background.text((147, 447), f'{is_boost()}', anchor="ms", font=other, fill="#FFFFFF")
        text_joined = draw_background.text((115, 252), f'{member.joined_at.strftime("%d/%m/%Y")}', anchor="ms",
                                           font=other,
                                           fill="#FFFFFF")
        text_account_registered = draw_background.text((115, 300), f'{member.created_at.strftime("%d/%m/%Y")}',
                                                       anchor="ms",
                                                       font=other, fill="#FFFFFF")
        text_id = draw_background.text((123, 350), f'{member.id}', anchor="ms", font=other, fill="#FFFFFF")
        text_nick = draw_background.text((550, 527), f'{is_nick()}', anchor="ms", font=other, fill="#FFFFFF")
        text_activity = draw_background.text((550, 575), f'{is_activity()}', anchor="ms", font=actvity, fill="#FFFFFF")
        text_warns = draw_background.text((905, 447), f"{is_warn()} / 5", anchor="ms", font=actvity, fill="#FFFFFF")

        background = background.resize((1100, 600))

        # Размещение элементов
        background.paste(avatar, (40, 80), avatar)
        background.paste(server_icon, (820, 28), server_icon)
        # РАЗМЕЩЕНИЕ ЗНАЧКОВ
        background.paste(partner, (197, 140), partner)
        background.paste(bot_developer, (233, 140), bot_developer)
        background.paste(supporter, (259, 140), supporter)
        background.paste(hs_balance, (348, 140), hs_balance)
        background.paste(hs_bravery, (376, 141), hs_bravery)
        background.paste(hs_brilliance, (398, 141), hs_brilliance)
        background.paste(boost_badge, (318, 140), boost_badge)

        background.paste(nitro_badge, (290, 141), nitro_badge)

        # Сохранение картинки в буфер обмена
        _buffer = io.BytesIO()
        background.save(_buffer, "png", quality=95)
        _buffer.seek(0)

        if member.id == 679691974663733363:
            await msg.delete()
            await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)

        else:
            if member.top_role is member_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
                # await ctx.send(f"Выполнено за {time.time() - start_time} секунд")
            elif member.top_role is sponsor_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            elif member.top_role is muted_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            elif member.top_role is favourite_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            elif member.top_role is press_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            elif member.top_role is head_tech_spec_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            elif member.top_role is support_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            elif member.top_role is owner_role:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()
            else:
                await ctx.reply(file=discord.File(fp=_buffer, filename=f'{member.name}profile.png'), delete_after=15)
                await msg.delete()


def setup(bot):
    bot.add_cog(UserPassportCog(bot))
