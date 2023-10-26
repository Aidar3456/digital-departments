users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
visits_number = {"Общее количество": 0,"Уникальные посещения": 0}
visits_number["Уникальные посещения"] = len(set(users))
visits_number["Общее количество"] = len(users)
print(visits_number)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
