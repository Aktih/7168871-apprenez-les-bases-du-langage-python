fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}

fruits["kiwi"] = "vert"
print(fruits)

couleur_banane = fruits["banane"]
print(couleur_banane)

fruits["pomme"] = "vert"
print(fruits)

del(fruits["banane"]) # delete de la cle banane
print(fruits.keys())