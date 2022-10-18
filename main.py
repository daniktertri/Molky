import random #import de la bibliotheque random pour avoir 
joueurs_point = {} #dictionaire avec le prenom des joueurs et leurs nombre de points
liste_joueurs = [] #Cette liste de joueurs est nececaire seulement pour la premiere manche
gagnant = 0 # nombre de gagnants varie de 0 a 1 -->est la pour arreter le cycle while)
def debut(): 
    '''
    entree: aucune 
    sortie: aucune
    variables: 
       nombre_de_joueurs -- int
       temporaire -- str
       liste_joueurs -- list
       joueur_point -- dictionaire
    methode: demander le nombre de joueurs,les prenoms des joueurs et les range dans la liste et dans le dictionaire+ leur attribuer 0 points qui sont les points de base.
    '''
    print('Bienvenue au jeux du Molky.\nCe programme est fait pour gerer vos points :)')
    nombre_de_joueurs = int(input("Combiens etes vous a jouer?\n"))
    if nombre_de_joueurs <2: 
        print(f'Vous devez etre minimum 2 joueurs!')
        debut()
    else:
        for i in range(nombre_de_joueurs):
            temporaire = input(f'Entrez le prenom du {i+1} joueur:\n')
            liste_joueurs.append(temporaire)
            joueurs_point[temporaire] = 0
def premiere_manche():
    '''
    entree: aucune 
    sortie: aucune
    variables: 
             points_temporaire --
    methode: Pendant la premiere manche les joueurs sont mis dans un ordre au hasard.Puis l'on demande les points pour chaque joueurs et on verifie si les points sont bon. 
    '''
    random.shuffle(liste_joueurs)
    for p in range(len(liste_joueurs)):
        print(f'{liste_joueurs[p]} a vous de jouer!')
        point_temporaire = int(input(f'Entrez votre nombre de point:\n'))
        verification_points(point_temporaire,liste_joueurs[p])
def verification_points(points,prenom_joueur):
    """
    entree: points (int) -- nombre de points , prenom_joueur (str) -- prenom du joueurs.
    sortie: aucune
    variables: 
          joueurs_points : dictionaire
    methode: verifie que les points ne depasse pas 12 et ne sont pas inferieur a 0.
    """    
    if points <0 or points > 12:
        print(f'Erreur {prenom_joueur},recomencez vous ne pouvez pas avoir plus de 12 points et moins de 0 points.')
        redemander_score(prenom_joueur)
    else:
        joueurs_point[prenom_joueur] += points
        verification_scores()
def redemander_score(njoueur):
    '''
    entree: prenom du joueur : str
    sortie: aucune
    variables:   
         point_temporaire : int - variable temporaire pour les points 
    methode: 
    '''
    print(f'{njoueur} a vous de jouer!')
    point_temporaire = int(input(f'Entrez votre nombre de point:\n'))
    verification_points(point_temporaire,njoueur)

def reclasser_les_joueurs():
    '''
    entree: aucune 
    sortie: aucune
    variables:
            valeur_classe: list --  liste avec le nombre de point de chaque personne classer par ordre croissant
            reclasse_dict: dictionaire -- dictoinaire reclasse
    methode: reclasse les joueurs en fonction croissante de leurs points) -- elle trouve le joueur avec ses points puis le reclasse en fonction de la liste qui donne l'exemple.
    '''
    global joueurs_point
    valeur_classe = sorted(joueurs_point.values()) # liste avec seulement les points de joueur
    reclasse_dict = {} #dictionaire vide dans lequel va etre l'ordre des joueurs reclasse dans l'ordre croissant de leurs points
    for i in valeur_classe:
        for k in joueurs_point.keys():
            if joueurs_point[k] == i:
                reclasse_dict[k] = joueurs_point[k]
    joueurs_point = reclasse_dict #on ajoute les valeurs du dictionaire reclasse au principale :)

def fonction_principale():
    '''
    entree: aucune 
    sortie: aucune
    variables: 
              joueurs_points : dictionaire
    methode: Demande les points aux joueurs.
    '''
    for njoueur in joueurs_point:
        print(f'{njoueur} a vous de jouer!')
        point_temporaire = int(input(f'Entrez votre nombre de point:\n'))
        verification_points(point_temporaire,njoueur)
        verification_scores()

def fin_de_manche():
    '''
    entree: aucune 
    sortie: aucune
    variables: 
        joueurs_point : dictionaire
    methode: renvoie les points de chaque joueurs a la fin de chaque manche.
    '''    
    for njoueur, npoint in joueurs_point.items():
        print(f'{njoueur} a {npoint} points')

def gagnant_(legagnant):
    """
    entree: le prenom du gagnant
    sortie: aucune
    variables:
        gagnant : int
        legagnant: str
    methode: envoie un message avec le prenom du gagnant.
    """    
    global gagnant
    print(f'{legagnant} a gagne!!')
    print("Les scores finaux sont:")
    fin_de_manche()
    gagnant = 1
    exit()

def verification_scores():
    '''
    entree: aucune 
    sortie: aucune
    variables: 
         joueurs_points : dictionaire
    methode: verifie que le score est superieur a 50 ou egale a 50.Si le score est superieur remet les points a 25 si egale a 50 -- le joueur a gagne appelle la fonction "gagnant_"
    '''
    for njoueur, npoint in joueurs_point. items():
        if npoint > 50:
            print(f'{njoueur} est revenu a 25 points car il a depasse les 50 points')
            joueurs_point[njoueur] = 25
        if npoint == 50:
            gagnant_(njoueur)
            break
debut()
premiere_manche()
reclasser_les_joueurs()
fin_de_manche()
while gagnant == 0:   #cycle principale while lance les fonction tant qu'il n'y a pas de gagnant)
    reclasser_les_joueurs()#au debut on reclasse les joueurs en fonction de leurs points
    fonction_principale()# on demande au joueurs le nombre de points qu'ils ont marque de plus. 
    verification_scores()#On verifie si il y a un gagant.
    fin_de_manche()#On donne les resultat de la fin de manche.