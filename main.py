import logpass
import config
automate = False

print("1. Polar Flow")
print("2. Strava")
print("3. Automatic: Polar -> Endomondo")



service = int(input(">> "))
if(service == 1):
    import polar
elif(service == 2):
    import strava
elif(service == 3):
    config.automate = True
    import polar
else:
    print("Zly wybor")
    exit(1)

import endomondo
input("Do widzenia")
