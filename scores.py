# créer un dictionnaire "scores"
scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}
# créer une variable "pseudo" avec input utilisateur
pseudo = input("Quel est votre pseudo ? ")
# créer une variable "score" avec input utilisateur
score = int(input("Quel est votre score ? "))
# faire rentrer les deux input dans le dictionnaire : dict["clé"] = valeur
scores[pseudo] = score
# afficher le score de "Elocin03" ainsi que le score du nouveau pseudo entré
print(scores["Elocin03"], scores[pseudo])

# pour aller plus loin, j'aimerais trouver un moyen de trier:
# par clé
for pseudo in sorted(scores):
    print(pseudo)
# par valeur
for value in sorted(scores.values()):
    print(str(value))
# afficher tout (clé + valeur)
for key, value in scores.items():
    print (key + " : " + str(value))
# trier l'ensemble par clé
for key, value in sorted(scores.items()):
    print (key + " : " + str(value))
# trier l'ensemble par valeur
 
# comment entrer chaque nouvelle entrée utilisateur dans le dictionnaire ? Boucle "while" ?