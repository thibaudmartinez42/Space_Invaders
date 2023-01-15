import tkinter as tk            
from random import randint
from time import time
from tkinter import *






hauteur=480
largeur=640
VitesseDeplacement=10
largeur_vaisseau=30
hauteur_vaisseau=32
posX=largeur/2
posY=hauteur-hauteur_vaisseau-5
 
class Spaceship:
    
    def __init__(self):
        '''self.apparence=canevas.create_oval(posX-largeur_vaisseau/2,\
        posY-hauteur_vaisseau/2,posX+largeur_vaisseau/2,\
        posY+hauteur_vaisseau/2,width=2,outline='white')'''

        self.x=posX
        self.y=posY
        self.apparence=Canvas.create_image(self.x,self.y,anchor='center',image=ImageVaisseau)


    def deplacement(self,dir):
        if self.x>=largeur_vaisseau and dir==-1:
            self.x+=VitesseDeplacement*dir
        elif self.x<=largeur-largeur_vaisseau and dir==1:
            self.x+=VitesseDeplacement*dir
        self.Affichage()
        
    def Affichage(self):
        Canvas.coords(self.apparence,self.x,self.y)
        
        
    def ViePerdue(self):
        Canvas.itemconfig(self.apparence,image=ImageDestroy)
        mw.after(500,self.RetourApparenceNormale)
        
    def RetourApparenceNormale(self):
        Canvas.itemconfig(self.apparence,image=ImageVaisseau)

