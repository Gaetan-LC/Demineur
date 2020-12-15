#DEBUT D'UN DEMINEUR
from tkinter import *
import random, winsound, sys


#SET UP DE LA GRILLE
def grille(nb_col, nb_lignes, dim, origine):
    x1= origine
    y1= origine
    # DÃ©termine la hauteur de la grille
    y2 = y1 + (dim*nb_lignes)
    # DÃ©termine la ligne de la grille
    x2 = x1 + (dim*nb_col)
    colonne = 0
    while colonne <= nb_col:
        colonne+=1
        # CrÃ©ation de la ligne verticale
        can.create_line(x1,y1,x1,y2,width=2, fill="black") 
        # DÃ©calage de la ligne vers la droite
        x1 = x1 + dim 
    x1 = origine
    ligne = 0
    while ligne <= nb_lignes:
        ligne+=1
        # CrÃ©ation de la ligne horizontale
        can.create_line(x1,y1,x2,y1,width=2, fill="black") 
        # DÃ©calage de la ligne vers le bas
        y1 = y1 + dim 
