# -*- coding: utf-8 -*-
"""
Created on Fri Nov 08 14:23:04 2019

@author: telmar
"""

import random as rd

def encherePremierTourIA(jeu1, jeu2, jeu3, jeu4, carte,joueur):
    """Renvoie une liste de deux éléments avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout. Renvoie une liste d'un seul élément si personne n'a pris"""
    print("premier tour d'enchere")
    for i in range(4):
        if joueur[i][1] != "IAaleatoire" and joueur[i][1] != "IAminimax":
            print("c\'est au tour de: "+joueur[i][0])
            print('votre jeu')
            if i == 0:
                print(jeu1, "\n")
            elif i == 1:
                print(jeu2, "\n")
            elif i == 2:
                print(jeu3, "\n")
            elif i == 3:
                print(jeu4, "\n")
            print(carte)
            prise = input("Voulez-vous prendre ? (y/n)")
            
            if prise == "y": # Si quelqu'un prend, on renvoie le joueur et l'atout
                return [i, carte[1]]
        else: # Si le joueur est une IA, elle tire au hasard si elle prend ou pas
            prise = rd.randint(1,2)
            if prise == 1:
                return [i, carte[1]]
    return ["Personne n'a pris"]