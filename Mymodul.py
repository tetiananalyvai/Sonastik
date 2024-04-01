
from math import *
from datetime import *
def date(paev:int,kuu:int,aasta:int)->bool:
    """
    """
    try:
        d=datetime.datemine(aasta,kuu,paev)
       
        tulemus=True
    except:
        tulemus=False
    return tulemus
       


def is_prime(number:int)->bool:
    """
    :parem int
    """
    p=True
    if number>=0 and number<1001:
        for i in range(2,number):
            if number % i == 0:
                p=False
    return p


def bank(a:float,year:int)->float:
    """
    """
    for i in range(year):
        a=a*1.1
    return a
   



def season(number:int)->str:
    """
    :parem str nrkuu:
    :rtype: str
    """
    if number>0 and number<13:
        if number in [1,2,12]:
            s="talv"
        elif number in [3,4,5]:
            s="kevad"
        elif number in [6,7,8]:
            s="suvi"
        else:
            s="sügis"
    else:
        s="vale number"
    return s
           







def square (külg:float)->any:
    """Leiab: pindala-S,ümbermõõt-P,diagonaal-D

    :param float külg:
    :rtype: any
    """
    S=külg**2
    P=4*külg
    D=sqrt(2*külg**2)
    return S,P,D






def is_year_leap(aasta:int)->bool:
    """Tagastad True kui aasta on liigaasta ja False, kui on tavaline aasta
    :param int aasta: Kasutaja sisestab aasta jarjekorranumber
    :rtype: bool
    """
    if aasta%4==0:
        tüüp=True
    else:
        tüüp=False
    return tüüp
       




def arithmetic(a:int,t:str,b:int)->any:
    """Funktsioon tagastab kas +,-,*,/ tehede tulemust.
        + -liitmine,
        - -lahutamine,
        * -korrutamine
        / -jagamine
    :param int a: Esimene arv
    :param int b: Teine arv
    :param str t: Tehe
    :rtype: any
    """
    if t in ["+","-","*","/"]:
        if t=="+":
            v=a+b
        elif t=="-":
            v=a-b
        elif t=="*":
            v=a*b
        else:
            if b==0:
                v="DIV/0"
            else:
                v=a/b
    else:
        v="Tundmatu tehe"
    return v
               




def Summa(arv1:float,arv2:float,arv3=5.0)->float:
    """Funktsioon tagastab kolme arvude summa float fomaadis. Kolmas arv vaaikimisi võrdub 5.0.
    :param float arv1: Esimene arv, mis sisestab kasutaja
    :param float arv2: Teine arv, mis sisestab kasutaja
    :param float arv3: Kolmas arv, mis sisestab kasutaja või väikimisi =5.0
    :rtype: float
    """
    s=arv1+arv2+arv3
    return s


#"Registreerimine ja autoriseerimine"
import random
import string

# Järjendid kasutajate andmete hoidmiseks
users=[]  # Indeks 0 - kasutajanimed, Indeks 1 - paroolid

def register(kasutajanimi, parool):
    # Kontrolli, kas kasutajanimi on juba kasutusel
    if kasutajanimi in users[0]:
        return "Kasutajanimi on juba võetud, palun vali teine."

    # Lisa uus kasutaja
    users[0].append(kasutajanimi)
    users[1].append(parool)
    return "Registreerimine õnnestus."

def login(kasutajanimi, parool):
    # Kontrolli, kas kasutaja on registreeritud
    if kasutajanimi in users[0]:
        index=users[0].index(kasutajanimi)
        if users[1][index]==parool:
            return "Sisselogimine õnnestus."
        else:
            return "Vale parool."
    else:
        return "Kasutajat ei leitud."

def change_parool(kasutajanimi, vana_parool, uus_parool):
    # Kontrolli, kas kasutaja on registreeritud
    if kasutajanimi in users[0]:
        index=users[0].index(kasutajanimi)
        if users[1][index]==vana_parool:
            users[1][index]=uus_parool
            return "Parooli muutmine õnnestus."
        else:
            return "Vale parool."
    else:
        return "Kasutajat ei leitud."

def forgot_parool(kasutajanimi):
    # Kontrolli, kas kasutaja on registreeritud
    if kasutajanimi in users[0]:
        index=users[0].index(kasutajanimi)
        return f"Teie parool on: {users[1][index]}"
    else:
        return "Kasutajat ei leitud."

def generate_parool(pikkus=12):
    parool_characters=string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(parool_characters) for i in range(pikkus))


# "Sõnastik"

def loe_failist(f):
    with open(f,"r",encoding="utf-8") as fail:
        mas=[rida.strip() for rida in fail]
    return mas

def kirjuta_faili(sõnad, failinimi):
    with open(failinimi,'w',encoding="utf-8") as fail:
        for sõna in sõnad:
            fail.write(sõna+'\n')

# Пример заполнения списков слов
vene_sõnad=["привет", "друг", "яблоко","дорога",""]
est_sõnad=["tere", "sõber", "õun","tee"]

kirjuta_faili(vene_sõnad, "vene.txt")
kirjuta_faili(est_sõnad, "est.txt")
