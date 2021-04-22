from getpass import getpass
import os
import time

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

def loading():
    i = 0
    while i < 8:
        clear()
        if(i == 1):
            print("Betöltés.")
        if(i == 2):
            print("Betöltés..")
        if(i == 3):
            print("Betöltés...")
        if(i == 4):
            print("Betöltés.")
        if(i == 5):
            print("Betöltés..")
        if(i == 6):
            print("Betöltés...")
        time.sleep(0.5)
        i += 1

def megszakitas():
    i = 0
    while i < 4:
        clear()
        if(i == 1):
            print("Folyamat megszakítása folyamatban.")
        if(i == 2):
            print("Folyamat megszakítása folyamatban..")
        if(i == 3):
            print("Folyamat megszakítása folyamatban...")
        time.sleep(0.5)
        i += 1

def ellenorzes():
    i = 0
    while i < 4:
        clear()
        if(i == 1):
            print("Ellenőrzés.")
        if(i == 2):
            print("Ellenőrzés..")
        if(i == 3):
            print("Ellenőrzés...")
        time.sleep(0.5)
        i += 1

#INNEN INDUL    
clear = lambda: os.system('cls')
data = "userdata.txt"

try:
    f = open(data, "r")
except Exception:
    f = open(data, "x")
    f.close()
    print("Hiba történt! Kérlek indítsd újra a programot!")
    exit()

Counter = 0
Content = f.read() 
CoList = Content.split("\n") 

for i1 in CoList: 
    if i1: 
        Counter += 1

loading()
clear()

bemenet = input("--------------------------------------------------\nKöszöntelek a bejelentkező felületen!\nHasználd a 'B' betűt a bejelentkezéshez!\nNincsen még fiókod? Használd az 'R' betűt a regisztráláshoz!\n--------------------------------------------------\nB/R? ")

if(bemenet == "userlist"):
    f = open(data, "r")
    print("Talált felhasználók száma: " + str(Counter - 1)) 
    megszakitas()
    time.sleep(1)

if(bemenet == "b" or bemenet == "B"):
    
    username = input("Felhasználónév: ")
    password = getpass("Jelszó: ")
    
    i = 0
    f = open(data, "r")

    while(i <= Counter):
        temp = Convert(f.readline())
        if(username == temp[0]):
            ellenorzes()

            if(password == str(temp[1]).replace("\n", "")):
                print("Sikeresen bejelentkeztél!")
                time.sleep(3)
            else:
                print("Helytelen adatokat adtál meg!")
                megszakitas()
                time.sleep(1)
        i+=1

if(bemenet == "R" or bemenet == "r"):

    clear()
    print("--------------------------------------------------\nA felhasználónevednek legalább 4 karakter hosszúságúnak kell lennie,\nValamint nem tartalmazhat ékezetes karaktereket!\n--------------------------------------------------\n")
    username = input("Felhasználónév: ")

    clear()
    print("--------------------------------------------------\nA jelszavadnak legalább 6 karakter hosszúságúnak kell lennie,\nValamint nem tartalmazhat ékezetes karaktereket!\n--------------------------------------------------\n")
    password1 = getpass("Jelszó: ")

    if(password1 == username):
        print("A jelszavad nem egyezhet meg a felhasználóneveddel!")

    else:
        if(len(password1) >= 6):
            if "á" or "é" or "ő" or "ö" or "ü" or "ó" or "ú" or "ű" or "í" not in password1:
                password2 = getpass("Jelszó újra: ")
                if(password1 == password2):
                    new_line = username+" "+password1
                    f = open(data, "a")
                    f.write("\n")
                    f.write(new_line)
                    clear()
                    print("A regisztráció sikeres volt!")
                    time.sleep(3)

                if(password1 != password2):
                    print("Az általad megadott felhasználónevek nem egyeznek!")
                    megszakitas()
                    time.sleep(1)
            
            else:
                print("A jelszavad nem tartalmazhat ékezetes karaktereket!")
                megszakitas()
                time.sleep(1)
        
        if(len(password1) < 6):
            print("A jelszavadnak legalább 6 karakter hosszúságúnak kell lennie!")
            megszakitas()
            time.sleep(1)

    