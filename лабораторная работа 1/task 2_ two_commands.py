list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# TODO Разделите участников на две команды
mid_player = int(len(list_players)/2)  # Делим, далее выводим
print(list_players[:mid_player])
print(list_players[mid_player:])