
class Graph_Des_Calembours:
    def __init__(o):
        o.liste_mot = []
        o.liste_n_phonem = [[] for i in range(5)] # associe à un n, la liste des n-phonem (n = 2,3,4)
        o.indices_n_phonem = [{} for i in range(5)] # associe à chaque n_phonem l'indice à partir duquel il commence et
                                                    # celui à partir duquel il finit dans liste_mot -> [commence,fini]
        o.corr_deg3 = {} #associe à chaque 3-phonem les mots qui commencent par ce 3-phonem
        o.corr_deg4 = {} #associe à chaque 4-phonem les mots qui commencent par ce 4-phonem
    
    def ajouter_mot(o,word):
        pass

    def créer_liste_n_phonem(o):
        #cette fonction crée la liste des n_phonem ainsi que 
        #les dictionnaire qui au n-phonem associe les indices à partir duquel il commence et fini

        cur_n_phonem = [None,None,o.liste_mot[0][:2],o.liste_mot[0][:3],o.liste_mot[0][:4]]

        for n in range(2,5):
            o.liste_n_phonem[n].append(cur_n_phonem[n])
            o.indices_n_phonem[n][cur_n_phonem[n]] = [0,0]

        for i in range(len(o.liste_mot)):
            mot = o.liste_mot[i]
            for n in range(2,5):
                if mot[:n] != cur_n_phonem[n]:
                    o.indices_n_phonem[n][cur_n_phonem[n]][1] = i
                    cur_n_phonem[n] = mot[:n]
                    o.liste_n_phonem[n].append(cur_n_phonem[n])
                    o.indices_n_phonem[n][cur_n_phonem[n]] = [i,i]

    def get_tranche_de_mot_deg2(o,ph_word):
        syl = ph_word[-2:]
        if syl in o.liste_n_phonem[2]:
            a,b = o.indices_n_phonem[2][syl]
            if b > a + 50:
                return o.liste_mot[a:a+50]
            else:
                return o.liste_mot[a:b]
        return []
    
    def get_deg3_words(o,ph_word):
        syl = ph_word[-3:]
        if syl in o.liste_n_phonem[3]:
            return o.corr_deg3[syl]
        else:
            return []
        
    def get_deg4_words(o,ph_word):
        syl = ph_word[-4:]
        if syl in o.liste_n_phonem[4]:
            return o.corr_deg3[syl]
        else:
            return []
            


    def créer_corr_deg3(o):
        for triphonem in o.liste_n_phonem[3]:
            a,b = o.indices_n_phonem[3][triphonem]
            o.corr_deg3[triphonem] = o.liste_mot[a:b]

    def créer_corr_deg4(o):
        for quatriphonem in o.liste_n_phonem[4]:
            a,b = o.indices_n_phonem[4][quatriphonem]
            o.corr_deg3[quatriphonem] = o.liste_mot[a:b]
        
    def compatibilite_ex(o,deg,mot1,mot2):
        if mot1[-deg:] == mot2[:deg]:
            return True
        return False
    
    def compatibilite(o,deg,mot1,mot2):
        for _deg in range(2,deg+1):
            if o.compatibilite_ex(_deg,mot1,mot2):
                return True
        return False

