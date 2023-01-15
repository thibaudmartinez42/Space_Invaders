'''
créer le 6 décembre 2022 par Jeanne Champion et Thibaud Martinez pour le projet de Cs_dev

TO DO
cheat code
soucoupe
plusieur enemy de force différente
meilleur score
plusieur niveau
augmenter vitesse des aliens


'''



from tkinter import *
import time

class BehaviorMng:
    WIDTH = 700 
    HEIGHT = 900
    X1=10
    X2 =20
    y=40
    dy=65
    dx=10    #element de taille pour diver objet tel que le canvas ou le vaiseau
    
    def __init__(self,w) :
        self.w=w
        self.init_visual()
    
    def init_visual(self): # foncion qui créer tout les élment quand on lance le jeu
        self.Canevas = Canvas(self.w, width=self.WIDTH, height=self.HEIGHT,bg='blue')
        self.Canevas.pack(padx=5,pady=5)
        self.alien=self.Canevas.create_rectangle(self.X1,40,self.X2,65,fill='green')
        self.Canevas.pack(padx=5,pady=5)
        self.Canevas.focus_set()
        self.Canevas.bind('<Key>',self.Envoyer_Proj)
        Fond=PhotoImage(file='space.gif')
        self.Canevas.create_image(0,0,anchor=NW,image=Fond)


    
    def creer_vaisseau(self): 
        self.Canevas.create_rectangle(450,800,250,700,fill='black')
        im=PhotoImage(file='spaceship.gif')
        self.Canevas.create_image(450,800,anchor='center',image=im)
    
    def ilot(self): #ilot de protection
        self.Canevas.create_rectangle(50,600,150,550,fill='red')
        self.Canevas.create_rectangle(300,600,400,550,fill='red')
        self.Canevas.create_rectangle(550,600,650,550,fill='red')



    def creer_Proj(self,event):
        self.proj = self.Canevas.create_oval(345,695,355,685,fill='yellow')
        self.Envoyer_Proj(self)
    def Envoyer_Proj(self): #envoi le projectile
        y = self.Canevas.coords(self.proj)
        y[1]= y[3]
        y[3] =y[1]+10
        self.Canevas.coords(self.proj,y[0],y[1],y[2],y[3])
        self.w.after(100, self.Envoyer_Proj)


            
    def creer_alien(self): #creer l'alien
        self.Canevas.create_rectangle(self.X1,self.y,self.X2,self.dy,fill='green')
    
    def mouvement_alien(self):
    
        if self.dx == abs(self.dx) : #bouge a droite
            if self.X2 >= self.WIDTH:
                self.dx = -10
                self.y = self.y+10
                self.dy = self.dy+10
        if self.dx == -abs(self.dx) : #bouge a gauche
            if self.X1 <= 0:
                self.dx = 10
                self.y = self.y+10
                self.dy = self.dy+10

        self.X1=self.X1+self.dx
        self.X2=self.X2+self.dx
        self.Canevas.coords(self.alien,self.X1,self.y,self.X2,self.dy)
        self.w.after(100,self.mouvement_alien) #toute les 100 ms la fonction ce relance et l'alien bouge de nouveau


Mafenetre=Tk() #créer la fenêtre de jeu
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
b_mng=BehaviorMng(Mafenetre)




                    

def jouer(): # fonction qui lance le jeux
    global b_mng
    b_mng.creer_vaisseau()
    b_mng.ilot()
    Mafenetre.after(1000,b_mng.mouvement_alien)
    Mafenetre.mainloop()
    ingame = True,
    while ingame == True :
        touche =Event.keysym
        if touche == 'Backspace' :
                b_mng.Envoyer_Proj()

        




BoutonQuitter= Button(Mafenetre, text='quitter',command=Mafenetre.destroy)
BoutonQuitter.pack(side='right', padx=5, pady=5)
BoutonRecommencer= Button(Mafenetre, text='Recommencer',command=jouer)
BoutonRecommencer.pack(side='right', padx=5, pady=5)
BoutonJeu=Button(Mafenetre,text='Jouer',command = jouer)


jouer()
