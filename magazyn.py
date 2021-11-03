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
        historia.append(komenda)
    elif akcja == "zakup":
        komenda.append('zakup')
        komenda.append(input())
        komenda.append(int(input()))
        komenda.append(int(input()))
        historia.append(komenda)
    elif akcja == "sprzedaz":
        komenda.append('sprzedaz')
        komenda.append(input())
        komenda.append(int(input()))
        komenda.append(int(input()))
        historia.append(komenda)
    else:
        pass

print(historia)

for komenda in historia:
    if komenda[0] == 'saldo':
        stan_konta_po_akcji = saldo + komenda[1]
        if stan_konta_po_akcji >= 0:
            saldo = stan_konta_po_akcji
        else:
            print("Za malo srodkow")
            break

    if komenda[0] == 'zakup':
        stan_konta_po_akcji = saldo - komenda[2] * komenda[3]
        if stan_konta_po_akcji >= 0:
            saldo = stan_konta_po_akcji
            if not komenda[1] in magazyn:
                magazyn[komenda[1]] = komenda[3]
            else:
                magazyn[komenda[1]] += komenda[3]

    if komenda[0] == 'sprzedaz':
        if magazyn.get(komenda[1], -1) >= komenda[3]:
            magazyn[komenda[1]] -= komenda[3]
            saldo += komenda[2] * komenda[3]
        else:
            break

print(magazyn)
print(saldo)




