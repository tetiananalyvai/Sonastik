
from os import remove, path, system
from gtts import *
from random import *

def loe_failist(fail:str)->list:
    """Loetakse informatsioon failist ja tagastatakse info nagu järjend
    :param str fail: faili nimetus
    .rtype: list
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def tolkimine(sona:str,sonad:list,tolked:list)->str:
    if sona in sonad:
        indeks=sonad.index(sona)
        return tolked[indeks]
    elif sona in tolked:
        indeks=tolked.index(sona)
        return sonad[indeks]
    else:
        return "Sõna "+sona+" puudub"
def teadmiste_kontroll(sonad_est: list, sonad_rus: list):
    print("Tere tulemast teadmiste kontrolli režiimi!")
    print("Teil palutakse tõlkida mõned sõnad eesti keelest vene keelde.")
    print("Sisestage sõna tõlge. Testi lõpetamiseks vajutage sisestusklahvi ilma tippimata.")
    punktid=0
    koguarv=len(sonad_est)
    for sona_est, sona_rus in zip(sonad_est, sonad_rus):
        vastus=input(f"Kuidas seda sõna tõlgitakse '{sona_est}'? (vajutage väljumiseks Enter): ")
        if not vastus:  # tühja vastuse sisestamisel väljuge tsüklist
            break
        if vastus.strip().lower()==sona_rus.lower():
            print("Õige!")
            punktid+=1
        else:
            print(f"Vale. Õige tõlge: {sona_rus}")
    protsent = (punktid / koguarv) * 100 if koguarv > 0 else 0
    print(f"Kontroll lõpetatud. Olete sisestanud {punktid} võimalikust {koguarv}-st. Õigete vastuste protsent: {protsent:.2f}%")    
def teksti_lisamine_failisse(fail:str,sona:str,sonad:list):
    sonad.append(sona)
    f=open(fail,'a',encoding="utf-8")
    f.write(sona+'\n')
    f.close()
    return sonad
def faili_kustutamine():
    faili_nimi=input("Mis fail on vaja kustutada ära?")
    if path.isfile(faili_nimi): 
       remove(faili_nimi) #path.isdir(kaust)
       print(f"Fail {faili_nimi} oli kustutatud")
    else:
       print(f"Fail {faili_nimi} puudub")
def räägimine(est:list,rus:list):
    sona=input("Sisesta sõna:")
    if sona in rus:
        keel="ru"
    elif sona in est:
        keel="et"
    if keel in ["ru","et"]: 
        obj=gTTS(text=sona,lang=keel,slow=False).save("heli.mp3")
        system("heli.mp3")
    else:
        print("Viga!")
