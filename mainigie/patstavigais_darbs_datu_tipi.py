#Definē divus skaitļu mainīgos
num1 = 20 #int
num2 =10.5 #float 
#Aprēķini šo skaitļu summu
summa = num1 + num2
#Izvada rezultātu
print(summa)
#Izvadi rezultātu divos veidos
print(summa)
print(float(summa))

"""Izvadi:
teksta garumu
pirmo simbolu
tekstu apgrieztā secībā
"""

#Definē teksta mainīgo
teksts = "Sveiki pasaule"
print(len(teksts)) #Izvada teksta garumu
print(teksts[0]) #Izvada pirmo simbolu
print(teksts[::-1]) #Izvada tekstu apgrieztā secībā


"""
Izveido sarakstu (list) ar vismaz 5 elementiem
(drīkst būt dažādi datu tipi).

Izvadi:
visu sarakstu
pirmo elementu
pēdējo elementu
Pievieno sarakstam vienu jaunu elementu.
Nomaini vienu esošu elementu sarakstā.
Izvadi saraksta elementu skaitu
"""

saraksts = ["grāmata", 5, "zīmulis", 10.5, "pasaule"] #Izveido sarakstu ar dažādiem datu tipiem
print(saraksts) #Izvada visu sarakstu
print(saraksts[0]) #Izvada pirmo elementu
print(saraksts[-1]) #Izvada pēdējo elementu
saraksts.append("mašīna") #Pievieno sarakstam jaunu elementu
print(saraksts) #Izvada sarakstu pēc jauna elementa pievienošanas
saraksts[3] = "komikss" #Nomaina vienu elementu
print(saraksts)
print(len(saraksts)) #Izvada saraksta elementu skaitu




"""
Izveido vārdnīcu (dictionary) ar informāciju par sevi, piemēram:
vārds
vecums
pilsēta
Izvadi katru vērtību atsevišķi, izmantojot atslēgas.
Pievieno vārdnīcai jaunu atslēgu.
Izmanto un izvada:
.keys()
.values()
"""

#Izveido vārdnīcu (dictionary) ar informāciju par sevi
vards = "Angelina"
vecums = 15
pilsēta = "Viļāni"
#Izvadi katru vērtību atsevišķi, izmantojot atslēgas
print(vards)
print(vecums)
print(pilsēta)

vārdnīca = {
    "vārds": vards,
    "vecums": vecums,
    "pilsēta": pilsēta
}


#Pievieno vārdnīcai jaunu atslēgu
darbs = "programmēšana"
vārdnīca["darbs"] = darbs
print(vārdnīca)

#Izmanto un izvada:
#.keys()
#.values()

#Izvada vārdnīcas atslēgas
print(vārdnīca.keys()) 
#Izvada vārdnīcas vērtības
print(vārdnīca.values()) 











#Risinajums!
"""
1. Numbers & Strings (5 min)
Definē divus skaitļu mainīgos:
vienu int
vienu float

Aprēķini šo skaitļu summu.

Izvadi rezultātu divos veidos:
vienkārši ar print()
izmantojot teksta paskaidrojumu (string + skaitļi) (piemēram, print("Vārds:",vards))

Definē teksta mainīgo (string).

Izvadi:
teksta garumu
pirmo simbolu
tekstu apgrieztā secībā

"""
skaitlis1 = 5
skaitlis2 = 5.5

print(skaitlis1+skaitlis2)
print("Skaitļu summa:", skaitlis1+skaitlis2)

teksts = "Varavīksne"
print(len(teksts))
print(teksts[0])
print(teksts[::-1])
"""
"""
# 2.saraksti 5 min
#Izveido sarakstu (list) ar vismaz 5 elementiem
#(drīkst būt dažādi datu tipi).

#Izvadi:
#visu sarakstu
#pirmo elementu
#pēdējo elementu

#Pievieno sarakstam vienu jaunu elementu.
#Nomaini vienu esošu elementu sarakstā.

#Izvadi saraksta elementu skaitu.
"""
"""
saraksts = [1,4,5,"Arbūzs",[5.7]]
print(saraksts)
print(saraksts[0])
print(saraksts[-1])
saraksts.append(10)
saraksts[1]=33
print(saraksts)
print(len(saraksts))

"""
3. Dictionary (5 min)
Izveido vārdnīcu (dictionary) ar informāciju par sevi, piemēram:

vārds
vecums
pilsēta

Izvadi katru vērtību atsevišķi, izmantojot atslēgas.

Pievieno vārdnīcai jaunu atslēgu.

Izmanto un izvada:
.keys()
.values()

"""
maniDati = {"vards":"Anna","vecums":5,"pilseta":"Vecpiebalga"}
print(maniDati["vards"])
print(maniDati["vecums"])
print(maniDati["pilseta"])
maniDati["skola"]="Vecpiebalgas pirmsskolas izglītības iestāde"
print(maniDati.keys())
print(maniDati.values())
