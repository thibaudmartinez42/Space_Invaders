from player import *
from alien import *

import tkinter as tk            
from random import randint
from time import time
from tkinter import *

hauteur=480
largeur=640
largeur_alien=22      
hauteur_alien=16
ecart_alien=10
hauteur_alien_ligne1=50
nbre_alien_par_ligne=15
descente_alien=10
VitesseDeplacement=10
VitesseAlien=0.5
AccelerationAlien=0.05
largeur_vaisseau=30
hauteur_vaisseau=32
posX=largeur/2
posY=hauteur-hauteur_vaisseau-5
VitesseTir= 1
tps_entre_tir_alien=50
TempsTir=0
TirsAlien=[]
largeur_protections=1.5*largeur_vaisseau

class Tir:
    
    Compteur=0
    def __init__(self):
        self.x=vaisseau.x
        self.y=vaisseau.y
        self.apparence=Canvas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='white')
        self.encours=True
        Tir.Compteur+=1
    
    def Affichage(self):
        Canvas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
    
    def Deplacement(self):
        if self.encours:
            self.y-=VitesseTir
            self.Affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)