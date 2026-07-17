# exercice moyenne:
# création du dictionnaire
club_rank = {"Marie": 1, "Bernard": 4, "François": 2, "Thomas": 12, "Hila": 15}
# création d'une variable initialisée à 0 pour contenir les valeurs à additionner
sum_rank = 0
# création d'une boucle for pour additionner les valeurs
for value in club_rank.values():
    sum_rank += value
# afficher la valeur de la variable
print(sum_rank)
# diviser par le nombre de valeur pour avoir la moyenne
average_rank = sum_rank / len(club_rank)
# afficher la moyenne
print("Les membres du club sportif ont un rang moyen de : " + str(average_rank))
