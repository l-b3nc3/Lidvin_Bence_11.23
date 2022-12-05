from data import*
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
    print("4 - Áru felvétele kosárba")
    print("5 - Áru törlése a kosárból")
    print("6 - Kosár tartalma")
    print("0 - Kilépés")
    print("------------------------------------")
    return input("Kérem válasszon egy menüpontot==> ")

def aruKiiras():
    system("cls")
    print("-----------------Az összes áru--------------")
    for i in range(0, len(aruk)):
        print(f"\t{i+1}. {(aruk[i])}: {arak[i]} Ft ")

def ujAruFajlVegere(aru, ar):
    file=open("aruk.csv", "a", encoding="utf-8")
    file.write(f"\n{aru};{ar}")
    file.close()

def mentesFajlba():
    file=open("aruk.csv", "w", encoding="utf-8")
    for i in range(len(aruk)):
        file.write(f"{aruk[i]}; {arak[i]}")
        if i<len(aruk)-1:
            file.write("\n")
    file.close() 

def ujAru():
    system("cls")
    print("---------Kérem adja meg a felvenni kívánt áru nevét és árát-----------")
    ujAru=input("Áru neve==>")
    ujAr=int(input("Áru ára==>"))
    aruk.append(ujAru)
    arak.append(ujAr)
    ujAruFajlVegere(ujAru, ujAr)
    input("A felvétel megtörtént...")

def aruTorlese():
    system("cls")
    print("---------Áru törlése----------")
    aruKiiras()
    sorszam=1000
    while sorszam>len(aruk):
        sorszam=int(input("Kérem adja meg a törölni kívánt áru sorszámát==>"))
    aruk.pop(sorszam-1)
    arak.pop(sorszam-1)
    mentesFajlba()
    input("A törlés sikerült...")

def aruFelveteleKosarba():
    system("cls")
    print("-------------Vásárlás--------------")
    aruKiiras()
    print("-----------------------------------")
    sorszam=1000
    while sorszam>len(aruk):
        sorszam=int(input("Kérem adja meg a megvásárloni kívánt termék sorszámát==>"))
    db=int(input("Kérem adja meg a kívánt mennyiséget==>"))
    kosar_aruk.append(aruk[sorszam-1])
    kosar_arak.append(arak[sorszam-1])
    kosar_aru_db.append(db)
    input("A felvétel megtörtént...")

  

def kosarKiir():
    system("cls")
    print("------------A kosár trtalma-------------")
    for i in range(0, len(kosar_aruk)):
        print(f"\t{i+1}. {(kosar_aruk[i])} ---- {kosar_aru_db[i]} db ---- {kosar_arak[i]*kosar_aru_db[i]} Ft ")
    print("----------------------------------------")
    def osszegzes():
        osszeg=0
        for item in kosar_arak*kosar_aru_db[i]:
            osszeg+=item
        return osszeg
    print(f"Összesen: {osszegzes()} Ft")

def aruTorleseKosarbol():
    system("cls")
    kosarKiir()
    sorszam=1000
    while sorszam>len(aruk):    
        sorszam=int(input("Kérem adja meg a törölni kívánt árucikk sorszámát==>"))
    mennyiseg=int(input("Kérem adja meg a törölni kívánt mennyiséget==>"))
    if mennyiseg<kosar_aru_db[sorszam-1]:
        kosar_aru_db[sorszam-1]=kosar_aru_db[sorszam-1]-mennyiseg
       
    else: 
        kosar_aruk.pop(sorszam-1)
        kosar_arak.pop(sorszam-1)
    input("A törlés sikerült...")
    

