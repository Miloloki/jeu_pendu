# -*-coding:UTF-8 -*
import os
from random import *
os.chdir("C:/Users/Nouas/Desktop/RACHEL/Python/Pendu Python")

def lettre_dans_mot(lettre, mot_a_trouver):
		positions = [] 										
		position_actuelle = 0 			
		
		for lettre_mot in mot_a_trouver: 				
			if lettre_mot == lettre: 					
				positions.append(position_actuelle) 	
			position_actuelle+=1 						

		return positions 								

def affiche_lettres_trouvees(positions, mot_a_trouver):
		mot_a_afficher = ''
		
		position_actuelle = 0
		for lettre_mot in mot_a_trouver:  				
			if position_actuelle in positions: 			
				mot_a_afficher+=lettre_mot 				
			else:
				mot_a_afficher+='_'
			position_actuelle+=1

		return mot_a_afficher

def choisir_mot(donnees):
		liste_de_mot=[]									

		with open("donnees.py") as fichier:			
			for ligne in fichier:
				liste_de_mot = [liste_mots.strip() for liste_mots in fichier]
				liste_de_mot.append(ligne)					

			shuffle(liste_de_mot)							
			mot_a_trouver=liste_de_mot[0]					

		return mot_a_trouver

mot_a_trouver=choisir_mot("donnees.py")
positions_tout = []										
nb_coups=0


while nb_coups<8:
	lettre_joueur=input("Entrez une lettre : ")
	position_actuelle=lettre_dans_mot(lettre_joueur, mot_a_trouver)	
	
	if position_actuelle == []:
		nb_coups+=1		
	print(nb_coups)
	positions_tout+=position_actuelle
	mot_a_afficher = affiche_lettres_trouvees(positions_tout, mot_a_trouver)
	print(mot_a_afficher)



os.system("pause")
