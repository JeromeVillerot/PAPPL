# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:05:53 2020

@author: Jérôme VILLEROT
"""
"""
Cette fonction 
"""
from InitialiseInfini import initialiseInfini

def actualise(position_joueur,positionIA,valeur_noeud,valeur_branche):
    estAvecIA = (initialiseInfini(position_joueur,positionIA) == 0)
    if (estAvecIA):
        return (max(valeur_noeud, valeur_branche))
    else:
        return (min(valeur_noeud, valeur_branche))
        
