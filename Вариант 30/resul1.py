import csv
def count_potions() -> None:
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





if __name__ == '__main__':
    count_potions()
