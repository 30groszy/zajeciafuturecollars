#!/usr/bin/env python3

import sys

saldo = 0
magazyn = {}

historia = []

while True:
    komenda = []
    akcja = input()
    if akcja == "stop":
        break
    if akcja == "saldo":
        komenda.append('saldo')
        komenda.append(int(input()))
        komenda.append(input())
        (_akcja, wartosc, komentarz) = komenda
        saldo += int(wartosc)
        historia.append(komenda)
    elif akcja == "zakup":
        komenda.append('zakup')
        komenda.append(input())
        komenda.append(int(input()))
        komenda.append(int(input()))
        (_akcja, nazwa_produktu, cena, ilosc) = komenda
        stan_konta_po_akcji = saldo - int(cena) * int(ilosc)
        if stan_konta_po_akcji >= 0:
            saldo = stan_konta_po_akcji
            if not nazwa_produktu in magazyn:
                magazyn[nazwa_produktu] = int(ilosc)
            else:
                magazyn[nazwa_produktu] += int(ilosc)
        else:
            print("brak kasy")
        historia.append(komenda)
    elif akcja == "sprzedaz":
        komenda.append('sprzedaz')
        komenda.append(input())
        komenda.append(int(input()))
        komenda.append(int(input()))
        historia.append(komenda)
        if komenda[1] in magazyn.keys() and magazyn.get(komenda[1]) >= int(komenda[3]):
            magazyn[komenda[1]] -= int(komenda[3])
            saldo += int(komenda[2]) * int(komenda[3])
        else:
            print("Niewystarczajaca ilosc danego produktu na magazynie!")
    elif akcja == "konto":
        # print(saldo)
        break
    elif akcja == "magazyn":
        komenda = [akcja]
        produkt = input()
        while produkt != "stop":
            komenda.append(produkt)
            produkt = input()
        for produkt in komenda[1:]:
            ilosc = 0
            if produkt in magazyn.keys():
                ilosc = magazyn[produkt]
            print(f"{produkt}: {ilosc}")
        historia.append(komenda)
        break
    elif akcja == "przeglad":
        print("Podaj poczatek zakresu historii transakcji: ")
        start = int(input())
        print("Podaj koniec zakresu historii transakcji: ")
        stop = int(input())
        for komenda in historia[start: stop + 1]:
            for element in komenda:
                pass
    else:
        print("Bledna nazwa komendy! Sprobuj jeszcze raz.\nWpisz jedna z "
              "komend: saldo konto zakup sprzedaz przeglad magazyn")

        pass

komenda_z_argumentow = sys.argv[1:]
akcja = komenda_z_argumentow[0]

if akcja == "zakup":
    nazwa_produktu = komenda_z_argumentow[1]
    cena = komenda_z_argumentow[2]
    ilosc = komenda_z_argumentow[3]
    stan_konta_po_akcji = saldo - int(cena) * int(ilosc)
    historia.append(["zakup",nazwa_produktu, cena, ilosc])
    if stan_konta_po_akcji >= 0:
        saldo = stan_konta_po_akcji
        if not nazwa_produktu in magazyn.keys():
            magazyn[nazwa_produktu] = int(ilosc)
        else:
            magazyn[nazwa_produktu] += int(ilosc)
    else:
        print("brak kasy")
elif akcja == "sprzedaz":
    nazwa_produktu = komenda_z_argumentow[1]
    cena = komenda_z_argumentow[2]
    ilosc = komenda_z_argumentow[3]
    if not nazwa_produktu in magazyn.keys() or int(magazyn[nazwa_produktu]) <= 0:
        print("Brak w magazynie")
    else:
        magazyn[nazwa_produktu] = int(magazyn[nazwa_produktu]) - int(ilosc)
        saldo += int(cena) * int(ilosc)
        historia.append(["sprzedaz",nazwa_produktu, cena, ilosc])

    if stan_konta_po_akcji >= 0:
        saldo = stan_konta_po_akcji
        if not nazwa_produktu in magazyn:
            magazyn[nazwa_produktu] = int(ilosc)
        else:
            magazyn[nazwa_produktu] += int(ilosc)
    else:
        print("brak kasy")
elif akcja == "magazyn":
    produkty = komenda_z_argumentow[1:]
    for produkt in produkty:
        ilosc = 0
        if produkt in magazyn.keys():
            ilosc = magazyn[produkt]
        print(f"{produkt}: {ilosc}")
elif akcja == "przeglad":
    start = int(komenda_z_argumentow[1])
    stop = int(komenda_z_argumentow[2]) + 1
    if start > stop:
        print("Liczby powinne być uporzadkowane rosnaco")
    print(historia[start:stop])
elif akcja == "konto":
    print(saldo)

elif akcja =="saldo":
    kwota = komenda_z_argumentow[1]
    komentarz = komenda_z_argumentow[2]
    saldo += int(kwota)
    historia.append(["saldo", kwota, komentarz])

print(historia)

