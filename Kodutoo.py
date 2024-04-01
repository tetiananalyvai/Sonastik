import Mymodul

# Alusta tühjade järjenditega
Mymodul.users=[[], []]

while True:
    print("\nValikud:")
    print("1. Registreeri")
    print("2. Logi sisse")
    print("3. Muuda parooli")
    print("4. Unustasin parooli")
    print("5. Lõpeta")

    choice=input("Vali tegevus: ")

    if choice=="1":  # Registreeri
        kasutajanimi=input("Sisesta kasutajanimi: ")
        parool_choice=input("Kas soovid ise luua parooli (i) või lasta seda luua automaatselt (a)? ")

        if parool_choice.lower()=="i":
            parool=input("Sisesta parool: ")
        elif parool_choice.lower()=="a":
            parool=Mymodul.generate_parool()
            print("Genereeritud parool: ", parool)
        else:
            print("Vale valik.")
            continue

        tulemus=Mymodul.register(kasutajanimi, parool)
        print(tulemus)

    elif choice == "2":  # Logi sisse
        kasutajanimi=input("Sisesta kasutajanimi: ")
        parool=input("Sisesta parool: ")

        tulemus=Mymodul.login(kasutajanimi, parool)
        print(tulemus)

    elif choice=="3":  # Muuda parooli
        kasutajanimi=input("Sisesta kasutajanimi: ")
        vana_parool=input("Sisesta vana parool: ")
        uus_parool=input("Sisesta uus parool: ")

        tulemus=Mymodul.change_parool(kasutajanimi, vana_parool, uus_parool)
        print(tulemus)

    elif choice=="4":  # Unustasin parooli
        kasutajanimi=input("Sisesta kasutajanimi: ")

        tulemus=Mymodul.forgot_parool(kasutajanimi)
        print(tulemus)

    elif choice=="5":  # Lõpeta
        print("Programm lõpetab.")
        break

    else:
        print("Vale valik, palun vali uuesti.")


import tkinter as tk
from tkinter import messagebox

def lahenda_ruut(a, b, c):
    discriminant=b**2-4*a*c
    if discriminant<0:
        return None
    elif discriminant==0:
        x=-b/(2*a)
        return x
    else:
        x1=(-b+discriminant**0.5)/(2*a)
        x2=(-b-discriminant**0.5)/(2*a)
        return x1, x2

def lahendada_ja_näidata():
    try:
        a=float(entry_a.get())
        b=float(entry_b.get())
        c=float(entry_c.get())
        tulemus=lahenda_ruut(a, b, c)
        if tulemus is None:
            messagebox.showinfo("Lahendus", "Võrrandil pole tegelikke juuri.")
        else:
            if isinstance(tulemus, tuple):
                messagebox.showinfo("Lahendus", f"Võrrandi juured: {tulemus[0]}, {tulemus[1]}")
            else:
                messagebox.showinfo("Lahendus", f"Võrrandi juured: {tulemus}")
    except ValueError:
        messagebox.showerror("Viga", "Palun sisestage arvväärtused.")


juur=tk.Tk()
juur.title("Ruutvõrrandi lahendamine")


label_a=tk.Label(juur, text="Sisestage koefitsiendid a:")
label_a.grid(row=0, column=0, padx=5, pady=5)

entry_a=tk.Entry(juur)
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b=tk.Label(juur, text="Sisestage koefitsiendid b:")
label_b.grid(row=1, column=0, padx=5, pady=5)

entry_b=tk.Entry(juur)
entry_b.grid(row=1, column=1, padx=5, pady=5)

label_c=tk.Label(juur, text="Sisestage koefitsiendid c:")
label_c.grid(row=2, column=0, padx=5, pady=5)

entry_c=tk.Entry(juur)
entry_c.grid(row=2, column=1, padx=5, pady=5)

solve_button=tk.Button(juur, text="Otsustama", command=lahendada_ja_näidata)
solve_button.grid(row=3, columnspan=2, padx=5, pady=5)

juur.mainloop()

