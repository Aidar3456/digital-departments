import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    list_ = []
    with open(INPUT_FILENAME, 'r') as i_file:
        reader = csv.DictReader(i_file)
        for row in reader:
            list_.append(row)
    with open(OUTPUT_FILENAME, 'w') as o_file:
        json.dump(list_, o_file, indent=4)




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
