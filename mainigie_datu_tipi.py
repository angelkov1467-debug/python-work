#5_10_2026
# ============================================================
# 1. UZDEVUMS — MANS VĀRDS
# ============================================================
#
# Izveido mainīgo "vards".
# Piešķir tam savu vārdu.
# Izdrukā mainīgā vērtību.
#
# Piemēram, ja vārds ir Anna, programmai jāizvada:
#
# Anna
#
# Tavs kods:
# ------------------------------------------------------------
vards = "Angelina"
print(vards)



# ============================================================
# 2. UZDEVUMS — PAR MANI
# ============================================================
#
# Izveido trīs mainīgos:
#
# vards
# uzvards
# pilseta
#
# Piešķir tiem atbilstošas vērtības.
#
# Izdrukā:
#
# Mani sauc Anna Bērziņa.
# Es dzīvoju Rēzeknē.
#
# Protams, izmanto savu informāciju.
#
# Tavs kods:
# ------------------------------------------------------------
vards = "Angelina"
uzvards = "Kovalova"
pilseta= "Vilani"

print("Mani sauc", vards, uzvards)
print("Es dzīvoju", pilseta,)





# ============================================================
# 3. UZDEVUMS — MAINĪGĀ VĒRTĪBAS MAIŅA
# ============================================================
#
# Izveido mainīgo:
#
# pilseta = "Rēzekne"
#
# Izdrukā tā vērtību.
#
# Pēc tam piešķir mainīgajam jaunu vērtību:
#
# "Viļāni"
#
# Vēlreiz izdrukā mainīgo.
#
# Tavs kods:
# ------------------------------------------------------------

pilseta = "Rezekne"
print(pilseta)
pilseta = "Vilani"
print(pilseta)



# Jautājums:
# Vai mainīgā vērtība Python programmā var mainīties?
#
# Atbildi komentārā:
#
# Atbilde:
# Ja, jo mes varam pamainit to :D





# ============================================================
# 4. UZDEVUMS — VESELS SKAITLIS (int)
# ============================================================
#
# Izveido mainīgo "vecums".
# Piešķir tam savu vecumu.
#
# Izdrukā:
#
# Man ir XX gadi.
#
# XX vietā jāparādās mainīgā "vecums" vērtībai.
#
# Tavs kods:
# ------------------------------------------------------------
vecums = 15
print("Man ir", vecums, "gadi.")



# ============================================================
# 5. UZDEVUMS — APRĒĶINI
# ============================================================
#
# Izveido:
#
# a = 15
# b = 7
#
# Aprēķini un izdrukā:
#
# 1. summu
# 2. starpību
# 3. reizinājumu
#
# Vēlamais rezultāts:
#
# Summa: 22
# Starpība: 8
# Reizinājums: 105
#
# Tavs kods:
# ------------------------------------------------------------

a = 15
b = 7
summa = a+b
starpiba = a-b
reizinajums = a*b
print("Summa:", summa)
print("Starpība:", starpiba)
print("Reizinājums:", reizinajums)





# ============================================================
# 6. UZDEVUMS — NĀKAMAIS GADS
# ============================================================
#
# Izveido mainīgo "vecums".
#
# Aprēķini, cik gadu tev būs pēc viena gada.
#
# Programmai jāizvada:
#
# Pēc gada man būs XX gadi.
#
# Aprēķinam izmanto mainīgo "vecums".
#
# Tavs kods:
# ------------------------------------------------------------


vecums = 15
vecums = vecums + 1
print("Pēc gada man būs", vecums, "gadi.")





# ============================================================
# 7. UZDEVUMS — DECIMĀLSKAITLIS (float)
# ============================================================
#
# Izveido mainīgo:
#
# cena = 2.50
#
# Izdrukā:
#
# Produkta cena ir 2.5 eiro.
#
# Tavs kods:
# ------------------------------------------------------------
cena = 2.50
print("Produkta cena ir", cena, "eiro.")



# ============================================================
# 8. UZDEVUMS — DIVU PRODUKTU CENA
# ============================================================
#
# Izveido:
#
# cena1 = 2.50
# cena2 = 3.75
#
# Aprēķini abu produktu kopējo cenu.
#
# Izdrukā:
#
# Kopā: 6.25 eiro
#
# Tavs kods:
# ------------------------------------------------------------
cena1 = 2.50
cena2 = 3.75
kopeja_cena = cena1 + cena2
print("Kopā:", kopeja_cena, "eiro.")




