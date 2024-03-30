def count_classes() -> None:
    """
    Функция для подсчета количества зелий классов.
    Результат выполнения функции выводится в консоль
    """
    companies = {}
    with open("tasks/ttt.txt", 'r', encoding="utf-8") as file:
        lines = []
        header = file.readline()
        for line in file:
            data = line.replace("\n", '').split("*")
            lines.append(data)
            name = data[0]
            tip = name
            if tip in companies.keys():
                companies[tip].append(float(data[-1].replace(",", ".")))
            else:
                companies[tip] = []
                companies[tip].append(float(data[-1].replace(",", ".")))
        for key, value in companies.items():
            print(f"Если продать все ноутбуки {key} можно заработать {sum(value)}")


if __name__ == '__main__':
    count_classes()