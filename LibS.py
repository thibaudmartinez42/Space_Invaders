
from tkinter import *
WIDTH = 700
HEIGHT = 900
Nb_Alien = 15
vie = 3


class BehaviorMng:
    
    X1=10
    X2 =20
    y=40
    dy=65
    dx=10    
    
    def __init__(self,w) :
        
        self.w=w
        self.init_visual()
    
    def init_visual(self):
        global Canevas
        Canevas = Canvas(self.w, width=WIDTH, height=HEIGHT, bg='blue')
        Canevas.pack(padx=5,pady=5)
        Canevas.pack(padx=5,pady=5)
        Canevas.focus_set()
        Canevas.bind('<Key>',Vaisseau.creer_Proj)


    

class Vaisseau :
    
    def __init__(self,w):
        self.w = w
        self.x1 = 450
        self.x2 = 250
        self.y1 = 800
        self.y2 = 700
    def creer_vaisseau(self):
        Canevas.create_rectangle(self.x1,self.y1,self.x2,self.y1,fill='black')
    def creer_Proj(self,event):
        self.coord_proj_x = (self.x1 + self.x2)/2
        self.coord_proj_y =685
        self.proj = Canevas.create_oval(self.coord_proj_x - 5,self.coord_proj_y + 10 ,self.coord_proj_x + 5,self.coord_proj_y,fill='yellow')
        self.w.after(50,self.mvt_proj)
    def mvt_proj(self):
        Canevas.move(self.proj,0,-10)
        coord_proj = Canevas.coords(self.proj)
        enemie = Canevas.find_overlapping(*coord_proj)
        if self.coord_proj_y <= 0 :
            Canevas.delete(self.proj)
        elif  enemie == '' :
            self.w.after(50,self.mvt_proj)
        else :
            Canevas.delete(enemie)
class aliens :
    def __init__(self,w):
        self.w =w
        self.x1 = 10
        self.x2 = 30
        self.y1 = 40
        self.y2 = 65
        self.dx = 10
        self.dy = 65
        Coord_Aliens = []

    def creer_alien(self):
        for i in Nb_Alien :
            Canevas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill='green')
            i += 1
    def mouvement_alien(self):
    
        if self.dx == abs(self.dx) :
            if self.x2 >= WIDTH:
                self.dx = -10
                self.y1 = self.y1+10
                self.y2 = self.y2+10
        if self.dx == -abs(self.dx) :
            if self.x1 <= 0:
                self.dx = 10
                self.y1 = self.y1+10
                self.y2 = self.y2+10

        self.X1=self.X1+self.dx
        self.X2=self.X2+self.dx
        Canevas.coords(self.alien,self.X1,self.y1,self.X2,self.y2)
        self.w.after(100,self.mouvement_alien)
        










Mafenetre=Tk()
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
b_mng=BehaviorMng(Mafenetre)



                    

def jouer():
    global b_mng
    
    Vaisseau.creer_vaisseau()
    aliens.creer_alien()
    Mafenetre.after(1000,b_mng.mouvement_alien)
    Mafenetre.mainloop()
    ingame = True,
    while ingame == True :
        touche =Event.keysym
        if touche == 'Backspace' :
                Vaisseau.creer_Proj()

        




BoutonQuitter= Button(Mafenetre, text='quitter',command=Mafenetre.destroy)
BoutonQuitter.pack(side='right', padx=5, pady=5)
BoutonRecommencer= Button(Mafenetre, text='Recommencer',command=jouer)
BoutonRecommencer.pack(side='right', padx=5, pady=5)
