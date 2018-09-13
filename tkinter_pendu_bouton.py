from tkinter import *
import tkinter as tk

fenetre = Tk()

m1 = PanedWindow(orient=VERTICAL)
m1.pack(fill=BOTH, expand=1)

panneauBoutonAlphabet = PanedWindow(m1, orient=HORIZONTAL)
m1.add(panneauBoutonAlphabet)


#######################Variables########################################

lettre = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
			'P','Q','R','S','T','U','V','W','X','Y','Z']
			
########################################################################



for j in range(26):
	b = Button(panneauBoutonAlphabet, text="{}".format(lettre[j]), command= lambda y=lettre[j]: print("{}".format(y)))
	panneauBoutonAlphabet.add(b)

########################################################################
def mort_bonhomme():
	bras_tg = canvas.coords(bras_g, 350, 350, 375, 300)
	bras_td = canvas.coords(bras_d, 400, 350, 375, 300)
	jambe_tg = canvas.coords(jambe_g, 360, 430, 375, 350)
	jambe_td = canvas.coords(jambe_d, 390, 430, 375, 350)
	tabouret1 = canvas.delete(tabouret_base, tabouret_g, tabouret_d)



bouton_dead=Button(m1, text="DEAD", command=mort_bonhomme)			

m1.add(bouton_dead)


########################################################################


fenetre.mainloop()
