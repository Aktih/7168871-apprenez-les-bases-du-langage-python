nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

print(nouvelle_campagne)

# methode 1
taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

# methode 2
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

nouvelle_campagne['responsable_de_campagne']
taux_de_conversion['facebook']

infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"
print(infos_labradoodle)

infos_labradoodle["poids"] = "45 kg"
print(infos_labradoodle)

# supprime la paire cle-valeur origine
del infos_labradoodle["origine"]
print(infos_labradoodle)

# verifier la presence d'une cle dans un dictionnaire
"poids" in infos_labradoodle
"race" in infos_labradoodle