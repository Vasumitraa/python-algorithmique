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

# pour aller plus loin, j'aimerais trouver un moyen de: 
# trier par clé
for pseudo in sorted(scores):
    print(pseudo)
# trier par valeur
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
# création d'un dictionnaire vide :
user_dict = {}
# création d'une variable "user_name" :
user_name = input("Quel est votre nom d'utilisateur ? ")
# création d'une variable "user_score" :
user_score = input("Quel est votre score ? ")
# stocker les deux input dans le dictionnaire :
user_dict[user_name] = user_score
print(user_dict)

# faire une boucle pour que chaque entrée aille dans le dictionnaire :
while user_name != "null":
    user_name = input("Quel est votre nom d'utilisateur ? ")
    if user_name == "null":
        break
    user_score = input("Quel est votre score ? ")
    user_dict[user_name] = user_score
    print(user_dict)

if user_name == "null":
    print(f"Voici les différents joueurs enregistrés, ainsi que leurs scores : {user_dict}")