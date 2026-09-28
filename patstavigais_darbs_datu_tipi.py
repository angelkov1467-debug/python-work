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

 






