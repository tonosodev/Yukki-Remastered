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
        img = Image.open(r".\pillow\infoimgimg.png")  # READY
        start_time = time.time()
        # user_img = str(member.avatar_url)[:-10]

        # resp = requests.get(user_img, stream=True)
        # resp = Image.open(io.BytesIO(resp.content))
        # resp = resp.convert("RGBA")
        # resp = resp.resize((60, 60), Image.ANTIALIAS)
        # img.paste(resp, (15, 15, 115, 115))  # user avatar

        #member_passport_embed_general = discord.Embed(title="debug")
        #member_passport_embed_general.set_image(f=r".\pillow\members\id{}.png".format(str(member.id)))

        if member is None:
            await ctx.reply("Укажите пользователя!")
        if member is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(r".\pillow\Modern_Sans_Light.otf", 100)
            fontbig = ImageFont.truetype(r".\pillow\Fitamint Script.ttf", 400)
            #    (x,y)::↓ ↓ ↓ (text)::↓ ↓ (r,g,b)::↓ ↓ ↓
            draw.text((200, 0), "Information:", (255, 255, 255), font=fontbig)  # draws Information
            draw.text((50, 500), "Username: {}".format(member.mention), (255, 255, 255),
                      font=font)  # draws the Username of the user
            draw.text((50, 700), "ID:  {}".format(member.id), (255, 255, 255), font=font)  # draws the user ID
            draw.text((50, 900), "User Status:{}".format(member.status), (255, 255, 255),
                      font=font)  # draws the user status
            draw.text((50, 1100), "Account created: {}".format(member.created_at), (255, 255, 255),
                      font=font)  # When the account was created
            draw.text((50, 1300), "Nickname:{}".format(member.display_name), (255, 255, 255),
                      font=font)  # Nickname of the user
            draw.text((50, 1500), "Users' Top Role:{}".format(member.top_role), (255, 255, 255),
                      font=font)  # draws the top rome
            draw.text((50, 1700), "User Joined:{}".format(member.joined_at), (255, 255, 255),
                      font=font)  # draws info about when the user joined
            img.save(r".\pillow\members\id{}.png".format(str(member.id)))
            await ctx.send(file=discord.File(fp=r".\pillow\members\id{}.png".format(str(member.id))))
            await ctx.send(f"Выполнено за {time.time() - start_time} секунд")

def setup(bot):
    bot.add_cog(PillowCog(bot))
