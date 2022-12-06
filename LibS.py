
from tkinter import Tk , Label , Button, StringVar, Entry, Canvas

Mafenetre=Tk()
Mafenetre.title("Katz invader")
Mafenetre.geometry("1000x800")
BoutonQuitter= Button(Mafenetre, text='quitter',command=Mafenetre.destroy)
BoutonQuitter.pack(side='right', padx=5, pady=5)
Canevas = Canvas(Mafenetre, width=700, height=900, bg='blue')
Canevas.pack(padx=5,pady=5)
Mafenetre.mainloop()