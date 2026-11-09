#02_11_2026
#treninuzdevumi - cikls for
"""
1. uzdevums - skaitļi
Izmanto ciklu for, lai:

izvadītu visus skaitļus no 1 līdz 10

izvadītu tikai pāra skaitļus

Padoms: izmanto range() un if nosacījumu.
"""

#skaitļi kurus mes izvadīsim
skaitlis = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]


#para skaitļu izvade, izmantojot range()
for skaitlis in range(1,11):
    if skaitlis %2 == 0:
        print(skaitlis, "ir para skaitlis")


#izvadīt visus skaitļus no 1 līdz 10
for skaitlis in range(1,11):
    print(skaitlis)




"""
2. uzdevums - teksts (string)
Dots teksts:

 
text = "Programmēšana"
 
 
Izmanto ciklu for, lai:

izvadītu katru burtu jaunā rindā

saskaitītu, cik burtu ir tekstā

Padoms: izmanto skaitītāja mainīgo.
"""

#teksta izvade pa simboliem
teksts = "Programmēšana"


simbolu_skaits = 0
for simbols in teksts:
    print(simbols)
    simbolu_skaits += 1




for simbols in teksts:
    print(simbols)



"""
3. uzdevums - saraksts (list)
Dots saraksts:
"""
 
numbers = [4, 7, 2, 9, 12]
 
"""
Izmanto ciklu for, lai:

izvadītu katru skaitli

izvadītu tikai tos skaitļus, kas ir lielāki par 5
"""
#izmantojot ciklu for 
print("Izvade ar ciklu for")
for elements in numbers:
    print(elements)


for elements in numbers:
    if elements > 5:
        print(elements, "ir lielaks par 5")
    





"""
4. uzdevums - vārdnīca (dictionary)
Dots vārdnīcas objekts:

 
student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}
 
 
Izmanto ciklu for, lai:

izvadītu katru atslēgu un tās vērtību šādā formātā:
"""


student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}
print(student)
for atslega, vertiba in student.items():
    print(atslega, ":", vertiba)











