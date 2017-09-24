import getpass
import os
from files import delTcx, clears



def InputLogin():
    print  "Podaj dane do konta Strava"
    print "-"*20
    userStr = raw_input("Podaj email: ")
    passwdStr = getpass.getpass("Podaj haslo: ")

    print "\nPodaj dane do konta Endomondo"
    print "-"*20
    userEnd = raw_input("Podaj email: ")
    passwdEnd = getpass.getpass("Podaj haslo: ")

    print "\nPodaj dane do konta PolarFlow"
    print "-"*20
    userP = raw_input("Podaj email: ")
    passwdP = getpass.getpass("Podaj haslo: ")

    secret = open('client.secret', 'w')
    secret.write(userStr+","+passwdStr+'\n')
    secret.write(userEnd+","+passwdStr+'\n')
    secret.write(userP+","+passwdP)
    secret.close()

def Menu():
    delTcx()
    print("1. Edytuj dane logowania")
    print("2. Synchronizuj dane")
    print("3. Zamknij")
    choose = int(raw_input("\n>> "))
    clears()

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
