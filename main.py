import random #import de la bibliotheque random pour avoir 
joueurs_point = {} #dictionaire avec le prenom des joueurs et leurs nombre de points
liste_joueurs = [] #Cette liste de joueurs est nececaire seulement pour la premiere manche
gagnant = 0 # nombre de gagnants varie de 0 a 1 -->est la pour arreter le cycle while)
def debut(): 
    '''
    entree: aucune 
    sortie: aucune
    variables: 
    methode: demander le nombre de joueurs,les prenoms des joueurs et les range dans la liste et dans le dictionaire+ leur attribuer 0 points qui sont les points de base.
    '''
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
    methode: 
    '''
    random.shuffle(liste_joueurs)
    for p in range(len(liste_joueurs)):
        print(f'{liste_joueurs[p]} a vous de jouer!')
        point_temporaire = int(input(f'Entrez votre nombre de point:\n'))
        verification_points(point_temporaire,liste_joueurs[p])

def verification_points(points,numero_joueur):
        if points <0 or points > 12:
            print(f'Erreur {numero_joueur},recomencez vous ne pouvez pas avoir plus de 12 points et moins de 0 points.')
            redemander_score(numero_joueur)
        else:
            joueurs_point[numero_joueur] += points
            verification_scores()

def redemander_score(njoueur):
    '''
    entree: prenom du joueur (str)
    sortie: aucune
    variables: point_temporaire
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
    methode: 
    '''
    global joueurs_point
    valeur_classe = sorted(joueurs_point.values()) # liste avec seulement les points de joueur
    reclasse_dict = {} #dictionaire vide dans lequel va etre l'ordre des joueurs reclasse dans l'ordre croissant de leurs points
    for i in valeur_classe:
        for k in joueurs_point.keys():
            if joueurs_point[k] == i:
                reclasse_dict[k] = joueurs_point[k]
    joueurs_point = reclasse_dict

def fonction_principale():
    '''
    entree: aucune 
    sortie: aucune
    variables: 
    methode: 
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
    methode: 
    '''    
    for njoueur, npoint in joueurs_point.items():
        print(f'{njoueur} a {npoint} points')

def gagnant_(legagnant):
    global gagnant
    print(f'{legagnant} a gagne!!')
    print(f'Les scores finaux sont:')
    #fin_de_manche()
    gagnant = 1

def verification_scores():
    '''
    entree: aucune 
    sortie: aucune
    variables: 
    methode: 
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
while True:   #cycle principale while qui fait lance les fonctions dans le bonne ordre.
    if gagnant<1:
        reclasser_les_joueurs()
        fonction_principale()
        fin_de_manche()
        verification_scores()
    else: 
        break 