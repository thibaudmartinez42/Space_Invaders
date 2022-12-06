
from tkinter import *

Mafenetre=Tk()
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
BoutonQuitter= Button(Mafenetre, text='quitter',command=Mafenetre.destroy)
BoutonQuitter.pack(side='right', padx=5, pady=5)
Canevas = Canvas(Mafenetre, width=700, height=900, bg='blue')
Canevas.pack(padx=5,pady=5)

def creer_vaisseau():
    Canevas.create_rectangle(450,800,250,700,fill='black')
def Envoyer_Proj():
    Canevas.create_oval(345,695,355,685,fill='yellow')
def jouer():
    creer_vaisseau()
    Mafenetre.mainloop()
    ingame = True,
    while ingame == True :
        touche =Event.keysym
        if touche == 'Backspace' :
                Envoyer_Proj()