# ============================================================
# 9. UZDEVUMS — TEMPERATŪRA
# ============================================================
#
# Izveido mainīgo "temperatura".
# Piešķir tam vērtību 18.5.
#
# Izdrukā:
#
# Šodien temperatūra ir 18.5 °C.
#
# Pēc tam izmanto funkciju type(), lai pārbaudītu
# mainīgā "temperatura" datu tipu.
#
# Tavs kods:
# ------------------------------------------------------------
temperatura = 18.5
print("Šodien temperatūra ir", temperatura, "°C.")
print(type(temperatura))





# ============================================================
# 10. UZDEVUMS — ATPAZĪSTI DATU TIPU
# ============================================================
#
# Apskati mainīgos:
#
# vards = "Jānis"
# vecums = 16
# atzime = 7.5
#
# Pie katra mainīgā komentārā norādi datu tipu.
#
# Piemēram:
#
# vards = "Jānis"       # str
#
# Tavs kods:
# ------------------------------------------------------------

vards = "Jānis"  # str
vecums = 16      # int
atzime = 7.5     # float




# ============================================================
# 11. UZDEVUMS — type()
# ============================================================
#
# Izveido mainīgos:
#
# vards = "Anna"
# vecums = 15
# atzime = 8.5
#
# Izmanto type(), lai pārbaudītu visu trīs mainīgo tipus.
#
# Programmai jāizvada trīs rezultāti.
#
# Tavs kods:
# ------------------------------------------------------------

vards = "Anna"
vecums = 15
atzime = 8.5
print(type(vards))
print(type(vecums))
print(type(atzime))



# ============================================================
# 12. UZDEVUMS — LIST
# ============================================================
#
# Izveido sarakstu "draugi".
#
# Sarakstā ievieto vismaz trīs draugu vārdus.
#
# Izdrukā visu sarakstu.
#
# Tavs kods:
# ------------------------------------------------------------

list = ["Janis", "Anna", "Banans"]
print(list)





# ============================================================
# 13. UZDEVUMS — LIST ELEMENTI
# ============================================================
#
# Izmantojot sarakstu "draugi" no iepriekšējā uzdevuma,
# izdrukā:
#
# 1. pirmo elementu;
# 2. otro elementu;
# 3. trešo elementu.
#
# Atceries:
# Python saraksta pirmā elementa indekss ir 0.
#
# Tavs kods:
# ------------------------------------------------------------

draugi = ["Janis", "Anna", "Banans"]
print(draugi[0])
print(draugi[1])
print(draugi[2])


# ============================================================
# 14. UZDEVUMS — MANI HOBIJI
# ============================================================
#
# Izveido sarakstu "hobiji".
#
# Sarakstā jābūt vismaz četriem hobijiem.
#
# Izdrukā:
# 1. pirmo hobiju;
# 2. pēdējo hobiju.
#
# Tavs kods:
# ------------------------------------------------------------
hobiji = ["Lasit", "Peldet", "Zimet", "Gleznot"]
print(hobiji[0])
print(hobiji[3])




# ============================================================
# 15. UZDEVUMS — PIEVIENO ELEMENTU
# ============================================================
#
# Izveido sarakstu:
#
# augli = ["ābols", "bumbieris", "banāns"]
#
# Izmanto append(), lai sarakstam pievienotu:
#
# "apelsīns"
#
# Pēc tam izdrukā visu sarakstu.
#
# Tavs kods:
# ------------------------------------------------------------

augli = ["ābols", "bumbieris", "banāns"]
augli.append("apelsins")
print(augli)




# ============================================================
# 16. UZDEVUMS — MAINĪT LIST ELEMENTU
# ============================================================
#
# Izveido:
#
# krasa = ["sarkana", "zila", "zaļa"]
#
# Nomaini "zila" pret "dzeltena".
#
# Izdrukā sarakstu.
#
# Rezultātam jābūt:
#
# ['sarkana', 'dzeltena', 'zaļa']
#
# Tavs kods:
# ------------------------------------------------------------

krasa = ["sarkana", "zila", "zala"]
krasa[1] = "dzeltena"
print(krasa)




# ============================================================
# 17. UZDEVUMS — DICTIONARY
# ============================================================
#
# Izveido vārdnīcu "skolens".
#
# Tajā jābūt:
#
# vards
# vecums
# pilseta
#
# Izmanto savus datus.
#
# Izdrukā visu vārdnīcu.
#
# Tavs kods:
# ------------------------------------------------------------

skolens = {
    "vards": "Angelina",
    "vecums": 15,
    "pilseta": "Vilani" 

}

print(skolens)



