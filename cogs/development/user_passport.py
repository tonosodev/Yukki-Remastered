"""
Today is 3/18/2021
Session by: https://github.com/DevilDesigner
Create Time: 10:57 AM
This Class: user_passport
"""
import io
import time

import discord
import requests
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
from loguru import logger


class UserPassportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Cog UserPassport loaded!")


    @commands.command(aliases=[''])
    async def passport(self, ctx, member: discord.Member = None):
        msg = await ctx.reply("`Печатаем паспорт, пожалуйста, подождите. . .`")

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
            # elif member.activity.name:
            #   desc += f'{member.activity.name}'
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
                        desc += f"Пользовательский статус: {current_activity.name} | Создан: {current_activity.created_at.strftime('%d-%m-%Y')}"
            return desc

        yukki_role = ctx.guild.get_role(766284632769036318)
        owner_role = ctx.guild.get_role(766231587104620554)
        support_role = ctx.guild.get_role(766233124681547776)
        head_tech_spec_role = ctx.guild.get_role(766293535832932392)
        press_role = ctx.guild.get_role(818715004671885314)
        favourite_role = ctx.guild.get_role(773291689514106920)
        muted_role = ctx.guild.get_role(802170065860296744)
        sponsor_role = ctx.guild.get_role(791227395331457047)
        member_role = ctx.guild.get_role(766232996285775903)

        try:
            if member is None:
                member = ctx.author

                url = str(member.avatar_url)[:-10]
                url = requests.get(url, stream=True)
                avatar = Image.open(io.BytesIO(url.content))

                ico = str(ctx.guild.icon_url)[:-10]
                ico = requests.get(ico, stream=True)
                server_icon = Image.open(io.BytesIO(ico.content))

                img_source = r".\pillow\profiles\member_profile.png"
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

                # tag = member.discriminator
                at = member.created_at
                # Шрифты
                headline_username = ImageFont.truetype(r".\pillow\VAG World.otf", size=25)
                headline_copyright = ImageFont.truetype(r".\pillow\BlenderPro-Book.ttf", size=25)
                other = ImageFont.truetype(r".\pillow\Slot Cyrillic.ttf", size=23)
                actvity = ImageFont.truetype(r".\pillow\Slot Cyrillic.ttf", size=21)
                # Тексты
                text_username = idraw.text((312, 48), f'{member.name}#{member.discriminator}', anchor="ms",
                                           font=headline_username, fill='#FFFFFF')
                text_copyright = idraw.text((950, 48), f'{ctx.guild.name}', anchor="ms", font=headline_copyright,
                                            fill='#FFFFFF')
                text_nitro = idraw.text((147, 447), f'{is_nitro()}', anchor="ms", font=other, fill="#FFFFFF")
                text_joined = idraw.text((115, 252), f'{member.joined_at.strftime("%d/%m/%Y")}', anchor="ms", font=other, fill="#FFFFFF")
                text_account_registered = idraw.text((115, 300), f'{member.created_at.strftime("%d/%m/%Y")}', anchor="ms", font=other, fill="#FFFFFF")
                text_id = idraw.text((123, 350), f'{member.id}', anchor="ms", font=other, fill="#FFFFFF")
                text_nick = idraw.text((552, 527), f'{is_nick()}', anchor="ms", font=other, fill="#FFFFFF")
                text_activity = idraw.text((552, 575), f'{is_activity()}', anchor="ms", font=actvity, fill="#FFFFFF")

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

                _buffer = io.BytesIO()
                welcome.save(_buffer, "png", quality=95)
                _buffer.seek(0)

                if member.top_role is member_role:
                    start_time = time.time()
                    await msg.delete()
                    await ctx.send(file=discord.File(fp=_buffer, filename=f'{member.name}welcome.png'))
                    await ctx.send(f"Выполнено за {time.time() - start_time} секунд")
                elif member.top_role is sponsor_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {sponsor_role}')
                elif member.top_role is muted_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {muted_role}')
                elif member.top_role is favourite_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {favourite_role}')
                elif member.top_role is press_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {press_role}')
                elif member.top_role is head_tech_spec_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {head_tech_spec_role}')
                elif member.top_role is support_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {support_role}')
                elif member.top_role is owner_role:
                    await msg.delete()
                    await ctx.send(f'Ваша роль: {owner_role.mention}')
                else:
                    await msg.delete()
                    await ctx.send(
                        f'**Нам не удалось напечатать Ваш паспорт...**\n'
                        f'`Ваша васшая роль не поддерживается.`\n\n'
                        f'__Обратитесь к техническим специалистам.__')

            else:
                url = str(member.avatar_url)[:-10]
                url = requests.get(url, stream=True)
                avatar = Image.open(io.BytesIO(url.content))

                ico = str(ctx.guild.icon_url)[:-10]
                ico = requests.get(ico, stream=True)
                server_icon = Image.open(io.BytesIO(ico.content))

                welcome = Image.open(r".\pillow\member_profile.png")
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

                # tag = member.discriminator
                at = member.created_at
                # Шрифты
                headline = ImageFont.truetype(r".\pillow\VAG World.otf", size=70)
                full_username = ImageFont.truetype(r".\pillow\VAG World.otf", size=50)
                footer = ImageFont.truetype(r".\pillow\BlenderPro-Book.ttf", size=46)
                # Тексты
                text_line_1 = idraw.text((718.5, 400), f'{member.name}#{member.discriminator}', anchor="ms",
                                         font=headline, fill='#FFFFFF')
                text_line_2 = idraw.text((755.5, 510), f'{ctx.guild.name}', anchor="ms", font=footer, fill='#FFFFFF')
                # Маска для картинки
                draw.ellipse((0, 0) + (250, 230), fill=255)
                draw_ico.ellipse((0, 0) + (150, 150), fill=255)
                # Изменять вместе с размером аватарки
                mask = mask.resize((245, 234))
                ico_mask = ico_mask.resize((150, 150))
                avatar.putalpha(mask)
                server_icon.putalpha(ico_mask)
                # Размер заднего фона (картинки)
                welcome = welcome.resize((1100, 600))
                # Размещение аватара на фоне
                welcome.paste(avatar, (597, 51), avatar)
                welcome.paste(server_icon, (510, 637), server_icon)

                _buffer = io.BytesIO()
                welcome.save(_buffer, "png", quality=95)
                _buffer.seek(0)

            if member.top_role is member_role:
                await msg.delete()
                await ctx.send(file=discord.File(fp=_buffer, filename=f'{member.name}welcome.png'))
                await ctx.send(f'Ваша роль: {member_role}')
            elif member.top_role is sponsor_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {sponsor_role}')
            elif member.top_role is muted_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {muted_role}')
            elif member.top_role is favourite_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {favourite_role}')
            elif member.top_role is press_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {press_role}')
            elif member.top_role is head_tech_spec_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {head_tech_spec_role}')
            elif member.top_role is support_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {support_role}')
            elif member.top_role is owner_role:
                await msg.delete()
                await ctx.send(f'Ваша роль: {owner_role.mention}')
            elif member.top_role is yukki_role:
                await msg.delete()
                await ctx.send(f'Это же я! Хе-хе...')
            else:
                await msg.delete()
                await ctx.send(
                    f'**Нам не удалось напечатать паспорт **{member.name}**...**\n'
                    f'`Высшая роль пользователя не поддерживается.`\n\n')

        except Exception as e:
            pass


def setup(bot):
    bot.add_cog(UserPassportCog(bot))
