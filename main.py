import logpass

print("1. Polar Flow")
print("2. Strava")

service = int(input(">> "))
if(service == 1):
    import polar
elif(service == 2):
    import strava
else:
    print("Zly wybor")
    exit(1)

import endomondo
