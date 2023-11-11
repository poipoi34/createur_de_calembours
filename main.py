#making a graph by defining a class node that has a list of children nodes
#nodes have phonem information and bool finishing

liste_phonem = ['1', 'A', 'E', 'G', 'H', 'I', 'J', 'N', 'O', 'V', 'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'U', 'u', 'v', 'w', 'y', 'z', 'â', 'è', 'é','ñ']
dict_phonem_model = {}
for phonem in liste_phonem:
    dict_phonem_model[phonem] = False

class Node:
    def __init__(o,phonem,depth):
        o.phonem = phonem
        o.finishing = False
        o.phonem_into = dict_phonem_model.copy() #liste de nodes
        o.list_of_child = [] #liste de nodes
        o.parent = None
        o.depth = depth

    def remonter(o):
        #retourne le mot qui finit par ce node
        if o.finishing == False:
            print("weird, trying to remonter une node qui n'est pas feuille")
        mot = o.phonem
        cur_node = o
        while (cur_node.depth > 0):
            mot = cur_node.parent.phonem + mot
            cur_node = cur_node.parent
        return mot
            

class Graph:
    def __init__(o):
        o.list_of_child = []
        o.phonem_into = dict_phonem_model.copy() #liste de nodes
        o.depth = 0
        
        o.word = ""
        
    def add(o,mot):
        i = 0
        cur_node = o
        while (i < len(mot)):
            if cur_node.phonem_into[mot[i]] == False:
                new_node = Node(mot[i],i)
                cur_node.phonem_into[mot[i]] = new_node
                cur_node.list_of_child.append(new_node)
                new_node.parent = cur_node
            if i == len(mot)-1:
                cur_node.phonem_into[mot[i]].finishing = True
            cur_node = cur_node.phonem_into[mot[i]]
            i+=1


    def print_all_words_from_node(o,node):
        for child in node.list_of_child:
            if child.finishing == True:
                print(child.remonter())

    def print_all_words(o):
        print_all_words_from_node(o)

    def get_words_starting_with(o,syl):
        
        
    def get_words_starting_from_node(o,node):
        liste = []
        o.rec(node,liste)
        return liste

    def rec(o,node,liste):
        

    def liste_de_mot_commençant_par(o,syl):
        liste = []
        node = o
        possible = True
        for char in syl:
            if node.phonem_into[char] != False:
                node = phonem_into[char]
            else:
                possible = False
        if possible = False:
            return []
        l = liste_de_mot_from_node(node)
        liste = [syl + mot for mot in l]
        #unfinished, parcours en largeur pas idéal

    def trouver_calembours(deg = 2):
        #parcours en profondeur. on collecte la suite de phonem,
        #une fois tombé sur un phonem "finish", continuer avec comme départ
        #les deg dernier phonem
        #faire le parcours en profondeur à partir des 2 dernier phonems du mot
        liste_phonems = []
        liste_feuille = []
        parcours()

    def parcours(o,cur_node,liste_feuille,liste_phonems):
        
        


def extraire_fichier(f):
    l = []
    for ligne in f:
        l.append(ligne[:-1])
    return l

liste_phonem = []
f_liste_mot = open("liste_mot_phonetique.txt","r")

liste_mot = extraire_fichier(f_liste_mot)

graph = Graph()

for mot in liste_mot:
    graph.add(mot)

def recherche_calembours(deg = 2):
    calembour = []
    for mot in liste_mot:
        calembour.append(mot)
        recherche_calembours_commencant_par(mot[:-2],calembour)

def recherche_calembours_commencant_par(mot,calembour):
    pass


    





    

