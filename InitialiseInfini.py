# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:54:07 2020

@author: Jérôme VILLEROT
"""
"""
Cette fonction permet d'initialiser la valeur du noeud. 
Si le joueur est avec l'IA, cette valeur est initialisée à -inf car on va maximiser le score
Si le joueur n'est pas avec l'IA, cette valeur est initialisée à +inf car on va minimiser le score
"""

def initialiseInfini(numero_joueur,positionIA):
    if ((((positionIA - numero_joueur)%4)%2) == 0):
        return (str('-inf'))
    else:
        return (str('inf'))
