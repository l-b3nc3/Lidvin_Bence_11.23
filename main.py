from functions import* 

fajlBeolvasas()


valasztas=""
while valasztas!=0:
    valasztas=menu()
    if valasztas=="1":
        aruKiiras()
        input("")
    elif valasztas=="2":
        ujAru()
    elif valasztas=="3":
        aruTorlese()
    elif valasztas=="4":
        aruFelveteleKosarba()
    elif valasztas=="5":
        aruTorleseKosarbol()
    elif valasztas=="6":
        kosarKiir()
        input("Vissza...")