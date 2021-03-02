import discord

import asyncio
import random
from discord.ext import commands
from pymongo import MongoClient
from config import mongo_db, bot_initialize, activity_status_watch, activity_status_competes, \
    activity_status_game, activity_status_listen


class ConnectCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            logo = open("logo.yml", "r", encoding="utf8")
            data = logo.read()
            print(data)
        except IOError:
            print(bot_initialize['logo_initialize_error'] + " " + logo.name)
        finally:
            logo.close()

        # ----------------------------- #
        #        YUKKI DATABASE         #
        # ----------------------------- #

        try:
            cluster = MongoClient(mongo_db['mongo_settings_cluster'])
            db = mongo_db['mongo_settings_db']
            coll = mongo_db['mongo_settings_coll']
            print("\n##################################################\n" + bot_initialize[
                'mongo_success_notification'] + "\n##################################################\n")
        except:
            print("\n##################################################\n" + bot_initialize[
                'mongo_error_notification'] + "\n##################################################\n")
        finally:
            pass

        # ----------------------------- #
        #        YUKKI ACTIVITY         #
        # ----------------------------- #

        # await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('клубок ниток 🧶', type=3))

        # status_msg = bot_initialize['activity_status']

        try:
            print("\n##################################################\n" + bot_initialize['activity_status_success'])
            print('[SUCCESS] Discord.py version ' + (
                str(discord.__version__)) + " | " + bot_initialize[
                      'discord_py_version'] + "\n##################################################\n")
            while True:
                await self.bot.change_presence(status=discord.Status.online,
                                               activity=discord.Game(random.choice(activity_status_game), type=3))
                await asyncio.sleep(30)  # Thread time
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=discord.Activity(name=random.choice(activity_status_competes),
                                                                         type=5))
                await asyncio.sleep(30)
                await self.bot.change_presence(status=discord.Status.dnd,
                                               activity=discord.Activity(type=discord.ActivityType.watching,
                                                                         name=random.choice(activity_status_watch)))
                await asyncio.sleep(30)
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=discord.Activity(type=discord.ActivityType.listening,
                                                                         name=random.choice(activity_status_listen)))
                await asyncio.sleep(30)
        except:
            print("\n##################################################\n" + bot_initialize[
                'activity_status_error'] + "\n##################################################\n")
        finally:
            pass


def setup(bot):
    bot.add_cog(ConnectCog(bot))
