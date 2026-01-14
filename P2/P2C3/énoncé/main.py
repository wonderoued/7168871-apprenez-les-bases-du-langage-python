# Ecrivez votre code ici


def salaire_mensuel(salaire_annuel):
    """cette fonction calcule le salaire mensuel, elle reçoit en paramètre le salaire annuel et est divisé par 12 et retourne le salaire mensuel
    :params:
    :salaire_annuel (float): le salaire annuel
    :returns:
    :salaire_mensuel (float)
    """

    return salaire_annuel / 12


def salaire_hebdomadaire(salaire_mensuel):
    """Cette fonction calcule le salaire hebdomadaire, elle reçoit en paramètre le salaire mensuel et est divisé par 4 et retourne le salaire hebdomadaire
    :params:
    :salaire_mensuel (float): le salaire mensuel
    :returns:
    :salaire_hebdomadaire (float)
    """

    return salaire_mensuel / 4


def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    """cette fonction calcule le salaire par heure, elle reçoit en paramètre le salaire hebdomadaire et heures_travailles; et retourne le salaire horaire en divisant salaire_hebdomadaire par heures_travaillees
    :param:
    :salaire_hebdomadaire (float): le salaire hebdomadaire
    :heures_travaillees (int): nombre d'heures de travail
    :returns:
    :salaire_horaire (float)
    """

    return salaire_hebdomadaire / heures_travaillees


salaire_annuels = float(input("saisissez votre salaire annuel ici : "))
nombre_heure_par_semaine = float(
    input("saisissez le nombre d'heures de travail par semaine ici : ")
)
mensuel = salaire_mensuel(salaire_annuels)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, nombre_heure_par_semaine)
print(f"votre salaire hebdomadaire est {round(horaire, 2)} euros.")
