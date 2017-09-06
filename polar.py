import os
from flow import FlowClient
client = FlowClient()

f = open('client.secret').readlines()
userP,passwdP = f[2].strip().split(',')

client.login(userP,passwdP)

ile = int(raw_input("Ile aktywnosci chcesz pobrac? (max = 10)\n>> "))

activities = client.activities()[::-1]
for i in range(ile):
    name = activities[i].tcx()
    os.rename(name,str(i)+'.tcx')
