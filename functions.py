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
    print("4 - Kosár tartalma")
    print("5 - Áru felvétele kosárba")
    print("0 - Kilépés")
    print("------------------------------------")
    return input("Kérem válasszon egy menüpontot==> ")

def aruKiiras():
    system("cls")
    print("-----------------Az összes áru--------------")
    for i in range(0, len(aruk)):
        print(f"\t{i+1}. {(aruk[i])}: {arak[i]} Ft ")
    input("")
        
