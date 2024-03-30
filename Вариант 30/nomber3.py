def get_information() -> None:
    """
    Функция для вывода информации по самому дорогому устройству,
    компанию которого запрашивает пользователь
    если ничего не найдено будет выводить: “У нас нет данного устройства.
    Результат будет выводиться в консоль
    """
    zapros=input()
    with open("devices.txt", encoding="UTF-8") as file:
        with open("dees.txt", 'w', encoding="UTF-8") as end:
            a=file.sort()
            end.write(a)
        print(f"По вашему запросу: {zapros} найдены следующие варианты: { a[0][0] } { a[0][1] } - тип устройства: { a[0][2] } ; Разрешение экрана - { a[0][3] } ;Цена - { a[0][8] }")


if __name__ == '__main__':
    get_information()