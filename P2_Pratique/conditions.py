#1er cas
ensoleille = False
neige = False

if ensoleille :
    print("on va a la plage !")
elif neige :
    print("on fait un bonhomme de neige")
else : 
    print ("on reste a la maison")

#2e cas
avec_soleil = True
en_semaine = True

if avec_soleil and not en_semaine :
    print("on va a la plage !")
elif avec_soleil and en_semaine :
    print("on va au travail")
else : 
    print ("on reste a la maison")

#3e cas
nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
    print("autoriser")
else:
    print("ne plus autoriser")

#4e cas 
fruit = "orange"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")