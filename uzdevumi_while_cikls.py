#09_11_2026

#cikls while
"""
1. uzdevums – skaitītājs (number)
Izmanto ciklu while, lai:

izvadītu skaitļus no 1 līdz 10

Padoms: izmanto skaitītāja mainīgo.
"""

#izvada skaitlus no 1 lidz 10

skaitlis = 1
while skaitlis < 11:
    print(skaitlis)
    skaitlis += 1 



"""
2. uzdevums – pāra skaitļi
Izmanto ciklu while, lai:

izvadītu tikai pāra skaitļus no 1 līdz 20

 Padoms: izmanto if nosacījumu.
"""
skaitlis = 1
while skaitlis < 21:
    if skaitlis %2 == 0:
        print(skaitlis)
    skaitlis += 1



"""
 3. uzdevums – teksts (string)
Dots teksts:
"""
 
text = "Python"
 
"""
Izmanto ciklu while, lai:

izvadītu katru burtu atsevišķā rindā

 Padoms: izmanto indeksu (i).
"""

i = 0
while i < len(text):
    print(text[i])
    i += 1



"""
 4. uzdevums – saraksts (list)
Dots saraksts:

 
numbers = [3, 6, 1, 8, 4]
 
 
Izmanto ciklu while, lai:

izvadītu visus saraksta elementus

saskaitītu un izvadītu visu skaitļu summu
"""

i = 0
numbers = [3, 6, 1, 8, 4]
summa = 0

while i < len(numbers):
    print(numbers[i])
    summa += numbers[i]
    i += 1
    print("Skaitļu summa ir:", summa)






