
from os import remove, path,system
from Moodul import *


rus=[] #vene kelsed
est=[] #eestikeelsed sonad
rus=loe_failist("Rus.txt")
est=loe_failist("Est.txt")
while True:
    print(rus)
    print(est)
    v=input("1-Tõlkimine\n2-Sõnade Lisamine\n3-Kontroll\n4-Räägimine\n5-lõpp\n")
    if v=="1":
        print("Tolkimine")
        sona=input("Sisasta sõna tõlkimiseks:")
        tolke=tolkimine(sona,rus,est)
        print(tolke)
    elif v=="2":
        print("Sõnade Lisamine")
        est_sona=input("Sisesta sõna eesti keeles:")
        rus_sona=input("Sisesta sõna vene keeles:")
        est=teksti_lisamine_failisse("Est.txt",est_sona,est)
        rus=teksti_lisamine_failisse("Rus.txt",rus_sona,rus)      
    elif v=="3":
        print("Teadmiste Kontroll")
    elif v=="4":       
        räägimine(est,rus)
    elif v=="5":
        print("Kõige head!")
        break