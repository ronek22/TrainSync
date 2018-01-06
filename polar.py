import os
import config
from flow import FlowClient
from files import clears
import endoData

clears()

client = FlowClient()

with open('client.secret') as cred:
    f = cred.readlines()
    userP, passwdP = f[2].strip().split(',')
    client.login(userP, passwdP)
    activities = client.activities()[::-1]



def sync_data():
    lastEndo = endoData.run()
    count = 0

    for work in activities:
        if(work.datetime[:10] <= lastEndo):
            break
        count += 1
    return count


print("1. Synchronizacja automatyczna")
print("2. Podaj ilosc treningow do zsynchronizowania")

choose = 1 if config.automate else int(input("\n>> "))
clears()

if choose == 1:
    ile = sync_data()
elif choose == 2:
    ile = int(input("Ilosc trenigow: "))
    clears()
else:
    print("Nie ma takiej opcji. Bye")
    exit(1)

print('{:~^30}'.format('PolarFlow'))
for i in range(ile):
    print("Plik %d.tcx pobierany" % i)
    content = activities[i].tcx()
    with open(str(i) + '.tcx', 'wb') as save:
        save.write(content)
