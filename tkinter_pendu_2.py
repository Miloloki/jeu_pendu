from tkinter import * 
import tkinter as tk

fenetre = Tk()

canvas = Canvas(fenetre, width=750, height=625, background='pink')

poteau = canvas.create_line(225, 150, 225, 500, width=4)
base = canvas.create_line(150, 500, 300, 500, width=4)
poutre = canvas.create_line(225, 150, 400, 150, width=4)
corde = canvas.create_line(375, 150, 375, 200, width=4)
tete = canvas.create_oval(350, 200, 400, 250)

tabouret_base = canvas.create_line(330, 430, 420, 430, width=2)
tabouret_g = canvas.create_line(340, 500, 360, 430, width=2)
tabouret_d = canvas.create_line(410, 500, 385, 430, width=2)

corps = canvas.create_line(375, 250, 375, 350)
bras_g = canvas.create_line(325, 250, 375, 300)
bras_d = canvas.create_line(425, 250, 375, 300)
jambe_g = canvas.create_line(350, 430, 375, 350)
jambe_d = canvas.create_line(400, 430, 375, 350)

txt1 = canvas.create_text(375, 40, text="Jeu du pendu", font="Arial 32 italic", fill="purple")
txt2 = canvas.create_text(375, 80, text="Tapez une lettre et essayez de ne pas mourir", font="Arial 22 italic", fill="purple")

########################################################################
def mort_bonhomme():
	bras_tg = canvas.coords(bras_g, 350, 350, 375, 300)
	bras_td = canvas.coords(bras_d, 400, 350, 375, 300)
	jambe_tg = canvas.coords(jambe_g, 360, 430, 375, 350)
	jambe_td = canvas.coords(jambe_d, 390, 430, 375, 350)
	tabouret1 = canvas.delete(tabouret_base, tabouret_g, tabouret_d)



bouton_dead=Button(fenetre, text="DEAD", command=mort_bonhomme)			
bouton_dead.pack()

########################################################################

def choisir_mot():
		mot_a_trouver = "patate"
		return mot_a_trouver
		
def affiche_mot_tiret():
		mot_mystere = ''
		nombre_de_lettre = 0
		while nombre_de_lettre < len(mot_a_trouver):
			nombre_de_lettre +=1
			mot_mystere+= "_ "
		return mot_mystere

def lettre_dans_mot():												
		positions = []													#On déclare positions comme une liste""" 										
		position_actuelle = 0											#"""on part de 0 position initiale"""
		recuperation = saisir_lettre.get() 														
		
		for lettre_mot in mot_a_trouver: 								#"""pour chaque lettre dans le mot a trouver"""	
			if lettre_mot == recuperation: 								#"""si la lettre du mot correspond a la lettre donnée"""
				positions.append(position_actuelle) 					#"""on ajout la position où se trouve la lettre"""
			position_actuelle+=1 										#"""on incrémente pour essayer la lettre suivante"""
		print(recuperation)
		return positions

def affiche_lettres_trouvees():
		mot_a_afficher = ''
		position_actuelle = 0											#"""On part de 0 position initiale"""
		for lettre_mot in mot_a_trouver:  								#"""on parcours le mot"""		
			if position_actuelle in positions:							#"""est-ce que la positino du mot correspond au mot""" 			
				mot_a_afficher+=lettre_mot 								#"""Si oui on affiche la lettre"""
			else:
				mot_a_afficher+='_'										#"""Si non on affiche un tiret"""
			position_actuelle+=1

		return mot_a_afficher
		
########################################################################

mot_a_trouver = choisir_mot()

########################################################################

txt3 = canvas.create_text(375, 550, text=affiche_mot_tiret(), font="Arial 22 italic", fill="purple")

saisir_lettre = Entry(fenetre, textvariable=StringVar, width=1)


########################################################################

def lettre_joueur(self): 
	recuperation = saisir_lettre.get()
	fct = lettre_dans_mot()
	if fct == []:
		rect5 = canvas.create_rectangle(450, 450, 700, 700, fill="pink", width = 0)
		txt5 = canvas.create_text(575, 550, text="Raté,"+'\n'+"Recommence", font="Arial 22 italic", fill="purple")
		print(fct)
	else:
		rect5 = canvas.create_rectangle(450, 450, 700, 700, fill="pink", width = 0)
		txt5 = canvas.create_text(600, 550, text=recuperation, font="Arial 22 italic", fill="purple")
		print(fct)
	
saisir_lettre.bind('<Return>', lettre_joueur)
saisir_lettre.pack()


########################################################################
canvas.pack()



fenetre.mainloop()


