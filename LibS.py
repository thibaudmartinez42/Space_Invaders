
from tkinter import *
WIDTH = 700
HEIGHT = 900
Nb_Alien = 15
Canevas = Canvas(T, width=WIDTH, height=HEIGHT, bg='blue')

class BehaviorMng:
    
    X1=10
    X2 =20
    y=40
    dy=65
    dx=10    
    
    def __init__(self,T) :
        self.w=T
        self.init_visual()
    
    def init_visual(self):
        
        Canevas.pack(padx=5,pady=5)
        self.alien=self.Canevas.create_rectangle(self.X1,40,self.X2,65,fill='green')
        Canevas.pack(padx=5,pady=5)
        Canevas.focus_set()
        Canevas.bind('<Key>',self.creer_Proj)


    
    


            
    def creer_alien(self):
        Canevas.create_rectangle(self.X1,self.y,self.X2,self.dy,fill='green')
    
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

class Vaisseau :
    
    def __init__(self,T):
        self.w = T
        self.x1 = 450
        self.x2 = 250
        self.y1 = 800
        self.y2 = 700
    def creer_vaisseau(self):
        Canevas.create_rectangle(self.x1,self.y1,self.x2,self.y1,fill='black')
    def creer_Proj(self,event):
        self.coord_proj = (self.x1 + self.x2)/2
        self.coord_proj_y =685
        self.proj = Canevas.create_oval(self.coord_proj - 5,self.coord_proj_y + 10 ,self.coord_proj + 5,self.coord_proj_y,fill='yellow')
        self.w.after(50,self.mvt_proj)
    def mvt_proj(self):
        Canevas.move(self.proj,0,-10)
        if self.coord_proj_y <= 0 :
            Canevas.delete(self.proj)
        else :
            self.w.after(50,self.mvt_proj)

class aliens :
    def __init__(self):
        self.x1 = 10
        self.x2 = 30
        self.y1 = 40
        self.y2 = 65

    def creer_alien(self):
        for i in Nb_Alien
        Canevas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill='green')

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
    
    Vaisseau.creer_vaisseau()
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
jouer()
