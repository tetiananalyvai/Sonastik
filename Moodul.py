
from os import remove, path, system
from gtts import *

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
