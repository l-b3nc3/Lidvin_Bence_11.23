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
    print("---------------Kisbolt-------------")
    print("1 - Összes áru")
    print("2 - Új áru felvététe")
    print("3 - Áru törlése")
    print("------------------------------------")
    print("0 - Kilépés")
    print("4 - Kosár")
    print("------------------------------------")
    return input("Kérem válasszon egy menüpontot==> ")
