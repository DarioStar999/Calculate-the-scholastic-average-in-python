print("""
     ____         _      ___    
    |    \       /_\    / _  \   (_)   _____
    |  _   \    /|_|\  | |_| |    _   |     |
    | | |   |  | | | | |  _  |   | |  |     |
    | |_|   |  |  _  | | | \ \   | |  |     |
    |______|   |_| |_| |_|  \_|  |_|  |_____| DarioStar999
""")
totalevoti =  int(input("Quanti voti hai in totale?Inserisci un numero tra 2 e 50: "))
c = 0
for i in range (totalevoti):
     c += int(input("Inserisci il voto: "))

print(f"La media è: {c/totalevoti}") 
