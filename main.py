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



