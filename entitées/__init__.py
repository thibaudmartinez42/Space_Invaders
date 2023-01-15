import tkinter as tk            
from random import randint
from time import time
from tir_alien import *
from protection import *
from player import *
from world import *
from alien import *
from tir_alien import *

Partie_en_cours=False
Partie_Perdu=True
ViesInit=300

#Canevas
hauteur=480
largeur=640

#vaisseau
largeur_vaisseau=30
hauteur_vaisseau=32
posX=largeur/2
posY=hauteur-hauteur_vaisseau-5

#Aliens
largeur_alien=22      
hauteur_alien=16
ecart_alien=10
hauteur_alien_ligne1=50
nbre_alien_par_ligne=15
descente_alien=10
VitesseDeplacement=10
VitesseAlien=0.5
AccelerationAlien=0.05

#Protections
nbre_protections=4
posY_protections=posY-35
largeur_protections=1.5*largeur_vaisseau
hauteur_protections=15
resistance_protections=5

#tirs allies et ennemies
VitesseTir= 1
tps_entre_tir_alien=50  #rester au dessus de 50 pour eviter de planter
Tirs=[]
TempsTir=0
TirsAlien=[]
TempsEntreTirs=1

#Score et points
Score=0
PointsAlien=30



def DelTirs():
    for i in Tirs:
        i.encours=False
    for i in TirsAlien:
        i.encours=False

def Tir_Alien():
    global ennemie,TirsAlien 
    if Partie_en_cours:
        L=[i.vivant for i in ennemie]
        i=randint(0,len(ennemie)-1)
        if L[i]:
            TirsAlien.append(TirAlien(i))
            mw.after(tps_entre_tir_alien,Tir_Alien)
        else:
            mw.after(1,Tir_Alien)



        
            
def AffichageVies(Vies):
    NbVies.config(text='Vies: '+str(Vies))
    
    
def Clavier(event):
    global TempsTir
    touche=event.keysym
    if touche=='q' or touche=='Left':
        vaisseau.deplacement(-1)
    elif touche=='d' or touche=='Right':
        vaisseau.deplacement(1)
    elif touche=='space':
        TempsTir1=time()
        if TempsTir1-TempsTir>=TempsEntreTirs or Tirs==[]:
            TempsTir=TempsTir1
            tir=Tir()
            Tirs.append(tir)
            Tirs[Tir.Compteur-1].Deplacement()

def PartieGagnee():
    global Partie_en_cours, Partie_Perdu
    gagne=True
    for i in ennemie:
        if i.vivant:
            gagne=False
    if gagne:
        canevas.grid_remove()
        winlose.config(text='Gagne')
        winlose.grid()
        canevas.delete("all")
        BoutonJouer.grid()
        BoutonJouer.config(text='Continuer')
        Alien.vitesse=VitesseAlien
        Partie_en_cours=False
        DelTirs()
        Partie_Perdu=False

def PartiePerdue():
    global Partie_en_cours, Partie_Perdu
    canevas.grid_remove()
    winlose.config(text='Perdu')
    winlose.grid()
    canevas.delete("all")
    BoutonJouer.grid()
    BoutonJouer.config(text='Rejouer')
    Alien.vitesse=VitesseAlien
    Partie_en_cours=False
    DelTirs()
    Partie_Perdu=True
    
    
def NouvellePartie():
    global ennemie, vaisseau, Partie_en_cours, Score, Vies, Defences
    canevas.grid()
    canevas.create_image(0,0,anchor='nw',image=ImageFond)
    winlose.grid_remove()
    BoutonJouer.grid_remove()
    vaisseau=Spaceship()
    Protections.Compteur=0
    Defences=[Protections() for i in range(nbre_protections)]
    Partie_en_cours=True
    if Partie_Perdu:
        Vies=ViesInit
        Score=0
        score.config(text='Score: '+str(Score))
    ennemie=[]
    AffichageVies(Vies)
    Alien.Compteur=0
    for i in range(nbre_alien_par_ligne):
        ennemie.append(Alien())
    for i in ennemie:
        i.Creation()
    MouvementAlien()
    Tir_Alien()

def Points(pts):
    global Score
    Score+=pts
    score.config(text='Score: '+str(Score))

mw=tk.Tk()

ImageVaisseau=tk.PhotoImage(file='spaceship.gif')
ImageDestroy=tk.PhotoImage(file='spaceshipdestroy.gif')
ImageAlien=tk.PhotoImage(file='invader.gif')
ImageFond=tk.PhotoImage(file='space.gif')

score=tk.Label(mw,text='Score: 0')
score.grid(row=1,column=1)

NbVies=tk.Label(mw,text="Vies: 3")
NbVies.grid(row=1,column=2)

canevas=tk.Canvas(mw,height=hauteur,width=largeur, bg='black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',Clavier)

BoutonJouer=tk.Button(mw,text='Jouer',command=NouvellePartie)
BoutonJouer.grid(row=0,column=1)



BoutonQuitter=tk.Button(mw,text='Quitter',command=mw.destroy)
BoutonQuitter.grid(row=0,column=2)

winlose=tk.Label(mw,text='Gagne')
winlose.grid(row=1,column=0)
winlose.grid_remove()

mw.mainloop()