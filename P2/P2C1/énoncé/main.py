# Ecrivez votre code ici !

# demander à l'utilisateur de saisir deux nombres à calculer
nombre1 = input("Entrez le premier nombre en entier ici : ")
nombre2 = input("Entrez le deuxième nombre entier ici : ")

# vérifier si les nombres saisir sont des nombres en string si c'est pas le cas on quitte le programme
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur les nombres saisir doivent être en entier.")
    raise SystemExit("Fin du programme")

# conversion des nombres saisis en entier
nombre1, nombre2 = int(nombre1), int(nombre2)

operation = input("saisissez l'opérateur du calcul [" + ",  - ,  * ,  / ]: ")
if operation not in ["+", "-", "*", "/"]:
    print("Erreur simbole incorrect, saisissez le simbole spécifié !")
    raise SystemExit("Fin du programme.")
# calculer les nombres saisis
resultat = 0  # initialisation d'une variable résultat pour notre opération
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # vérification de la nullété du nombre2 puisse que en division il est impossible de diviser par zéro
    if nombre2 == 0:
        print("Erreur impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")

    resultat = round(nombre1 / nombre2, 2)

print(f"le résultats de l'opération donne : {resultat}")
