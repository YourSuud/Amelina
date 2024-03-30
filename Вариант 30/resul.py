import csv
#1
countUlt=int(0)
countNote=int(0)
countNet=int(0)
with open("devices.txt",encoding="UTF-8") as file:
    with open("count_company.txt", 'w', encoding="UTF-8") as filend:
         for i in file:
            ful=list(str(i).split("*"))
            vid=(list(str(i).split("*"))[2])
            print(ful)
            ram=ful[5]
            if vid=="Ultrabook":
                countUlt += 1,
                print(ram)
            if vid=="Noteboo k":
                countNote +=1
            if vid =="Netbook":
                 countNet += 1
         filend.write("Utrabook")
         filend.write(f"<Ram1> {countUlt}")
         filend.write("Notebook")
         filend.write(f"<Ram1> {countNote}")
         filend.write("Netbook")
         filend.write(f"<Ram1> {countNet}")




'''with open("count_company.txt",encoding="UTF-8") as new:
    new=csv.writer(a)
#count_company.txt'''
#or vid=="Notebook" or vid=="Netbook" :
'''def count_potions() -> None:
    """
    Функция для решения первой задачи. Выводит на экран количество Мощного зелья
    :return:
    """
    with open("tasks/magical.csv", 'r', encoding="utf-8") as file:
        alist = {}
        count = 0
        header = file.readline()
        for line in file:
            data = line.split(",")
            if data[1] == "-1":
                data[1] = "0"
            if data[0] == "Мощное Зелье":
                count += int(data[1])
            if not data[0] in alist.keys():
                alist[data[0]] = int(data[1])
            else:
                alist[data[0]] += int(data[1])

    with open("magicaPotions.txt", 'w', encoding="utf-8") as out:
        for key, value in alist.items():
            out.write(f"{key} в запасах еще есть - {value}\n")

    print(count)


if __name__ == '__main__':
    count_potions()'''