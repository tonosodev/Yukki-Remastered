import asyncio
import random
import discord
from discord.ext import commands
from config import slot_command_aliases, slot


class SlotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=slot_command_aliases)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def slot(self, ctx):
        # await ctx.reply('{}, временно на технических работах.'.format(ctx.message.author.mention), delete_after=10)

        random_reward = random.randrange(slot['slot_minimum_win'], slot['slot_maximum_win'], 1)
        await ctx.message.delete()

        logs = self.bot.get_channel(slot['slot_notification_channel'])
        member = discord.Member

        parrot = ':gem:'  # Эмодзи совпадения слотпинов
        slotspin = ':purple_heart:'  # Эмодзи слотпинов (начальные)
        slots = ['<:s_leaf:769180703916687371>', '<:s_leaf:769180703916687371>', '<:s_leaf:769180703916687371>',
                 '<:s_flowers:769180731631992832>', '<:s_forest:769180705354678292>', '<:s_tomato:769185902986788874>',
                 '<:s_lime:769185042819317790>', '<:s_lime:769185042819317790>', '<:s_lime:769185042819317790>',
                 '<:s_lime:769185042819317790>', '<:s_lime:769185042819317790>', '<:s_lime:769185042819317790>']
        slot1 = slots[random.randint(0, 11)]
        slot2 = slots[random.randint(0, 11)]
        slot3 = slots[random.randint(0, 11)]
        slot4 = slots[random.randint(0, 11)]
        slot5 = slots[random.randint(0, 11)]

        slot6 = slots[random.randint(0, 11)]
        slot7 = slots[random.randint(0, 11)]
        slot8 = slots[random.randint(0, 11)]
        slot9 = slots[random.randint(0, 11)]
        slot10 = slots[random.randint(0, 11)]
        slot11 = slots[random.randint(0, 11)]
        slot12 = slots[random.randint(0, 11)]
        slot13 = slots[random.randint(0, 11)]
        slot14 = slots[random.randint(0, 11)]
        slot15 = slots[random.randint(0, 11)]
        slot16 = slots[random.randint(0, 11)]
        slot17 = slots[random.randint(0, 11)]
        slot18 = slots[random.randint(0, 11)]
        slot19 = slots[random.randint(0, 11)]
        slot20 = slots[random.randint(0, 11)]
        slot21 = slots[random.randint(0, 11)]
        slot22 = slots[random.randint(0, 11)]
        slot23 = slots[random.randint(0, 11)]
        slot24 = slots[random.randint(0, 11)]
        slot25 = slots[random.randint(0, 11)]

        slotOutput = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14,
            slot15,
            slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
        slotOutput1 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin,
            slotspin,
            slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin,
            slotspin,
            slotspin, slotspin, slotspin, )
        results0 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            parrot, parrot, parrot, parrot, parrot, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14,
            slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
        results1 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, slot5, parrot, parrot, parrot, parrot, parrot, slot11, slot12, slot13, slot14,
            slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
        results2 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, parrot, parrot, parrot, parrot,
            parrot,
            slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
        results3 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14,
            slot15,
            parrot, parrot, parrot, parrot, parrot, slot21, slot22, slot23, slot24, slot25)
        results4 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14,
            slot15,
            slot16, slot17, slot18, slot19, slot20, parrot, parrot, parrot, parrot, parrot)
        results5 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            parrot, slot2, slot3, slot4, slot5, parrot, slot7, slot8, slot9, slot10, parrot, slot12, slot13, slot14,
            slot15,
            parrot, slot17, slot18, slot19, slot20, parrot, slot22, slot23, slot24, slot25)
        results6 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, parrot, slot3, slot4, slot5, slot6, parrot, slot8, slot9, slot10, slot11, parrot, slot13, slot14,
            slot15,
            slot16, parrot, slot18, slot19, slot20, slot21, parrot, slot23, slot24, slot25)
        results7 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, parrot, slot4, slot5, slot6, slot7, parrot, slot9, slot10, slot11, slot12, parrot, slot14,
            slot15,
            slot16, slot17, parrot, slot19, slot20, slot21, slot22, parrot, slot24, slot25)
        results8 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, parrot, slot5, slot6, slot7, slot8, parrot, slot10, slot11, slot12, slot13, parrot,
            slot15,
            slot16, slot17, slot18, parrot, slot20, slot21, slot22, slot23, parrot, slot25)
        results9 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, parrot, slot6, slot7, slot8, slot9, parrot, slot11, slot12, slot13, slot14,
            parrot,
            slot16, slot17, slot18, slot19, parrot, slot21, slot22, slot23, slot24, parrot)
        results10 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            parrot, slot2, slot3, slot4, slot5, slot6, parrot, slot8, slot9, slot10, slot11, slot12, parrot, slot14,
            slot15,
            slot16, slot17, slot18, parrot, slot20, slot21, slot22, slot23, slot24, parrot)
        results11 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(
            slot1, slot2, slot3, slot4, parrot, slot6, slot7, slot8, parrot, slot10, slot11, slot12, parrot, slot14,
            slot15,
            slot16, parrot, slot18, slot19, slot20, parrot, slot22, slot23, slot24, slot25)

        msg = await ctx.send(
                "{}\n {}, рулетка запущенна!\nС Вашего счета списано 80 <:Yukki_Dollar:769711177826566144>".format(
                    slotOutput1, ctx.message.author.mention))

        await asyncio.sleep(2)
        await msg.edit(
            content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущена!\nС Вашего счета списано 80 <:Yukki_Dollar:769711177826566144>'.format(
                slot1, slotspin, slotspin, slotspin, slotspin, slot6, slotspin, slotspin, slotspin, slotspin, slot11,
                slotspin, slotspin, slotspin, slotspin, slot16, slotspin, slotspin, slotspin, slotspin, slot21,
                slotspin,
                slotspin, slotspin, slotspin, ctx.message.author.mention))
        await asyncio.sleep(2)
        await msg.edit(
            content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущена!\nС Вашего счета списано 80 <:Yukki_Dollar:769711177826566144>'.format(
                slot1, slot2, slotspin, slotspin, slotspin, slot6, slot7, slotspin, slotspin, slotspin, slot11, slot12,
                slotspin, slotspin, slotspin, slot16, slot17, slotspin, slotspin, slotspin, slot21, slot22, slotspin,
                slotspin, slotspin, ctx.message.author.mention))
        await asyncio.sleep(2)
        await msg.edit(
            content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна!\nС Вашего счета списано 80 <:Yukki_Dollar:769711177826566144>'.format(
                slot1, slot2, slot3, slotspin, slotspin, slot6, slot7, slot8, slotspin, slotspin, slot11, slot12,
                slot13,
                slotspin, slotspin, slot16, slot17, slot18, slotspin, slotspin, slot21, slot22, slot23, slotspin,
                slotspin,
                ctx.message.author.mention))
        await asyncio.sleep(2)
        await msg.edit(
            content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна!\nС Вашего счета списано 80 <:Yukki_Dollar:769711177826566144>'.format(
                slot1, slot2, slot3, slot4, slotspin, slot6, slot7, slot8, slot9, slotspin, slot11, slot12, slot13,
                slot14,
                slotspin, slot16, slot17, slot18, slot19, slotspin, slot21, slot22, slot23, slot24, slotspin,
                ctx.message.author.mention))
        await asyncio.sleep(2)
        await msg.edit(
            content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна!\nС Вашего счета списано 80 <:Yukki_Dollar:769711177826566144>'.format(
                slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14,
                slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25,
                ctx.message.author.mention))

        if slot1 == slot2 == slot3 == slot4 == slot5:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results0, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)


        elif slot6 == slot7 == slot8 == slot9 == slot10:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results1, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot11 == slot12 == slot13 == slot14 == slot15:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results2, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot16 == slot17 == slot18 == slot19 == slot20:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results3, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot21 == slot22 == slot23 == slot24 == slot25:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results4, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot1 == slot6 == slot11 == slot16 == slot21:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results5, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot2 == slot7 == slot12 == slot17 == slot22:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results6, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot3 == slot8 == slot13 == slot18 == slot23:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results7, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot4 == slot9 == slot14 == slot19 == slot24:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results8, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot5 == slot10 == slot15 == slot20 == slot25:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results9, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot1 == slot7 == slot13 == slot19 == slot25:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results10, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem:️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        elif slot5 == slot9 == slot13 == slot17 == slot21:
            await msg.edit(
                content="{}\n {}, Вы выиграли!\nУвидеть свой выигрыш Вы можете в канале <#769205419276369931>".format(
                    results11, ctx.author.mention), delete_after=10)
            emb = discord.Embed(title='Казино :gem: ️',
                                color=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255),
                                                             random.randint(1, 255)))
            emb.add_field(name='Пользователь **{}**'.format(ctx.message.author.name),
                          value=' выиграл в казино **{}** <:Yukki_Dollar:769711177826566144>'.format(random_reward))
            emb.set_footer(text=f'{self.bot.user.name} © 2020 | Все права защищены', icon_url=self.bot.user.avatar_url)
            await logs.send(embed=emb)

        else:
            await msg.edit(
                content="{}\n {}, Вы проиграли и потеряли стартовый капитал в 80 <:Yukki_Dollar:769711177826566144>".format(
                    slotOutput, ctx.message.author.mention),
                delete_after=10)


def setup(bot):
    bot.add_cog(SlotCog(bot))
