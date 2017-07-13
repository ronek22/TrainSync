import getpass
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def InputLogin():
    print  "Podaj dane do konta Strava"
    print "-"*20
    userStr = raw_input("Podaj email: ")
    passwdStr = getpass.getpass("Podaj haslo: ")

    print "\nPodaj dane do konta Endomondo"
    print "-"*20
    userEnd = raw_input("Podaj email: ")
    passwdEnd = getpass.getpass("Podaj haslo: ")

    secret = open('client.secret', 'w')
    secret.write(userStr+","+passwdStr+'\n')
    secret.write(userEnd+","+passwdStr)
    secret.close()

def Menu():
    print("1. Edytuj dane logowania")
    print("2. Synchronizuj dane")
    print("3. Zamknij")
    choose = int(raw_input("\n>> "))
    cls()

    if choose == 1:
        InputLogin()
    elif choose == 2:
        pass
    else:
        print "Do zobaczenia  :)"
        exit(1)

if os.stat('client.secret').st_size == 0:
    InputLogin()
else:
    Menu()
