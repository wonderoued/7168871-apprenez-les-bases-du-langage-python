# Ecrivez votre code ici !

nombres = input(
    "saisissez une liste de nombres ici (séparés par des virgules): "
)  # récuperé la liste de nombre de l'utilisateur sous forme de string
liste = nombres.split(
    ","
)  # convertir la liste de nombre en string en liste de nombre type type list string
print("liste de nombres :", liste)  # afficher la liste de nombre.

liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)
print("liste_entiers :", liste_entiers)

somme = 0
for nombre in liste_entiers:
    somme += nombre
print("la somme de la liste_entier =", somme)

moyenne = somme / len(liste_entiers)
print("la moyenne de la liste_entier =", moyenne)


nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("les nombres > à la moyenne :", nombre_au_dessus_moyenne)

nombre_paires = 0
for nombre in liste_entiers:
    if nombre % 2 == 0:
        nombre_paires += 1
print("nombre de nombre_paires :", nombre_paires)
