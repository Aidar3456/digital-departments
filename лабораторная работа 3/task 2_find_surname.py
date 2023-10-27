from typing import List

def find_common_participants(group1, group2, key=','):
    name_list = list()
    group11 = group1.split(key)
    group22 = group2.split(key)
    for i in range(0, len(group11)):
        for j in range(0, len(group22)):
            if group11[i] == group22[j]:
                name_list.append(group11[i])
    name_list.sort()
    return name_list

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))