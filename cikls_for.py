#02_11_2026

#cikls - for

saraksts = [1, 2, 3, 4, 5]
print(saraksts)

#izvadīt katru elementu atsevišķi
print(saraksts[0])
print(saraksts[1])
print(saraksts[2])
print(saraksts[3])
print(saraksts[4])


#izmantojot ciklu for
print("Izvade ar ciklu for")
for elements in saraksts:
    print(elements)

#elementa meklešana sarakstā
produkti = ["piens", "maize", "olas", "bobs"]
izvele = input("Lūdzu ievadi savu miļāko augli:")

#meklešana izmantojot indeksu 
#problema šadai metodei - ja saraksta elements mainās, tas manuali ir jamaina
print("Versija ar indeksu")
if izvele == produkti[0]:
    print("Šis auglis ir saraksta")
elif izvele == produkti[1]:
    print("Šis auglis ir saraksta")
elif izvele == produkti[2]:
    print("Šis auglis ir saraksta")
elif izvele == produkti[3]:
    print("Šis auglis ir saraksta")
else:
    print("Šis auglis nav sarakstā")

#variants 2 
#meklešana ar nosacijumu, kur izmanto in (iekšeja cikla darbība)
print("Versija ar nosacijumu in")
if izvele in produkti:
    print("Šis auglis ir saraksta")
else:
    print("Šis auglis nav saraksta")

#variants 3 - izmantojot ciklu un salidzinašanu 
print("Versija ar ciklu un velak saidzināšanu")
atrasts = False #boolean tipa mainigais, kas tiek izmantots ka karodziņvērtība
for elements in produkti:
    if izvele == elements:
        atrasts = True

if atrasts == True:
    print("Šis auglis ir saraksta")
else:
    print("Šis auglis nav saraksta")


#skaitļu izvade, izmantotjot funkciju range()
for skaitlis in range(1,10):
    print(skaitlis)

#para skaitļu izvade, izmantojot range()
for skaitlis in range(1,11):
    if skaitlis %2 == 0:
        print(skaitlis, "ir para skaitlis")

#teksta izvade pa simboliem
teksts = "Python"

for simbols in teksts:
    print(simbols)

#vardnicas izvade, izmantojot ciklu for
skolens = {
    "vards": "Anna",
    "vecums": 16,
    "kurss": "Programmešana I"
}
print(skolens)
for atslega, vertiba in skolens.items():
    print(atslega, ":", vertiba)

