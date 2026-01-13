# Écrivez votre code ici !


fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange",
}  # création d'un dictionnaire de fruits
fruits["kiwi"] = "vert"  # ajout du fruit kiwi et sa valeur au dictionnaire fruits
couleur_banane = fruits.get("banane")  # affichage de la valeur du fruit banane
fruits["pomme"] = "vert"  # modification de la valeur du fruit pomme
del fruits["banane"]
print(f"clée restante : {fruits.keys()}")
