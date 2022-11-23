from data import aruk, arak
from os import system


def fajlBeolvasas():
    file=open("aruk.csv", "r", encoding="utf8" )
    for i in file:
        darabolt=i.strip().split(";")  
        aruk.append(darabolt[0])
        arak.append(int(darabolt[1]))
    file.close()

def menu():
    system("cls")
    print("---------------Menü-------------")
    print("0 - Kilépés")
    print("1 - Összes áru")
    print("2 - Kosár")
    print("3 - Új áru felvététe")
    print("4 - Áru törlése")
    print("--------------------------------")
    return input("Kérem válasszon egy menüpontot==> ")
