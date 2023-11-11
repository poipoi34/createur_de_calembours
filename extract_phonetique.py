# ce script extrait les mots en phonétique avec plus de 2 phonem

f_liste_mot_phonetique = open("liste_mot_phonetique.txt","w")
with open("Dico332Kmot.txt") as liste_mot_utf8:
    it = 0
    for ligne in liste_mot_utf8:
        
        i1 = ligne.find(";")
        i2 = ligne[i1+1:].find(";")
        i0 = -1
        if ligne.count(",") and ligne.find(",") < i1:
            i0 = ligne.find(",")
        if i2 > 3:
            f_liste_mot_phonetique.write(ligne[i1+1:i1+i2+1] + ";" + ligne[i0+1:i1] + "\n")
        
        
