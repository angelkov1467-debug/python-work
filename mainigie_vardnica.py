#28_09_2026
"""
✍️ Praktiskais uzdevums
Izveido vārdnīcu par sevi (iekļauj: vārds, vecums un iegūtā izglītība (pamatskolas, vidusskolas, augstākā un t.t.))
Izvadi izveidoto vārdnīcu

Izvadi vārdnīcas atslēgas
Izvadi vārdnīcas atslēgu vērtības

Izmanto .keys() un .values()

Iedomājies, ka jau esi nosvinējis dzimšanas dienu un maini vērtību atslēgā vecums
Izvadi visu vārdnīcu

Izvadi tikai atslēgas vecums vērtību
"""

cilvekaDati = {"vards":"Janis", "vecums": 25, "izglītība": "augstākā"}#Atslēgu nosaukumus neikļaujam mīkstinājuma zīme
print(cilvekaDati)
#Izvadi vārdnīcas atslēgas un vērtības
print(cilvekaDati.keys())
print(cilvekaDati.values())
cilvekaDati["vecums"] = 26 
#Izvadi visu vārdnīcu
print(cilvekaDati)
print(cilvekaDati["vecums"])





