
from tkinter import *
import time

class BehaviorMng:
    WIDTH = 700
    HEIGHT = 900
    X1=10
    X2 =20
    y=40
    dy=65
    dx=10    
    
    def __init__(self,w) :
        self.w=w
        self.init_visual()
    
    def init_visual(self):
        self.Canevas = Canvas(self.w, width=self.WIDTH, height=self.HEIGHT, bg='blue')
        self.Canevas.pack(padx=5,pady=5)
        self.alien=self.Canevas.create_rectangle(self.X1,40,self.X2,65,fill='green')
        self.Canevas.pack(padx=5,pady=5)
        self.Canevas.focus_set()
        self.Canevas.bind('<Key>',self.Envoyer_Proj)


    
    def creer_vaisseau(self):
        self.Canevas.create_rectangle(450,800,250,700,fill='black')
    def creer_Proj(self,event):
        self.proj = self.Canevas.create_oval(345,695,355,685,fill='yellow')
        self.Envoyer_Proj(self)
    def Envoyer_Proj(self):
        y = self.Canevas.coords(self.proj)
        y[1]= y[3]
        y[3] =y[1]+10
        self.Canevas.coords(self.proj,y[0],y[1],y[2],y[3])
        self.w.after(100, self.Envoyer_Proj)


            
    def creer_alien(self):
        self.Canevas.create_rectangle(self.X1,self.y,self.X2,self.dy,fill='green')
    
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


Mafenetre=Tk()
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
b_mng=BehaviorMng(Mafenetre)



                    

def jouer():
    global b_mng
    b_mng.creer_vaisseau()
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

