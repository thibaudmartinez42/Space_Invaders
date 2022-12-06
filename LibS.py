
from tkinter import *

Mafenetre=Tk()
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
BoutonQuitter= Button(Mafenetre, text='quitter',command=Mafenetre.destroy)
BoutonQuitter.pack(side='right', padx=5, pady=5)
Canevas = Canvas(Mafenetre, width=700, height=900, bg='blue')
Canevas.pack(padx=5,pady=5)
x=10
dx=40
alien=Canevas.create_rectangle(x,40,dx,65,fill='green')
def creer_vaisseau():
    Canevas.create_rectangle(450,800,250,700,fill='black')
def Envoyer_Proj():
    Canevas.create_oval(345,695,355,685,fill='yellow')
def creer_alien(x,y,dx,dy):
    Canevas.create_rectangle(x,y,dx,dy,fill='green')
def mouvement_alien():
    global x, dx
    x=x+10
    dx=dx+10
    y=40
    dy=65
    Canevas.coords(alien,x,y,dx,dy)
    Mafenetre.after(1000,mouvement_alien)
def jouer():
    creer_vaisseau()
    Mafenetre.after(1000,mouvement_alien)
    Mafenetre.mainloop()
    ingame = True,
    while ingame == True :
        touche =Event.keysym
        if touche == 'Backspace' :
                Envoyer_Proj()


