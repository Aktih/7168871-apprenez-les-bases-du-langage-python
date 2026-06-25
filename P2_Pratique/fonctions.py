def afficher_message():
    print("Bonjour, comment ça va ?")

afficher_message()

def afficher_nom_prenom(nom, prenom):
    print("Nom :", nom)
    print("Prénom :", prenom)

afficher_nom_prenom("Lamps","Nicolas")

def calculer_somme(a, b):
  resultat = a + b
  return resultat

somme = calculer_somme(10,56)
print(somme)