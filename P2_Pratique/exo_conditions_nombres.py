nombre1 = input()

print(nombre1)
test_nb1 = nombre1.isnumeric()
print(test_nb1)

nombre2 = input()

print(nombre2)
test_nb2 = nombre2.isnumeric()
print(test_nb2)

if test_nb1 == False:
    raise SystemExit("Fin du programme")
else:
    nombre1=int(nombre1)

if test_nb2 == False:
    raise SystemExit("Fin du programme")
else:
    nombre2=int(nombre2)

operation = input()
print(operation)

match operation:
    case "+":
        print("Addition")
    case "-":
        print("Soustraction")
    case "*":
        print("Multiplication")
    case "/":
        print("Division")
    case _:
        raise SystemExit("Fin du programme")

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1-nombre2
elif operation == "*":
    resultat = nombre1*nombre2
elif operation == "/" and nombre1 != 0 and nombre2 != 0:
    resultat = round(nombre1/nombre2)
else: 
    raise SystemExit("Fin du programme")

print(resultat)
