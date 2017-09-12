import os
from flow import FlowClient
import endoData

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
client = FlowClient()
f = open('client.secret').readlines()
userP,passwdP = f[2].strip().split(',')
client.login(userP,passwdP)
activities = client.activities()[::-1]

def sync_data():
    lastEndo = endoData.run()
    count = 0

    for work in activities:
        if(work.datetime[:10]<=lastEndo):
            break
        count+=1
    return count

print "1. Synchronizacja automatyczna"
print "2. Podaj ilosc treningow do zsynchronizowania"

choose = int(raw_input("\n>> "))
cls()

if choose==1:
    ile = sync_data()
elif choose==2:
    ile = int(raw_input("Ilosc trenigow: "))
    cls()
else:
    print "Nie ma takiej opcji. Bye"
    exit(1)

for i in range(ile):
    content = activities[i].tcx()
    with open(str(i)+'.tcx','w') as save:
        save.write(content)
