
# comment entrer chaque nouvelle entrée utilisateur dans le dictionnaire ? Boucle "while" ?
# création d'un dictionnaire vide ?
user_dict = {}
# création d'une variable "user_name"
user_name = input("Quel est votre nom d'utilisateur ? ")
# création d'une variable "user_score" 
user_score = input("Quel est votre score ? ")
# stocker les deux input dans le dictionnaire
user_dict[user_name] = user_score
print(user_dict)

while user_name != "null" and user_score != "null":
    user_name = input("Quel est votre nom d'utilisateur ? ")
    user_score = input("Quel est votre score ? ")
    user_dict[user_name] = user_score
    print(user_dict)