#09_11_2026

#funkcijas

#funkcija - koda bloks, kur var izmantot vairakart

#funkcijas piemers - saskaitišana
def summa(skaitlis1, skaitlis2):
    return skaitlis1 + skaitlis2

rezultats = summa(5,5)
print(rezultats)


#funkcijas piemers - teksta atgriešana

def sveiciens(vards):
    return "Sveiki, " +vards+ "!"
vards = input("Ievadi savu vardu: ")
print(sveiciens(vards))


#funkcijas piemers - saraksta elementu skaitīšana


def elementu_skaits(saraksts):
    skaits = 0 
    for elements in saraksts:
        skaits += 1
    return skaits
print(elementu_skaits([1, 4, 6]))

#funkcijas piemers - parbaude, vai vardnica ir noteikta atslega

def vai_atslega_ir(dati,atslega):
    if atslega in dati:
        return "Atslega ir atrasta"
    else:
        return "Atslega nav atrasta"


students = {"vards": "Jānis", "vecums": 16}
print(vai_atslega_ir(students, "bob"))


#funkcijas piemers - bez return

def vai_atslega_ir(dati,atslega):
    if atslega in dati:
        print("Atslega ir atrasta")
    else:
        print("Atslega nav atrasta")


students = {"vards": "Jānis", "vecums": 16}
vai_atslega_ir(students, "bob")





























