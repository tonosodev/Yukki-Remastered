import discord
from discord.ext import commands
import pymongo


class RoleShopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, role: discord.Role = None, ids=None, cost: int = None):
        if not ids:
            emb = discord.Embed(description='Укажите <id> предмета!')
            emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))
            await ctx.send(embed=emb)
        elif not cost:
            emb = discord.Embed(description='Укажите <cost> предмета!')
            emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))
            await ctx.send(embed=emb)

        elif not role:
            emb = discord.Embed(description='Укажите <role> предмета!')
            emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))
            await ctx.send(embed=emb)

        else:

            shop.insert_one({
                "role_id": role.id,
                "ids": ids,
                "cost": cost,
                "guild": ctx.guild.id
            })

            emb = discord.Embed(description=f'Вы успешно добавили {role.mention}')

            emb.add_field(name='ID покупки:', value={ids})
            emb.add_field(name='Цена:', value={cost})
            emb.add_field(name='ID роли:', value=role.id)

            await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_role(self, ctx, role: discord.Role = None):
        if not role:
            emb = discord.Embed(description='Укажите <role> предмета!')
            await ctx.send(embed=emb)
        else:
            shop.remove({"role_id": role.id})

            emb = disocrd.Embed(description=f'Вы успешно удалили {role.mention} из магазина!')
            emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))

            await ctx.send(embed=emb)

    @commands.command()
    async def shop(self, ctx):
        connect = shop.find({"guild": ctx.guild.id})
        emb = discord.Embed(title=f'Магазин ролей сервера {ctx.guild.name}')

        for x in connect:
            ids = x['ids']
            role = x['role_id']
            cost = x['cost']

            if ctx.guild.get_role(role) != None:

                if ctx.guild.get_role(role) in ctx.author.roles:

                    emb.add_field(
                        name=f'| Куплено',
                        value=f'| {ctx.guild.get_role(role).mention}\nㅤㅤㅤ'
                    )

                else:

                    emb.add_field(
                        name=f'| ID: {ids}\n[Sale]   > {cost} :leaves:',
                        value=f'| {ctx.guild.get_role(role).mention}\nㅤㅤㅤ'
                    )

        emb.set_footer(text='Страница 1 из 1 | Напишите `=buy_role <key>` для покупки роли. Пример - `=buy_role key`')
        await ctx.send(embed=emb)

    @commands.command()
    async def buy_role(self, ctx, ids=None):
        if not ids:
            emb = discord.Embed(description='Укажите <id> предмета!')
            await ctx.send(embed=emb)

        else:
            connect = shop.find({"guild": ctx.guild.id})
            for y in connect:
                if ids == y['ids']:
                    balance = db['test']

                for x in balance.find({"_id": ctx.author.id}):

                    if x['cash'] < y['cost']:
                        emb = discord.Embed(description='У вас недостаточно денег!')
                        emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))
                        await ctx.send(embed=emb)
                    else:
                        emb = discord.Embed(
                            description=f'Вы успешно купили роль {ctx.guild.get_role(y["role_id"]).mention}')
                        emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))
                        await ctx.send(embed=emb)

                        result = x['cash'] - y['cost']
                        balance.update_one({"_id": ctx.author.id}, {"$set": {"cash": result}})

                        role = discord.utils.get(ctx.guild.roles, id=y['role_id'])
                        await ctx.author.add_roles(role)
            else:
                emb = discord.Embed(description='Такого ID предмта не существует!')
                emb.set_author(icon_url='{}'.format(ctx.author.avatar_url), name='{}'.format(ctx.author))
                await ctx.send(embed=emb)

    @add_role.error
    async def add_role_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(title='Вы не можете использовать данную команду!',
                                description='Нужные права: `Администратор`')
            await ctx.send(embed=emb)

    @remove_role.error
    async def remove_role_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(title='Вы не можете использовать данную команду!',
                                description='Нужные права: `Администратор`')
            await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(RoleShopCog(bot))
