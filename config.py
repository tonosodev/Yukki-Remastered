# ===================================================================#
#                          GENERAL SETTINGS                          #
# ===================================================================#
bot_settings = {
    "bot_token": "NzY2MjcwOTkwMDA3MDA5MzMw.X4g7eA.VGtQzkr36_i535EDvcOUlJZNNg0",
    "bot_name": "Yukki",
    "bot_prefix": "Юкки, ",
    "log_channel": 766218369279852554,  # ID-канала для отправки лога оповещений бота
    "system_log_channel": 789246267645362196,  # ID-канала для отправки лога ошибок
    "report_channel": 766218032363077632,  # ID-канала для отправки внутрисерверных репортов
    "need_accept_report_roles": [766293535832932392, 766233124681547776, 766231587104620554]
}
# ===================================================================#
#                          VERIFICATION                              #
# ===================================================================#
verification = {
    "verification_channel_id": 766217891971465216,  # ID-канала для обработки добавления реакции
    "verification_post_id": 789959038770872341,  # ID-поста для обработки добавления реакции
    "verification_log_id": 767819023178006569
}
verification_roles = {
    '<a:verify:768537178221051944>': 766232921685622795  # Verified
}
# ===================================================================#
#                             REPORTS                                #
# ===================================================================#
reports = {
    "report_channel_id": 766218032363077632
}
# ===================================================================#
#                               ROLES                                #
# ===================================================================#
server_roles = {
    "everyone_role": 766213910595633153,
    "not_verified_role": 768118967759405056,
    "verified_role": 766232921685622795,
    "member_role": 766232996285775903,
    "muted_role": 766366691466149898,
    "tech.support_role": 766293535832932392,
    "support_role": 766233124681547776,
    "owner_role": 766231587104620554
}
# ===================================================================#
#                             ECONOMY                                #
# ===================================================================#

SLOT_PRICE = 80

slot = {
    "slot_notification_channel": 769205419276369931,  # ID-канала для уведомлений
    "slot_minimum_win": 100,  # Сумма минимального выигрыша
    "slot_maximum_win": 700,  # Сумма максимального выигрыша
}
# ===================================================================#
#                             ECONOMY                                #
# ===================================================================#
private_room_category = 769490405711413248
# Категория для добавления приватных каналов пользователей

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
activity_status_watch = ["за порядком ☕", "ламповый телевизор"]
activity_status_game = ["клубок ниток 🧶", "Бесконечное Лето", "плюшевого мишку"]
activity_status_listen = ["Gorillaz", "Blue Foundation", "Bring Me The Horizon", "Owl City", "Виктора Цоя", "ЧайФ",
                          "Чиж & Co", "To The Sky  | ost: Legend of the Guardians"]
activity_status_competes = ["шахматы", "Cuphead", "чаепитие"]

bot_initialize = {
    "cog_load_error": "LOADING ERROR!\nCHECK TROUBLES AND CORRECT CODE!",
    "token_error": "\n\n\tConnection error or TOKEN is invalid!\n\t\tCHECK TOKEN AND TRY AGAIN...\n\n",
    "logo_initialize_error": "Error reading from file",
    "activity_status_success": "[SUCCESS] Discord activity status is ready!",
    "activity_status_error": "[ERROR] Discord activity status doesnt ready!",
    "discord_py_version": "1.6.0a adapted",
    "mongo_success_notification": "          [SUCCESS] MONGODB CONNECTED!\n            WELCOME ABOARD, CAPTAIN!",
    "mongo_error_notification": "          [ERROR] MONGODB CONNECT ERROR!\n                    CHECK DATA!",

    "new_user_authorize": "",

    "copyright_message": "\n\t  Yukki© 2021 | All rights reserved",
    "embeds_footer_message": "© 2021 | Все права защищены"
}
# ===================================================================#
#                             PERMISSIONS                            #
# ===================================================================#
owner = 766231587104620554
support = 766233124681547776
head_tech_spec = 766293535832932392
sponsor = 791227395331457047
member = 766232996285775903
debug_server_owner = 816635673175130122
commands_permission = {
    "recovery_command_permission": [owner, head_tech_spec],
    # ==========================
    "server_status_permission": [debug_server_owner, owner, support, head_tech_spec, sponsor],
    "say_permission": [owner, support, head_tech_spec],
    "slowmode_command_permission": [owner, support, head_tech_spec],
    # ==========================
    "kick_command_permission": [owner, support],
    "clear_command_permission": [owner, support, head_tech_spec, sponsor],
    "add_role_command_permission": [owner, support],
    "remove_role_command_permission": [owner, support],
    "ban_command_permission": [owner, support],
    "unban_command_permission": [owner, support],
    "mute_command_permission": [owner, support],
    "unmute_command_permission": [owner, support],
    "version_command_permission": [owner, support, head_tech_spec, sponsor, member],
    # ==========================
    "slot_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "link_cutter_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "magicball_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "wiki_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "covid_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "avatar_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "translate_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "user_report_command_permission": [owner, support, head_tech_spec, sponsor, member],
    "hug_command_permission": [owner, support, head_tech_spec, sponsor, member],
    # ===========================
    "help_command_permission": [owner, support, head_tech_spec, sponsor, member]
}
user_report_reaction_permission_owner = owner
user_report_reaction_permission_support = support
recovery_reaction_permission_owner = owner
recovery_reaction_permission_head_tech = head_tech_spec
# ===================================================================#
#                              ALIASES                               #
# ===================================================================#
link_cutter_command_aliases = ['сократить', 'сократить_ссылку', 'cut', 'сократи', 'сократи_ссылку']
magicball_command_aliases = ['шар', 'Шар', 'магический_шар', 'magicball']
ping_aliases = ['пинг', 'ПИНГ', 'Пинг', 'задержка', 'Задержка', 'Задержки', 'задержки']
say_command_aliases = ['скажи', 'напиши', 'отправь', 'Скажи', 'Напиши', 'Отправь']
slot_command_aliases = ['слот', 'Слот', 'СЛОТ', 'казино', 'Казино', 'КАЗИНО', 'рулетка', 'Рулетка', 'РУЛЕТКА']
slowmode_command_aliases = ['слоумод', 'Слоумод', 'медленный_режим', 'Медленный_режим']
virtual_ram_aliases = ['озу', 'ОЗУ', 'RAM']
wiki_command_aliases = ['вики', 'википедия', 'Вики', 'Википедия', 'педия', 'Педия']
covid_command_aliases = ['ковид', 'Ковид', 'коронавирус', 'Коронавирус', 'covid', 'Covid']
avatar_command_aliases = ['ава', 'Ава', 'аватар', 'Аватар']
translate_command_aliases = ['переведи', 'перевод', 'Переведи', 'Перевод']
user_report_command_aliases = ['репорт', 'жалоба', 'зарепорть', 'пожаловаться', 'Репорт', 'Жалоба', 'Зарепортить',
                               'Пожаловаться']
hug_command_aliases = ['обними', 'Обними', 'обнимашки', 'Обнимашки', 'обнимаю', 'Обнимаю', 'обниму', 'Обниму']
member_activity = ['активити', 'Активити', 'активность', 'Активность', 'статистика', 'Статистика']
# ==========================
server_status_aliases = ['инфо', 'Инфо', 'серверинфо', 'Серверинфо']
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
help_command_aliases = ['помощь', 'помоги', 'команды', 'Помощь', 'Помоги', 'Команды', 'хелп', 'Хелп']

# ==========================
