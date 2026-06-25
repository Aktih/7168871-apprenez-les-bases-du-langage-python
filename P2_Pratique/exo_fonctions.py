def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel/12
    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel/4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

salaire_annuel = input("Quel est votre salaire annuel ?")
salaire_annuel = float(salaire_annuel)

salaire_mens = salaire_mensuel(salaire_annuel)
print(salaire_mens)
salaire_hebdo = salaire_hebdomadaire(salaire_mens)
print(salaire_hebdo)

heures_travaillees = input("Combien d'heures travaillez-vous par semaine ?")
heures_travaillees = float(heures_travaillees)

salaire_horaire_def = salaire_horaire(salaire_hebdo, heures_travaillees)
print ("Votre salaire horaire est de", round(salaire_horaire_def, 2), "euros")