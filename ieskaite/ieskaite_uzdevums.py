# Izveido Python programmu failā uzdevums.py. Programmai jādarbojas atbilstoši šādām prasībām. 

# Izveido mainīgo vards, kurā saglabā lietotāja ievadīto vārdu. (2 p.) 

# Izveido mainīgo vecums, kurā saglabā veselu skaitli 16. (1 p.) 

# Izveido mainīgo atzime, kurā saglabā decimālskaitli 8.5. (1 p.) 

# Izveido sarakstu prieksmeti ar vismaz trim mācību priekšmetiem. (2 p.) 

# Izveido vārdnīcu skolens, kurā glabā vismaz skolēna vārdu un vecumu. (2 p.) 

# Izmanto print(), lai izvadītu skolēna vārdu, vecumu, atzīmi un mācību priekšmetu sarakstu. (2 p.) 

# Programmai jāizmanto norādītie mainīgo nosaukumi. Datu ievadei izmanto input(). Nav nepieciešams veidot nosacījumus vai ciklus. 

vards = input("Ievadi vārdu: ")
vecums = 16
atzime = 8.5    
prieksmeti = ["Python", "HTML", "CSS"]
skolens = {"vards": vards, "vecums": vecums} # type: ignore
print("Vārds:", skolens["vards"]) # type: ignore
print("Vecums:", skolens["vecums"]) # type: ignore
print("Atzīme:", atzime)
print("Mācību priekšmeti:", prieksmeti)



