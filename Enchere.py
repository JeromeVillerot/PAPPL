# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:57:10 2019

@author: telmar
"""

def Enchere(jeu1, jeu2, jeu3, jeu4, carte):
    """Renvoie une liste avec le joueur qui a pris (entre 0 et 3) et la couleur de l'atout, ou avec un unique élément "On redistribue"."""
    prise = EncherePremierTour(jeu1, jeu2, jeu3, jeu4, carte)
    if prise[0] != "Personne n'a pris":
        return [prise[0], prise[1]]
    else:
        prise = EnchereDeuxiemeTour(jeu1, jeu2, jeu3, jeu4, carte)
        if prise[0] != "Personne n'a pris":
            return [prise[0], prise[1]]
        else:
            return ["On redistribue"]
