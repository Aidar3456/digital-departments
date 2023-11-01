from typing import List


def find_common_participants(group1, group2, key=','):
    group1 = group1.split(key)
    group2 = group2.split(key)
    set_group = set(group1)
    name_set = set_group.intersection(group2)
    name_list = list(name_set)
    name_list.sort()
    return name_list


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))
