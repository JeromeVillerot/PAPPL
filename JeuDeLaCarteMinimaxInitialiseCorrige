# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:43:51 2020

@author: Jérôme VILLEROT
"""

from CartesJouables import cartesJouables
from CompareCarteJeu import compareCarteJeu
from JeuDeLaCarteMinimaxCorrige import jeuDeLaCarteMinimaxCorrige
from InitialiseInfini import initialiseInfini
from Actualise import actualise

"""
Cette fonction va traiter le premier tour où l'IA doit choisir la carte qu'il doit jouer. 
paramètre:
    @jeu1, jeu2, jeu3, jeu4 = jeux des 4 joueurs (dans l'ordre où ils vont jouer ce tour!) ce sont des listes de cartes
    @couleur_atout = couleur de l'atout de cette manche, c'est un string
    @cartes_pli = liste des cartes du pli en cours
    @ difficulte = entier qui définie la difficulté de l'IA
    @ belote, rebelote = prend les valeurs entre 0 et 4 suivant qu'une belote ou une rebelote ait été dite ou non
    @ plis_equipe1 = liste des plis de l'equipe 1 depuis le debut de la manche(un plis etant une liste de 4 cartes) jeu1 et jeu3 sont les joueurs de cette equipe
    @plis_equipe2 = liste des plis de l'equipe 2 depuis le debut de la manche(un plis etant une liste de 4 cartes) jeu2 et jeu3 sont les joueurs de cette equipe
    @ num_pli = entier entre 0 et 8 correspondant au numero du pli de la manche qui a été terminé (à 8 la manche est finis)
    @ positionIA= entier entre 0 et 3 qui correspond à la postion de l'IA dans ce tour
    @poids= liste des poids pour l'IA
    @premiere_carte = indice de la carte que doit jouer l'IA durant ce tour (tout les possibilités seront testées) c'est un entier.
    @carte_meneuse = carte qui mene ce tour
    @meneur= entier entre 0 et 3 qui donne la position du meneur de ce tour
    @preneur= entier entre 0 et 3 qui correspond au joueur qui a pris l'atout à cette manche

"""

def jeuDeLaCarteMinimaxInitialise(jeu1,jeu2,jeu3,jeu4,couleur_atout, cartes_pli,difficulte,belote,rebelote,plis_equipe1,plis_equipe2,num_pli,positionIA,poid,premiere_carte,carte_meneuse,meneur,preneur):
    
    if len(cartes_pli)==0:
        cartes_possibles=cartesJouables(jeu1, cartes_pli, couleur_atout, carte_meneuse)
        cartes_pli.append(cartes_possibles[premiere_carte])
        carte_meneuse1=cartes_pli[-1]
        gagnant1=1  
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==4:
            belote1=0
        else :
            belote1=belote
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==0:
            rebelote1 = 0
        else:
            rebelote1 = rebelote
        v1 = initialiseInfini(1,positionIA)#fonction qui renvoie -inf si le 2eme joueur est avec l'IA, +inf sinon
        for carte2 in cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse1):
            cartes_pli.append(carte2)
            if compareCarteJeu(carte_meneuse1, cartes_pli[-1], couleur_atout)==-1:
                carte_meneuse2=cartes_pli[-1]
                gagnant2=2
            else :
                carte_meneuse2=carte_meneuse1
                gagnant2=gagnant1   
            if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote1==4:
                belote2=1
            else :
                belote2=belote1
            if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote1==1:
                rebelote2 = 1
            else:
                rebelote2 = rebelote1
            v2 = initialiseInfini(2,positionIA)#fonction qui renvoie -inf si le 3eme joueur est avec l'IA, +inf sinon
            for carte3 in cartesJouables(jeu3, cartes_pli, couleur_atout, carte_meneuse2):
                cartes_pli.append(carte3)
                if compareCarteJeu(carte_meneuse2, cartes_pli[-1], couleur_atout)==-1:
                    carte_meneuse3=cartes_pli[-1]
                    gagnant3=3
                else :
                    carte_meneuse3=carte_meneuse2
                    gagnant3=gagnant2
                if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote2==4:
                    belote3=2
                else :
                    belote3=belote2
                if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote2==2:
                    rebelote3 = 2
                else:
                    rebelote3 = rebelote2
                v3 = initialiseInfini(3,positionIA)#fonction qui renvoie -inf si le 4eme joueur est avec l'IA, +inf sinon
                for carte4 in cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3):
                    cartes_pli.append(carte4)
                    if compareCarteJeu(carte_meneuse3, cartes_pli[-1], couleur_atout)==-1:
                        carte_meneuse4=cartes_pli[-1]
                        gagnant4=4
                    else :
                        carte_meneuse4=carte_meneuse3
                        gagnant4=gagnant3  
                    j1=jeu1[:]
                    j1.remove(cartes_pli[0])
                    j2=jeu2[:]
                    j2.remove(cartes_pli[1])
                    j3=jeu3[:]
                    j3.remove(cartes_pli[2])
                    j4=jeu4[:]
                    j4.remove(cartes_pli[3])
                    if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote3==4:
                        belote4=3
                    else :
                        belote4=belote3
                    if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote3==3:
                        rebelote4 = 3
                    else:
                        rebelote4 = rebelote3
                    
                    if gagnant4==1:
                        plis_equipe1.append(cartes_pli)
                        poid=  jeuDeLaCarteMinimaxCorrige(j1,j2,j3,j3,couleur_atout, difficulte,belote4,rebelote4,plis_equipe1,plis_equipe2,num_pli+1,positionIA,poid,preneur)
                        plis_equipe1.remove(cartes_pli)
                            
                            
                    elif gagnant4==2:
                        plis_equipe2.append(cartes_pli)                        
                        poid =  jeuDeLaCarteMinimaxCorrige(j2,j3,j4,j1,couleur_atout, difficulte,(belote4+1)%4,(rebelote4+1)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+1)%4,poid,(preneur+1)%2)
                        plis_equipe2.remove(cartes_pli)                        
                        
                    elif gagnant4==3:
                        plis_equipe1.append(cartes_pli)                        
                        poid = jeuDeLaCarteMinimaxCorrige(j3,j4,j1,j2,couleur_atout, difficulte,(belote4+2)%4,(rebelote4+2)%4,plis_equipe1,plis_equipe2,num_pli+1,(positionIA+2)%4,poid,(preneur+2)%2)
                        plis_equipe1.remove(cartes_pli)   
                            
                            
                    elif gagnant4==4:
                        plis_equipe2.append(cartes_pli)                        
                        poid =  jeuDeLaCarteMinimaxCorrige(j4,j1,j2,j3,couleur_atout, difficulte,(belote4+3)%4,(rebelote4+3)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+3)%4,poid,(preneur+3)%2)
                        plis_equipe2.remove(cartes_pli)                        
                    cartes_pli.pop(-1)
                    v3 = actualise(3,positionIA,v3,poid)#on actualise le score : on choisi le plus grand ou le plus petit, en fonction de si le joueur 4 est avec l'IA ou pas
                cartes_pli.pop(-1)
                v2 = actualise(2,positionIA,v2,v3)#on actualise le score : on choisi le plus grand ou le plus petit, en fonction de si le joueur 3 est avec l'IA ou pas
            cartes_pli.pop(-1)
            v1 = actualise(1,positionIA,v1,v2)#on actualise le score : on choisi le plus grand ou le plus petit, en fonction de si le joueur 4 est avec l'IA ou pas
            valeur_noeud = v1
        cartes_pli.pop(-1)
        
    elif len(cartes_pli)==1:
        cartes_possibles=cartesJouables(jeu2, cartes_pli, couleur_atout, carte_meneuse)
        cartes_pli.append(cartes_possibles[premiere_carte])
        if compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)==-1:
            carte_meneuse2=cartes_pli[-1]
            gagnant2=2
        else :
            carte_meneuse2=carte_meneuse
            gagnant2=meneur  
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==4:
            belote2=1
        else :
            belote2=belote
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==1:
            rebelote2 = 1
        else:
            rebelote2 = rebelote
        v2 = initialiseInfini(2,positionIA)#fonction qui renvoie -inf si le 3eme joueur est avec l'IA, +inf sinon
        for carte3 in cartesJouables(jeu3, cartes_pli, couleur_atout, carte_meneuse2):
            cartes_pli.append(carte3)
            if compareCarteJeu(carte_meneuse2, cartes_pli[-1], couleur_atout)==-1:
                carte_meneuse3=cartes_pli[-1]
                gagnant3=3
            else :
                carte_meneuse3=carte_meneuse2
                gagnant3=gagnant2
            if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote2==4:
                belote3=2
            else :
                belote3=belote
            if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote2==2:
                rebelote3 = 2
            else:
                rebelote3 = rebelote2
            v3 = initialiseInfini(3,positionIA)#fonction qui renvoie -inf si le 4eme joueur est avec l'IA, +inf sinon
            for carte4 in cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3):
                cartes_pli.append(carte4)
                if compareCarteJeu(carte_meneuse3, cartes_pli[-1], couleur_atout)==-1:
                    carte_meneuse4=cartes_pli[-1]
                    gagnant4=4
                else :
                    carte_meneuse4=carte_meneuse3
                    gagnant4=gagnant3 
                j2=jeu2[:]
                j2.remove(cartes_pli[1])
                j3=jeu3[:]
                j3.remove(cartes_pli[2])
                j4=jeu4[:]
                j4.remove(cartes_pli[3])     
                if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote3==4:
                    belote4=3
                else :
                    belote4=belote3
                if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote3==3:
                    rebelote4 = 3
                else:
                    rebelote4 = rebelote3
                if gagnant4==1:
                    plis_equipe1.append(cartes_pli)                    
                    poid=  jeuDeLaCarteMinimaxCorrige(jeu1,j2,j3,j4,couleur_atout, difficulte,belote4,rebelote4,plis_equipe1,plis_equipe2,num_pli+1,positionIA,poid,preneur)
                    plis_equipe1.remove(cartes_pli)
                        
                elif gagnant4==2:
                    plis_equipe2.append(cartes_pli)                    
                    poid = jeuDeLaCarteMinimaxCorrige(j2,j3,j4,jeu1,couleur_atout, difficulte,(belote4+1)%4,(rebelote4+1)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+1)%4,poid,(preneur+1)%2)
                    plis_equipe2.remove(cartes_pli)
                    
                elif gagnant4==3:
                    plis_equipe1.append(cartes_pli)                    
                    poid = jeuDeLaCarteMinimaxCorrige(j3,j4,jeu1,j2,couleur_atout, difficulte,(belote4+2)%4,(rebelote4+2)%4,plis_equipe1,plis_equipe2,num_pli+1,(positionIA+2)%4,poid,(preneur+2)%2)
                    plis_equipe1.remove(cartes_pli)
                    
                elif gagnant4==4:
                    plis_equipe2.append(cartes_pli)                    
                    poid = jeuDeLaCarteMinimaxCorrige(j4,jeu1,j2,j3,couleur_atout, difficulte,(belote4+3)%4,(rebelote4+3)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+3)%4,poid,(preneur+3)%2)
                    plis_equipe2.remove(cartes_pli)
                cartes_pli.pop(-1)
                v3 = actualise(3,positionIA,v3,poid)#on actualise le score : on choisi le plus grand ou le plus petit, en fonction de si le joueur 4 est avec l'IA ou pas
            cartes_pli.pop(-1)
            v2 = actualise(2,positionIA,v2,v3)#on actualise le score : on choisi le plus grand ou le plus petit, en fonction de si le joueur 3 est avec l'IA ou pas
            valeur_noeud = v2
        cartes_pli.pop(-1)
        
        
    elif len(cartes_pli)==2:
        cartes_possibles=cartesJouables(jeu3, cartes_pli, couleur_atout, carte_meneuse)
        cartes_pli.append(cartes_possibles[premiere_carte])
        if compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)==-1:
            carte_meneuse3=cartes_pli[-1]
            gagnant3=3
        else :
            carte_meneuse3=carte_meneuse
            gagnant3=meneur
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==4:
            belote3=2
        else :
            belote3=belote
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==2:
            rebelote3 = 2
        else:
            rebelote3 = rebelote
        v3 = initialiseInfini(3,positionIA)#fonction qui renvoie -inf si le 4eme joueur est avec l'IA, +inf sinon
        for carte4 in cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse3):
            cartes_pli.append(carte4)
            if compareCarteJeu(carte_meneuse3, cartes_pli[-1], couleur_atout)==-1:
                carte_meneuse4=cartes_pli[-1]
                gagnant4=4
            else :
                carte_meneuse4=carte_meneuse3
                gagnant4=gagnant3  
            j3=jeu3[:]
            j3.remove(cartes_pli[2])
            j4=jeu4[:]
            j4.remove(cartes_pli[3])                
            if cartes_pli[-1][1]==couleur_atout and (cartes_pli[-1][0] in ["Dame", "Roi"]) and belote3==4:
                belote4=3
            else :
                belote4=belote3
            if cartes_pli[-1][1]==couleur_atout and (cartes_pli[-1][0] in ["Dame", "Roi"]) and belote3==3:
                rebelote4 = 3
            else:
                rebelote4 = rebelote3                
            if gagnant4==1:
                plis_equipe1.append(cartes_pli)
                poid= jeuDeLaCarteMinimaxCorrige(jeu1,jeu2,j3,j4,couleur_atout, difficulte,belote4,rebelote4,plis_equipe1,plis_equipe2,num_pli+1,positionIA,poid,preneur)
                plis_equipe1.remove(cartes_pli)
                
            elif gagnant4==2:
                plis_equipe2.append(cartes_pli)
                poid = jeuDeLaCarteMinimaxCorrige(jeu2,j3,j4,jeu1,couleur_atout, difficulte,(belote4+1)%4,(rebelote4+1)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+1)%4,poid,(preneur+1)%2)
                plis_equipe2.remove(cartes_pli)
                
            elif gagnant4==3:
                plis_equipe1.append(cartes_pli)
                poid = jeuDeLaCarteMinimaxCorrige(j3,j4,jeu1,jeu2,couleur_atout, difficulte,(belote4+2)%4,(rebelote4+2)%4,plis_equipe1,plis_equipe2,num_pli+1,(positionIA+2)%4,poid,(preneur+2)%2)
                plis_equipe1.remove(cartes_pli)
                
            elif gagnant4==4:
                plis_equipe2.append(cartes_pli)
                poid = jeuDeLaCarteMinimaxCorrige(j4,jeu1,jeu2,j3,couleur_atout, difficulte,(belote4+3)%4,(rebelote4+3)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+3)%4,poid,(preneur+3)%2)
                plis_equipe2.remove(cartes_pli)
            cartes_pli.pop(-1)
            v3 = actualise(3,positionIA,v3,poid)#on actualise le score : on choisi le plus grand ou le plus petit, en fonction de si le joueur 4 est avec l'IA ou pas
            valeur_noeud = v3
        cartes_pli.pop(-1)

        
    elif len(cartes_pli)==3:
        cartes_possibles=cartesJouables(jeu4, cartes_pli, couleur_atout, carte_meneuse)
        cartes_pli.append(cartes_possibles[premiere_carte])
        if compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)==-1:
            carte_meneuse4=cartes_pli[-1]
            gagnant4=4
        else :
            carte_meneuse4=carte_meneuse
            gagnant4=meneur
        j4=jeu4[:]
        j4.remove(cartes_pli[3])            
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==4:
            belote4=3
        else :
            belote4=belote
        if cartes_pli[-1][1]==couleur_atout and cartes_pli[-1][0] in ["Dame", "Roi"] and belote==3:
            rebelote4 = 3
        else:
            rebelote4 = rebelote        
        if gagnant4==1:
            plis_equipe1.append(cartes_pli)
            poid= jeuDeLaCarteMinimaxCorrige(jeu1,jeu2,jeu3,j4,couleur_atout, difficulte,belote4,rebelote4,plis_equipe1,plis_equipe2,num_pli+1,positionIA,poid,preneur)
            plis_equipe1.remove(cartes_pli)
            
        elif gagnant4==2:
            plis_equipe2.append(cartes_pli)
            poid = jeuDeLaCarteMinimaxCorrige(jeu2,jeu3,j4,jeu1,couleur_atout, difficulte,(belote4+1)%4,(rebelote4+1)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+1)%4,poid,(preneur+1)%2)
            plis_equipe2.remove(cartes_pli)
            
        elif gagnant4==3:
            plis_equipe1.append(cartes_pli)
            poid = jeuDeLaCarteMinimaxCorrige(jeu3,j4,jeu1,jeu2,couleur_atout, difficulte,(belote4+2)%4,(rebelote4+2)%4,plis_equipe1,plis_equipe2,num_pli+1,(positionIA+2)%4,poid,(preneur+2)%2)
            plis_equipe1.remove(cartes_pli)
            
        elif gagnant4==4:
            plis_equipe2.append(cartes_pli)
            poid = jeuDeLaCarteMinimaxCorrige(j4,jeu1,jeu2,jeu3,couleur_atout, difficulte,(belote4+3)%4,(rebelote4+3)%4,plis_equipe2,plis_equipe1,num_pli+1,(positionIA+3)%4,poid,(preneur+3)%2)
            plis_equipe2.remove(cartes_pli)
        cartes_pli.pop(-1)
        valeur_noeud = poid
    return valeur_noeud
