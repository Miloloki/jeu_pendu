# -*-coding:UTF-8 -*
import os
from random import *
os.chdir("C:/Users/Nouas/Desktop/RACHEL/Python/Pendu Python")

def lettre_dans_mot(lettre, mot_a_trouver):
		positions = []													#On déclare positions comme une liste""" 										
		position_actuelle = 0 											#"""on part de 0 position initiale"""			
		
		for lettre_mot in mot_a_trouver: 								#"""pour chaque lettre dans le mot a trouver"""	
			if lettre_mot == lettre: 									#"""si la lettre du mot correspond a la lettre donnée"""
				positions.append(position_actuelle) 					#"""on ajout la position où se trouve la lettre"""
			position_actuelle+=1 										#"""on incrémente pour essayer la lettre suivante"""

		return positions 												#"""on renvoie la position"""								

def affiche_lettres_trouvees(positions, mot_a_trouver):
		mot_a_afficher = ''
		
		position_actuelle = 0											#"""On part de 0 position initiale"""
		for lettre_mot in mot_a_trouver:  								#"""on parcours le mot"""		
			if position_actuelle in positions:							#"""est-ce que la positino du mot correspond au mot""" 			
				mot_a_afficher+=lettre_mot 								#"""Si oui on affiche la lettre"""
			else:
				mot_a_afficher+='_'										#"""Si non on affiche un tiret"""
			position_actuelle+=1

		return mot_a_afficher

def choisir_mot(donnees):
		liste_de_mot=[]													#"""on créé notre liste"""				

		with open("donnees.py") as fichier:								#"""on déclare dans quel fichier on va aller chercher le mot, en lecture"""			
			for ligne in fichier:
				liste_de_mot = [liste_mots.strip() for liste_mots in fichier]
				liste_de_mot.append(ligne)								#"""on met le mot trouver dans notre liste de mot"""

			shuffle(liste_de_mot)										#"""shuffle nous sort les mots en aléatoire"""						
			mot_a_trouver=liste_de_mot[0]								#""" on prends le premier mot de notre liste de mot"""

		return mot_a_trouver


mot_a_trouver=choisir_mot("donnees.py")
print(mot_a_trouver)
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
