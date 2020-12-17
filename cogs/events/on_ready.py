import discord
from discord.ext import commands
from pymongo import MongoClient
from config import mongo_db, bot_initialize


class ConnectCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            logo = open("logo.txt", "r", encoding="utf8")
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
            print("\n##################################################\n" + bot_initialize['mongo_success_notification'] + "\n##################################################\n")
        except:
            print("\n##################################################\n" + bot_initialize['mongo_error_notification'] + "\n##################################################\n")
        finally:
            pass

        # ----------------------------- #
        #        YUKKI ACTIVITY         #
        # ----------------------------- #

        # await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('клубок ниток 🧶', type=3))
        status_msg = bot_initialize['activity_status']
        try:
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=str(status_msg)))
            print("\n##################################################\n" + bot_initialize['activity_status_success'])
        except:
            print("\n##################################################\n" + bot_initialize['activity_status_error'])
        finally:
            pass
        print('[SUCCESS] Discord.py version ' + (
            str(discord.__version__)) + " | " + bot_initialize['discord_py_version'] + "\n##################################################\n")


def setup(bot):
    bot.add_cog(ConnectCog(bot))
