"""
Today is 3/17/2021
Session by: https://github.com/DevilDesigner
Create Time: 9:00 PM
This Class: DB
"""

import sqlite3
import time


class Get:
    def __init__(self):
        pass

    def mute(self, member):
        conn = sqlite3.connect("./cogs/administration_commands/data/members_mutes.db")
        cursor = conn.cursor()

        if member:
            cursor.execute(f"SELECT * FROM mutes WHERE member={member.id}")
            result = cursor.fetchone()
        else:
            cursor.execute(f"SELECT * FROM mutes WHERE time < {float(time.time())}")
            result = cursor.fetchall()

        return result


class Set:
    def __init__(self):
        pass

    def mute(self, member, time):
        conn = sqlite3.connect("./cogs/administration_commands/data/members_mutes.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM mutes")
        if not cursor.fetchone():
            cursor.execute(f"INSERT INTO mutes VALUES ({member.id}, 0)")
        else:
            cursor.execute(f"UPDATE mutes SET time = {float(time)} WHERE member='{member.id}'")

        conn.commit()
        conn.close()
