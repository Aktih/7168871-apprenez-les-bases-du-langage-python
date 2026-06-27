# calculator : package
# operations : module
# addition / multiplication :  fonctions

# Methode 1 : import de tout le module
import calculator.operations

resultat = calculator.operations.addition(3,5)
print(resultat)

# Methode 2 : import d'une fonction specifique du module
from calculator.operations import multiplication

resultat2 = multiplication(8,2)
print(resultat2)