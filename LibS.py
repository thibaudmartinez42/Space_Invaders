
from tkinter import *

Mafenetre=Tk()
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
Canevas = Canvas(Mafenetre, width=700, height=900, bg='blue')

def creer_vaisseau():
    Canevas.create_rectangle(450,800,250,700,fill='black')
def Envoyer_Proj(event):
    Canevas.create_oval(345,695,355,685,fill='yellow')
Mafenetre.mainloop()
def game_Over():
    
def jouer():
    creer_vaisseau()
    
                


BoutonQuitter= Button(Mafenetre, text='quitter',command=Mafenetre.destroy)
BoutonQuitter.pack(side='right', padx=5, pady=5)
BoutonRecommencer= Button(Mafenetre, text='Recommencer',command=jouer)
BoutonRecommencer.pack(side='right', padx=5, pady=5)

Canevas.pack(padx=5,pady=5)
Canevas.focus_set()
Canevas.bind('<Key>',Envoyer_Proj)
