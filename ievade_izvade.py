#28_09_2026

#Ievades un izvade 

#ievades funkcija ir input()

vards =input("Ievadi savu vardu:") #Ievades funkcija, kas prasa vardu
print("Tavs vard ir",vards)

vecums = int(input("Ievadi savu vecumu: ")) #Ievades funkcija, kas prasa vecumu
print("Tu esi dzimis",2026-vecums,"gada")

#ka vel var
vecums = int(input("Ievadi savu vecumu: ")) #Ievades funkcija, kas prasa vecumu
dzimsanasGads = 2026-int(vecums) #int() - parveido tekstu veselā skaitlī
print("Tu esi dzimis "+str(dzimsanasGads)+". gada")


#SHORTCUT : ctrl+K+C(parveidot par komentāru) ctrl+K+U(parveidot par kodu)

#Pievienot vērtību sarakstam
prieksmeti = [] #Definējam tukšu sarakstu
prieksmeti.append(input("Ievadi 1. priekšmetu: "))
prieksmeti.append(input("Ievadi 2. priekšmetu: "))
print(prieksmeti)


#Pievienot vērtību vardnīcai
skolens = {} #Definējam tukšu vārdnīcu
skolens["vards"] = input("Ievadi skolēna vārdu: ")
skolens["vecums"] = input("Ievadi skolēna vecumu: ")
print(skolens)








