class Aventurier:
	"L'aventurier doit voler le trésor du donjon"
def __init__(self):
        self.chemin = 0
		self.inventaire = inventaire = ['fouet','Torche','Fossil','Sac']
	def get_chemin(self):
        return self.chemin
	def get_inventaire(self):
        return self.inventaire
	def affiche_inventaire(self):
		for x in self.inventaire
		linventaire = linventaire + "- " + x +"\n"
		return linventaire
		
#---------------------------------------------------------------------------------------------------
		
class Donjon:
	"Le donjon doit empècher l'aventurier de voler son trésor"
	def __init__(self):
	self.salles = salles = ["La mare pleinne de lamproie","La chausse trappe","Le saut de liannes mal accrocher","Un chemin avec du gaz imflamable","Le plafons a pic","Le couloir a tir de carabine","Des insects empoisonés","Les flaque d'acides"]
	self.cheminpiege = 0
#---------------------------------------------------------------------------------------------------	
	
print ("Bienvenu")
text = input("Connaissé vous les règles de ce jeu ?\n")
if text == "non":
    print ("Alors il est temps de vous les expliqué !")
elif text == "oui":
    print ("tant mieux")
    
text = input("Etes vous l'aventurier ?\n")

#while text != "oui" or text != "non":
#    print ("je n'ai pas compris")
#   text = input("Etes vous l'aventurier ?\n")
#    if text == "oui" or text == "non":
#        break

if text == "non":
    joueur = 1
    print ("Alors c'est vous le fameux donjon maléfique !")
elif text == "oui":
    joueur = 2
    print ("Alors c'est vous le fameux aventurier alors prennez place a l'orée du donjon !")

print ("Bien commençon\n\nLe donjon commence !\n")

###########################################
#donjon
if joueur == 1:
    print ("Un aventurier ce présente a votre porte il a définitevement \nl'intention de s'introduire et de dérober vos trésors\n")
    print ("Vous avez 3 salles pour éliminer ce géneur\n")
    print ("La première salle possède 3 chemin :\n- une marre rempli de lamproie assoiffé !\n")
    print ("- Une chausse trape qui tombe a pic litéralement !\n")
    print ("- Un gaz inflamable !\n\n\n")
    piege = [0]
    i = 0
    while text != "aucune":

        text = input("Choissez les chemins a armé !\n")

        if text == "aucun":
            print("étonant !\n")
        elif text == "finis":
            print("La mise en place est finis\n")
            break
        elif text == "La marre" or "le premier":
            print("- Il mourra s'il n'utilise pas sa nouriture dans le sac\n")
            piege[i] = 1
            i=i+1
        elif text == "La chausse trape" or "le deuxième":
            print("- Il mourra s'il n'utilise pas son fouet\n")
            piege[i] = 2
            i=i+1
        elif text == "Le gaz" or "le troisième":
            print("- Il mourra s'il n'utilise pas sa torche\n")
            piege[i] = 3
            i=i+1

    print ("Maintenant c'est le tour de l'aventurier")
    joueur == 2
else:
    print ("Vous êtes munie d'outils pour prendre le donjon d'assaut \n")
    print("- un fouet\n")
    print("- une torche\n")
    print("- un fossile\n")
    print("- un sac\n\n")
    print("Ces objet ne sont utilisable qu'une fois pour survivre !")
	
text = input("Vous pouvez choisire d'utiliser un objet pour vous accordé un passage sans emcombre !\n")

    #print ("Toujours pas mort le pilleur a utilisé XXX pour survivre")
    #print ("La seconde possède une marre rempli de lamproie assoiffé !\n")
##########
    #print ("La troisième possède une marre rempli de lamproie assoiffé !\n")
##########

##########
    #print ("le projet prend de l'essort")
##########
