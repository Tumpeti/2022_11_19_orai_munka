""" ISMÉTLÉS: # lista utolsó elemét elérni =
lista = [5,6,7,8]
utolso = lista[len(lista)-1]
# hozzáadás az append paranccsal
lista.append(9)"""

"""
# 3. feladat
homerseklet = [0,12,13,9,2,7]
i = 0
elozonap_homerseklete = 0
csokkent_a_homerseklet = []
while i < len(homerseklet):
    aktualis_nap = homerseklet[i]
    if aktualis_nap - 3 <= elozonap_homerseklete:
        csokkent_a_homerseklet.append(i)
    i += 1
    elozonap_homerseklete = homerseklet[i-1]
print(f"Októberben a {csokkent_a_homerseklet} napokon csökkent a hőmérséglet három vagy több mint három fokkal.")
"""
"""
# szövegkezelés
# 1
szoveg = input("Kérek egy tetszőleges szöveget: ")
szoveg = szoveg.upper()
print(szoveg)
# 2
if len(szoveg) > 10:
    print(f"A szöveg hossza {len(szoveg)} karakter.")
"""
# 3
"""

szoveg2 = input("Kérek egy legalább három betűs szöveget!")
szoveg2 = szoveg2.upper()
if len(szoveg2) < 3:
    print("Nem elég hosszú a szöveg!")
"""
# 4
"""print("Az első a helye: ")
print(szoveg2.find("a"))
print("Az összes a száma: ")
print(szoveg2.count("a"))
"""
"""
i = 0
while i < len(szoveg2):
    if szoveg2[i] == "A":
        print(f"A {i+1}. helyen áll az első a betű.")
        break
    else: i += 1
"""
# Zsolt variációja:

szoveg_jo = False
while not szoveg_jo:
    szoveg = input("Adjon meg egy legalább hárombetűs szót! ")
    if len(szoveg) >= 3:
        szoveg_jo = True

# 5
i = 0
osszes_a = 0
while i < len(szoveg):
    if szoveg.upper()[i] == "A":
        osszes_a += 1
    i += 1
print(f"Az összes a betű száma: {osszes_a}")
# 1

nevek_lista = ""
egy_nev = 0
while egy_nev != "@":
    egy_nev = (input("Kérek neveket: "))
    if egy_nev == "@":
        break
    nevek_lista += egy_nev + " "
print(nevek_lista)

