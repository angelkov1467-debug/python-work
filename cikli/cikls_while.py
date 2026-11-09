#09_11_2026

#cikls while

#izpildas, tik ilgi, kamer ir true

#izvadit skitlus lidz 5
skaitlis = 1
while skaitlis < 5:
    print(skaitlis)
    skaitlis += 1

#parbaudit lietotaja paroli
parole = ""

while parole != "1234":
    parole =input("Ievadi paroli: ")

print("Parole ir pareiza")

#break and continue

#break 

skaitlis = 1
while skaitlis < 6:
    print(skaitlis)
    skaitlis += 1
    if skaitlis == 3:
        break
print("Cikls beidzas, jo skaitlis ir 3")


#continue - IZLAIŽ VIENU ATKARTOJUMU
skaitlis = 1
while skaitlis < 6:
    print("skaitlis ir vienads ar 3")
    skaitlis += 1
    continue
print(skaitlis)
skaitlis =+ 1

