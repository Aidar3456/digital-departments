import json

# TODO решите задачу
INPUT_FILE = "input.json"


def task() -> float:
    S = 0
    with open(INPUT_FILE, 'r') as i_file:
        data = json.load(i_file)
        for i in range(len(data)):
            list_ = data[i]
            S += round(list_['score']*list_['weight'], 3)
    return S

print(task())
