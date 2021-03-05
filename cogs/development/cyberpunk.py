import time
from io import BytesIO

import discord
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands


class CyberpunkCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cyberpunk(self, ctx, *, arg):
        start_time = time.time()
        if arg != '':
            def cyberp(x):
                global img
                img = Image.open(r".\pillow\photo.png")
                font = ImageFont.truetype(r".\pillow\BlenderPro-Book.ttf", 35)
                text = ImageDraw.Draw(img)
                pos = [150, 225]
                userText = x
                userText = userText.replace("\\n", "\n")
                userText = userText.replace("\\t", "\t")
                value = 0
                for i in userText:
                    text.text((pos[0], pos[1]), i, font=font, fill=('#000000'))
                    pos[0] += 20
                    value += 1
                    if value == 85:
                        pos[0] = 150
                        pos[1] += 50
                        value = 0
                pos[0] = 150
                pos[1] += 50

            cyberp(arg)
            output = BytesIO()
            img.save(output, 'png')
            image_pix = BytesIO(output.getvalue())
            await ctx.reply(file=discord.File(fp=image_pix, filename='pix_ava.png'))
            await ctx.send(f"Выполнено за {time.time() - start_time} секунд")
        else:
            await ctx.reply("вы не ввели текст!")


def setup(bot):
    bot.add_cog(CyberpunkCog(bot))
