import tkinter as tk            
from random import randint
from time import time






largeur_alien=22      
hauteur_alien=16
ecart_alien=10
hauteur_alien_ligne1=50
nbre_alien_par_ligne=15
descente_alien=10
VitesseDeplacement=10
VitesseAlien=0.5
AccelerationAlien=0.05
class Alien:
    
    Compteur=0
    def __init__(self):
        Alien.Compteur += 1
        self.Compteur=Alien.Compteur
        self.vivant=True
        self.x=self.Compteur*(ecart_alien+largeur_alien)
        Alien.y=hauteur_alien_ligne1
        Alien.dir=1
        Alien.vitesse=VitesseAlien

    def Creation(self):
        #self.apparence=canevas.create_rectangle(self.x-largeur_alien/2,Alien.y-hauteur_alien/2,self.x+largeur_alien/2,Alien.y+hauteur_alien/2,width=2,outline='white')
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImageAlien)

    def Affichage(self):
        #canevas.coords(self.apparence , self.x-largeur_alien/2 ,Alien.y-hauteur_alien/2 , self.x+largeur_alien/2 ,Alien.y+hauteur_alien/2)
        canevas.coords(self.apparence,self.x,self.y)

    def mouvement_alien(self):
    
        if self.dx == abs(self.dx) :
            if self.X2 >= self.WIDTH:
                self.dx = -10
                self.y = self.y+10
                self.dy = self.dy+10
        if self.dx == -abs(self.dx) :
            if self.X1 <= 0:
                self.dx = 10
                self.y = self.y+10
                self.dy = self.dy+10

        self.X1=self.X1+self.dx
        self.X2=self.X2+self.dx
        self.Canevas.coords(self.alien,self.X1,self.y,self.X2,self.dy)
        self.w.after(100,self.mouvement_alien)
