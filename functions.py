from data import aruk, arak


def fajlBeolvasas():
    file=open("aruk.csv", "r", encoding="utf8" )
    for i in file:
        darabolt=i.strip().split(";")  
        aruk.append(darabolt[0])
        arak.append(int(darabolt[1]))
    file.close()


