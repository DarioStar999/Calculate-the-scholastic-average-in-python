print("""
     ____         _      ___    
    |    \       /_\    / _  \   (_)   _____
    |  _   \    /|_|\  | |_| |    _   |     |
    | | |   |  | | | | |  _  |   | |  |     |
    | |_|   |  |  _  | | | \ \   | |  |     |
    |______|   |_| |_| |_|  \_|  |_|  |_____| DarioStar999
""")
totalevoti =  int(input("How many grades do you have? "))
c = 0
for i in range (totalevoti):
     c += int(input("Insert the grade:  "))

print(f"Your grade average is: {c/totalevoti}") 