# ============================================================
# 18. UZDEVUMS — DICTIONARY VĒRTĪBAS
# ============================================================
#
# Izmantojot iepriekšējo vārdnīcu "skolens",
# izdrukā atsevišķi:
#
# 1. vārdu;
# 2. vecumu;
# 3. pilsētu.
#
# Tavs kods:
# ------------------------------------------------------------

print(skolens["vards"])
print(skolens["vecums"])
print(skolens["pilseta"])






# ============================================================
# 19. UZDEVUMS — PIEVIENO DICTIONARY INFORMĀCIJU
# ============================================================
#
# Izveido vārdnīcu:
#
# skolens = {
#     "vards": "Anna",
#     "vecums": 16
# }
#
# Pievieno tai jaunu informāciju:
#
# "pilseta": "Rēzekne"
#
# Pēc tam izdrukā visu vārdnīcu.
#
# Tavs kods:
# ------------------------------------------------------------

skolens = {
    "vards": "Anna",
    "vecums": 16
}

skolens["pilseta"] = "Rēzekne"
print(skolens)




# ============================================================
# 20. UZDEVUMS — ATPAZĪSTI VISUS DATU TIPUS
# ============================================================
#
# Apskati:
#
# a = "Python"
# b = 25
# c = 3.14
# d = ["ābols", "bumbieris"]
# e = {"vards": "Anna"}
#
# Katram mainīgajam ar komentāru norādi datu tipu.
#
# Piemēram:
#
# a = "Python"  # str
#
# Pēc tam izmanto type(), lai pārbaudītu savas atbildes.
#
# Tavs kods:
# ------------------------------------------------------------

a = "Python" #str
b = 25 #int
c = 3.14 #float
d  = ["ābols", "bumbieris"] #list
e = {"vards": "Anna"} #dict

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# ============================================================
# 21. UZDEVUMS — IZVEIDO PATS
# ============================================================
#
# Izveido piecus mainīgos:
#
# 1. str
# 2. int
# 3. float
# 4. list
# 5. dictionary
#
# Izmanto savas izvēlētas vērtības.
#
# Pēc tam izmanto type(), lai pārbaudītu visu piecu
# mainīgo datu tipus.
#
# Tavs kods:
# ------------------------------------------------------------

str = "Banani" #str
int = 36 #int
float = 3.14 #float
list = ["Banan", "Papa", "Mama"] #list
dictionary = {"vards": "Anna", "vecums": 16} #dict

print(type(str))
print(type(int))
print(type(float))
print(type(list))
print(type(dictionary))



# ============================================================
# 22. UZDEVUMS — MANS PROFILS
# ============================================================
#
# Izveido programmu "Mans profils".
#
# Programmā OBLIGĀTI izmanto visus piecus datu tipus:
#
# str
# int
# float
# list
# dictionary
#
# Informācijai jābūt par tevi.
#
# Programmā jābūt:
#
# - vārdam;
# - vecumam;
# - vidējai atzīmei;
# - vismaz 3 hobijiem;
# - pilsētai.
#
# Programmai jāizvada informācija saprotamā veidā.
#
# Piemēram:
#
# MANS PROFILS
# ------------
# Vārds: Anna
# Vecums: 16
# Vidējā atzīme: 8.2
# Hobiji: ['mūzika', 'sports', 'spēles']
# Pilsēta: Rēzekne
#
# Tavs kods:
# ------------------------------------------------------------

Mans_profils = { 
      
    "vards": "Angelina",
    "vecums": 15,
    "vidējā atzīme": 9.5,
    "hobiji": ["Lasit", "Peldet", "Zimet"],
    "pilseta": "Vilani"

}

print(Mans_profils)



# ============================================================
# PAŠNOVĒRTĒJUMS
# ============================================================
#
# Atbildi komentāros.
#
# 1. Es protu izveidot mainīgo:
# [*] Jā
# [ ] Daļēji
# [ ] Vēl ne
#
# 2. Es protu atšķirt str, int un float:
# [*] Jā
# [ ] Daļēji
# [ ] Vēl ne
#
# 3. Es protu izveidot list:
# [*] Jā
# [ ] Daļēji
# [ ] Vēl ne
#
# 4. Es protu piekļūt list elementam:
# [*] Jā
# [ ] Daļēji
# [ ] Vēl ne
#
# 5. Es protu izveidot dictionary:
# [*] Jā
# [ ] Daļēji
# [ ] Vēl ne
#
# 6. Es protu iegūt vērtību no dictionary:
# [ ] Jā
# [*] Daļēji
# [ ] Vēl ne
#
# 7. Man vēl nav skaidrs:
#
# _________________________________________________



































