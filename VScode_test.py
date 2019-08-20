import sys, requests

# print(sys.version)    #Printer hvilken versjon som blir brukt
print(sys.executable)  # Printer hvor filen befinner seg


def Hilsen(hvem):
    Hils = "Hei, {}".format(hvem)
    return Hils


r = requests.get("https://snl.no")
print(r.status_code)

"""
Code-runner er en ekstention som kun har "read only - output"
For å kunne bruke input må man kjøre koden i terminalen. 
Enten på gamle måten eller høyre klikk i vinduet å kjør i terminalen.
"""
# name = input("Your name? ")
# print(Hilsen(name))

