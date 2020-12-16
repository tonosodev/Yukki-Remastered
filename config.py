# ===================================================================#
#                          GENERAL SETTINGS                          #
# ===================================================================#

bot_settings = {
    "bot_token": "NzY2MjcwOTkwMDA3MDA5MzMw.X4g7eA.PLdlBX2vFVI-HMcD97bDofXRDWs",
    "bot_name": "Yukki",
    "bot_prefix": "Юкки, ",
    "log_channel": 766218369279852554,  # ID-канала для отправки лога
}

# ===================================================================#
#                          VERIFICATION                              #
# ===================================================================#

MAX_ROLES_PER_USER = 10
EXCROLES = {}

verification = {
    "verification_channel_id": 766217891971465216,  # ID-канала для обработки добавления реакции
    "verification_post_id": 768238823511293973  # ID-поста для обработки добавления реакции
}
verification_roles = {
    '<a:verify:768537178221051944>': 766232921685622795  # Verified
}

# ===================================================================#
#                             ECONOMY                                #
# ===================================================================#

SLOT_PRICE = 80

slot = {
    "slot_notification_channel": 769205419276369931,  # ID-канала для уведомлений
    "slot_minimum_win": 0000,  # Сумма минимального выигрыша
    "slot_maximum_win": 0000,  # Сумма максимального выигрыша
}

# ===================================================================#
#                             DATABASE                               #
# ===================================================================#

mongo_db = {
    "mongo_settings_cluster": "mongodb://NeverMind:Qwsxza2qwsxzA123132@nevermindcluster-shard-00-00.hfbwn.mongodb.net:27017,nevermindcluster-shard-00-01.hfbwn.mongodb.net:27017,nevermindcluster-shard-00-02.hfbwn.mongodb.net:27017/YukkiData?ssl=true&replicaSet=atlas-lsqum0-shard-0&authSource=admin&retryWrites=true&w=majority",
    "mongo_settings_db": "cluster.YukkiData",
    "mongo_settings_coll": "db.YukkiCollection"
}

# ===================================================================#
#                             INITIALIZE                             #
# ===================================================================#
bot_initialize = {
    "activity_status": "за порядком ☕",
    "token_error": "\n\n\tGeneral code error or TOKEN is invalid!\n\t\tCHECK TOKEN AND TRY AGAIN...\n\n",
    "logo_initialize_error": "Error reading from file",
    "activity_status_success": "\n##################################################\n[SUCCESS] Discord activity status is ready!",
    "activity_status_error": "\n##################################################\n[ERROR] Discord activity status doesnt ready!",
    "discord_py_version": "1.6.0a adapted\n##################################################\n",
    "mongo_success_notification": "\n##################################################\n          [SUCCESS] MONGODB CONNECTED!\n            WELCOME ABOARD, CAPTAIN!\n##################################################\n",
    "mongo_error_notification": "\n##################################################\n          [ERROR] MONGODB CONNECT ERROR!\n                    CHECK DATA!\n##################################################\n",
}

# ===================================================================#
#                             PERMISSIONS                            #
# ===================================================================#
ping_permission = 766293535832932392, 766233124681547776, 766231587104620554
virtual_ram_permission = [766231587104620554]
bot_status_permission = 766231587104620554
slot_command_permission = None

# ===================================================================#
#                              ALIASES                               #
# ===================================================================#
ping_aliases = ['пинг', 'ПИНГ', 'Пинг', 'задержка', 'Задержка', 'Задержки', 'задержки']
virtual_ram_aliases = ['озу', 'ОЗУ', 'RAM']
bot_status_aliases = ['бот', 'Бот', 'БОТ', 'Бот_статус', 'бот_статус', 'бот_инфо', 'Бот_инфо']
slot_command_aliases = ['слот', 'Слот', 'СЛОТ', 'казино', 'Казино', 'КАЗИНО', 'рулетка', 'Рулетка', 'РУЛЕТКА']
# ==========================
kick_command_aliases = ['кик', 'кикни', 'выгони', 'Кик', 'Кикни', 'Выгони', 'кикнуть', 'Кикнуть', 'выгнать', 'Выгнать']
mute_command_aliases = ['мут', 'Мут', 'замуть', 'Замуть', 'заглуши', 'Заглуши', 'затки', 'Заткни']
unmute_command_aliases = ['размут', 'Размут', 'размуть', 'Размуть', 'анмут', 'Анмут']
ban_command_aliases = ['бан', 'Бан', 'забань', 'Забань', 'заблокируй', 'Заблокируй']
unban_command_aliases = ['разбан', 'Разбан', 'разбань', 'Разбань', 'разблокируй', 'Разблокируй', 'пардон', 'Пардон']
add_role_command_aliases = ['добавить_роль', 'Добавить_роль', 'добавь_роль', 'Добавь_роль']
remove_role_command_aliases = ['удалить_роль', 'Удалить_роль', 'удали_роль', 'Удали роль', 'сними_роль', 'Сними роль',
                               'снять_роль', 'Снять_роль']
clear_command_aliases = ['очисти', 'Очисти', 'очисти_чат', 'Очисти_чат', 'очистить', 'Очистить', 'очистить_чат',
                         'Очистить_чат']
version_command_aliases = ['версия']
# ==========================
