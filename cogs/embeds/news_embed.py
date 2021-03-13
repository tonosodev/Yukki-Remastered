"""
Today is 3/7/2021
Session by: https://github.com/DevilDesigner
Create Time: 8:38 AM
This Class: roles_embed
"""
from datetime import datetime
from discord.ext import commands

from config import commands_permission


class MetaPeaceEmbedsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*commands_permission['server_status_permission'])
    async def news_embed(self, ctx):
        newspaper_role = ctx.guild.get_role(818748991135023125)
        now = datetime.now()
        year = now.strftime("%Y")
        await ctx.message.delete()
        msg = (

            f"<:n3:817941992998305844> **Приветствуем, дорогие участники {ctx.guild.name}**\n"
            "<:n2:817941992864481301> *Мы продолжаем работу над развитием нашего жилища,*\n"
            "<:n2:817941992864481301> *добавляя всё больше интересных возможностей!*\n"
            "<:n2:817941992864481301>\n"

            f"<:n2:817941992864481301> Рады сообщить, что совместными усилиями с <@679691974663733363>...\n"
            "<:n2:817941992864481301> <:online:816332016551329832> `Завершена работа над системой авто-ролей`;\n"
            "<:n2:817941992864481301> <:online:816332016551329832> `Доработана система пользовательских репортов`;\n"
            "\n"
        )
        await ctx.send(
            # Header
            "<:blank:817933141514911754>                  <:wdash:817934436317528125> <:bdash:817934432450773012> <:wdash:817934436317528125> <:bdash:817934432450773012> ƝƐƜS <:bdash:817934432450773012> <:wdash:817934436317528125> <:bdash:817934432450773012> <:wdash:817934436317528125>\n"
            "                           ╰══• ೋ•✧๑♡๑✧•ೋ •══╯\n\n"
            # Body and Description
            + msg +
            # Footer
            f"<a:shard_3:816330981908807711> Рассылка новостей сообщества для {newspaper_role.mention}\n\n"
            "                         ╭══• ೋ•✧๑♡๑✧•ೋ •══╮\n"
            f"<:blank:817933141514911754>                  <:wdash:817934436317528125> <:bdash:817934432450773012> <:wdash:817934436317528125> <:bdash:817934432450773012> {year} <:bdash:817934432450773012> <:wdash:817934436317528125> <:bdash:817934432450773012> <:wdash:817934436317528125>"
        )
        for member in ctx.guild.members:
            if newspaper_role in member.roles:
                try:
                    await member.send(
                        # Header
                        f"<:blank:817933141514911754>\n"
                        f"       ✩｡:•.─────  ❁ **{ctx.guild.name}** ❁  ─────.•:｡✩\n"
                        f"<:blank:817933141514911754>\n"
                        # Body
                        f"" + msg + "\n"
                        # Footer
                                    "Вы получили это оповещение, так как подписаны на рассылку.\n"
                                    "©Licensed MetaPeacePress®\n█║▌│█│║▌║││█║▌║█║▌\n"
                                    "<:blank:817933141514911754>\n")
                except:
                    pass


def setup(bot):
    bot.add_cog(MetaPeaceEmbedsCog(bot))
