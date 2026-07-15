# exercice inventory:
inventory = {"potion": 1, "scroll": 2, "holy sword": 0}
for key in inventory :
    print(key)

inventory = {"potion": 1, "scroll": 2, "holy sword": 0}
for value in inventory.values() :
    print(value)

inventory = {"potion": 1, "scroll": 2, "holy sword": 0}
for key, value in inventory.items() :
    print (key + " : " + str(value))

# exercice scores:
scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}
pseudo = input("Quel est votre pseudo ? ")
score = input("Quel est votre score ? ")
scores[pseudo] = score
for key, value in scores.items() :
    print (key + " : " + str(value))

# exercice moyenne:
# création du dictionnaire
rank = {"Marie": 1, "Bernard": 4, "François": 2, "Thomas": 12, "Hila": 15}
# création d'une variable initialisée à 0 pour contenir les valeurs à addictionner
middle_rank = 0
# création d'une boucle for pour additionner les valeurs
for value in rank.values():
    middle_rank += value
# afficher la valeur de la variable
print(middle_rank)
# diviser par le nombre de valeur pour avoir la moyenne
middle_rank /= 5
# afficher la moyenne
print("Les membres du club sportif ont un rang moyen de : " + float(middle_rank))

