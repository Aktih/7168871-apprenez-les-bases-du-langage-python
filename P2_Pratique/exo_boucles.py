nombres = input("Veuillez saisir une liste de nombres separes par des virgules :")
print(nombres)

test=nombres.split(sep=",")

liste_entiers=[]

for nombre in test:
    nombre_int=int(nombre)
    liste_entiers.append(nombre_int)

print(liste_entiers)

somme=0
for nombre_int in liste_entiers:
    somme += nombre_int

moyenne = somme / len(liste_entiers)
print(moyenne)

nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)