
from googletrans import Translator, constants
from random_word import RandomWords
from random import randint

r = RandomWords()
translator = Translator()

langue_destination = 'en'
langue_source = 'fr'
maxechec = 3
langue_jeu = 'fr'       # ne sourtout pas changer manuellement , changer à partir du menu
nbmot=3
mode_jeu="mot"


difficulte = "aléatoire"

liste_phrase_choix_langue=["enter le nom de la langue que vous voulez utiliser :",
                           "La langue que vous avez entré n'est pas disponible",
                           "peut ètre que l'orthographe est mauvaise vous pouvez consulter la liste des langues disponibles dans le menu"]

liste_phrase_menu=["Pour voir les langues disponibles : entrez 4",
                   str("Il y a actuelement " + str(nbmot) + " réponse a trouver : pour modifier le nombre de réponse à trouver entrez 5"),
                   "Pour commencer une partie : entrez 6",
                   "pour fermer le jeu : entrez 7",
                   "choix : ",
                   "langues disponibles :",
                   "choix incorecte",
                   "combien de mot voulez vous chercher (minimum 1, maximum 15) : ",
                   "pour utiliser les mots aléatoire : entrez 1 ",
                   "pour utiliser la liste facile : entrez 2 ",
                   "pour utiliser la liste moyenne : entrez 3 ",
                   "pour utiliser la liste difficile : entrez 4 ",
                   "combien de phrases voulez-vous chercher (minimum 1, maximum 5) : "]

# ses variable servent à ne pas àvoir à rapeller l'API , à chaque fois que l'on veut faire un print ou input,
# elle stock intialement ce qui correspond à des valeurs par défault utiliser lors du lancement du jeu
# on ne stock que celle qui risque d'ètre apeller plusieurs fois pour donner le meme résultat

liste_phrase_special=["La langue proposé à la traduction est le francais : pour la changer entrez 1",
                      "La langue dans laquelle il faut traduire est l'anglais : pour la changer entrez 2",
                      "Le jeu est actuellement en francais : pour la changer entrez 3",
                      "les mots proposé sont générer aléatoirement : pour les modifier entrez 8",
                      "Des mots sont actuellement proposé à la tradution pour passer aux phrases entrez : 9",
                      "Des phrases sont actuellement proposées à la tradution pour passer aux mots entrez : 9"]

# les phrases qui sont modifié lors d'une action de l'utilisateur et pas au changement de langue

liste_phrase_jeu=["Donnez la traduction de ",
                  " bonne réponse ",
                  " est bien traduit par ",
                  " mauvaise réponse ",
                  " n'est pas traduit par ",
                  " dommage vous n'avez pas trouver, les bonnes réponses étaient : ",
                  " vous ferez mieux à la question suivante",
                  " vous avez eu ",
                  "et",
                  "essayez d'améliorer votre score"
                  ]

liste_mot_simple=["jambe", "pied", "nez", "père", "sœur", "maison", "lit", "lampe", "verre", "table",
                   "robe", "rue", "moto", "nuit", "orange"  ]

liste_mot_moyen=["quereller", "engouler", "convenance", "moustache", "vidange", "figer", "contacter",
                 "prostate", "boulon", "cacahuète", "patiente", "chopper", "piratage", "information",
                 "rétracter"]

liste_mot_difficile=["doxycycline", "interopérabilité", "convenance", "hirsute", "précipitamment",
                     "pintade", "chiropracteur", "zircon", "lotissement", "amandine", "pasteurisation",
                     "entrebâiller", "contentieux", "philanthrope", "psychothérapie"]

phrase_simple=["C’est combien pour l’acheter ?",
"Vous allez bien ?",
"Je te souhaite une bonne journée ",
"je n’ai plus faim",
"Vous allez faire quoi ce soir ?"]

phrase_moyenne=["c’est la plus belle aubaine que je t’aie rencontrée",
"Chaque jour, chaque seconde, tu prends une décision qui pourrait changer ta vie ?",
"La mode se démode, le style jamais",
"pour être irremplaçable, il faut être différente",
"Parfois on regarde le ciel, on fixe une étoile et on pense à une personne"]

phrase_difficile=["Là où on s’aime, il ne fait jamais nuit. ",
"une hirondelle ne fait pas le printemps.",
"L’homme propose, Dieu dispose.",
"Le jeu ne vaut pas la chandelle.",
"Aujourd’hui n’est pas le lendemain d’hier, mais la veille de demain."]

liste_indice_mot=[]
liste_indice_phrase = []


def traduction_phrase_du_jeu():
    global liste_phrase_menu
    global liste_phrase_choix_langue
    global langue_jeu

    if (langue_jeu!='fr'):
        for i in range (0,len(liste_phrase_choix_langue)):
            liste_phrase_choix_langue[i]=trad_menu(liste_phrase_choix_langue[i])
        for i in range (0,len(liste_phrase_menu)):
            liste_phrase_menu[i]=trad_menu(liste_phrase_menu[i])
        for i in range (0,len(liste_phrase_jeu)):
            liste_phrase_jeu[i]=trad_menu(liste_phrase_jeu[i])
        liste_phrase_special[2] = str(trad_menu("La langue du jeu est actuellement le " + constants.LANGUAGES[langue_jeu] + " : pour la changer entrez 3"))
        liste_phrase_special[1] = str(trad_menu("La langue dans laquelle le mot doit ètre traduit est " + constants.LANGUAGES[langue_destination] + " : pour la changer entrez 2"))
        liste_phrase_special[0] = str(trad_menu("La langue du mot proposé à la traduction est le " + constants.LANGUAGES[langue_source] + " : pour la changer entrez 1"))
        liste_phrase_special[3] = str(trad_menu(liste_phrase_special[3]))
        liste_phrase_special[4] = str(trad_menu(liste_phrase_special[6]))


def generation_mot():
    global difficulte
    global liste_mot_difficile
    global liste_mot_moyen
    global liste_mot_simple
    global mode_jeu
    global liste_indice_phrase
    global liste_indice_mot

    if len(liste_indice_mot)==15:
        liste_indice_mot=[]
    if len(liste_indice_phrase)==5:
        liste_indice_phrase=[]

    if mode_jeu=="mot":
        nb = randint(0, 14)
        while nb in liste_indice_mot:
            nb = randint(0, 14)
        assert nb not in liste_indice_mot
        liste_indice_mot.append(nb)
        assert nb in liste_indice_mot
        if difficulte == "simple":
            return liste_mot_simple[nb]
        if difficulte == "moyen":
            return liste_mot_moyen[nb]
        if difficulte == "difficile":
            return liste_mot_difficile[nb]
        if difficulte == "aléatoire":
            randomen = r.get_random_word(hasDictionaryDef=True, minCorpusCount=20000)
            # peut changer la valeur pour modfier le niveau de difficulté; et prendre des mots plus ou moins commun
            mot_a_traduiref = translator.translate(randomen, dest=langue_source, src='en')
            return mot_a_traduiref.text
    else:
        nb = randint(0, 4)
        while nb in liste_indice_phrase:
            nb = randint(0, 4)
        assert nb not in liste_indice_phrase
        liste_indice_phrase.append(nb)
        assert nb in liste_indice_phrase
        if difficulte == "simple":
            return phrase_simple[nb]
        if difficulte == "moyen":
            return phrase_moyenne[nb]
        if difficulte == "difficile":
            return phrase_difficile[nb]


def recuperation_trad(traduction):  # sert à récupérer les différentes traductions possible du mot
    nb_trad = len(
        traduction.extra_data["possible-translations"][0][2])  # pour avoir le nombre de traduction alternative
    tab_tradalt = []
    for i in range(nb_trad):
        tab_tradalt.append(str.upper(traduction.extra_data["possible-translations"][0][2][i][0]))

    assert nb_trad==len(tab_tradalt)
    return tab_tradalt


def trad_menu(phrase_a_traduire):
    global langue_jeu
    traduction = translator.translate(phrase_a_traduire, dest=langue_jeu, src="fr")
    return traduction.text


def choix_langue():
    temp_source = input(liste_phrase_choix_langue[0] + " ")
    for clef in constants.LANGUAGES:
        if constants.LANGUAGES[clef] == temp_source:
            assert clef in constants.LANGUAGES[clef]
            return clef
    print(liste_phrase_choix_langue[1])
    print(liste_phrase_choix_langue[2])
    return None


def menu():
    global langue_source
    global langue_destination
    global langue_jeu
    global liste_phrase_menu
    global liste_phrase_special
    global nbmot
    global difficulte
    global mode_jeu
    choix = 0

    while (choix != "7"):
        for i in range (0,3):
            print(liste_phrase_special[i])
        for i in range(0,4):
            print(liste_phrase_menu[i])
        print(liste_phrase_special[3])
        if mode_jeu=="mot":
            print(liste_phrase_special[4])
        else:
            print(liste_phrase_special[5])

        choix = str(input(liste_phrase_menu[4] + " "))

        if (choix == "4"):
            print(trad_menu(liste_phrase_menu[5]))
            for clef in constants.LANGUAGES:
                print(constants.LANGUAGES[clef])
        if (choix == "1"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_source = temp_langue
                print(trad_menu("la langue des mots proposes à la traduction est désormais le " + constants.LANGUAGES[
                    langue_source]))
                liste_phrase_special[0]=str(trad_menu("La langue du mot proposé à la traduction est le " + constants.LANGUAGES[langue_source] + " : pour la changer entrez 1"))
        if (choix == "2"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_destination = temp_langue
                print(trad_menu("la langue dans laquelle il faut traduire est désormais le " + constants.LANGUAGES[
                    langue_destination]))
                liste_phrase_special[1] = str(trad_menu("La langue dans laquelle le mot doit ètre traduit est " + constants.LANGUAGES[langue_destination] + " : pour la changer entrez 2"))

        if ((int(choix) < 1) or (int(choix) > 9)):
            print(liste_phrase_menu[6])
        if (choix == "5"):
            if (mode_jeu=="mot"):
                nbmot = int(input(liste_phrase_menu[7]))
                if (nbmot < 1):
                    nbmot = 1
                elif (nbmot > 15):
                    nbmot = 15
            else:
                nbmot = int(input(liste_phrase_menu[12]))
                if (nbmot < 1):
                    nbmot = 1
                elif (nbmot > 5):
                    nbmot = 5
            liste_phrase_menu[1] = trad_menu(str("Il y a actuelement " + str(nbmot) + " réponses a trouver : pour modifier le nombre de réponses à trouver entrer 5"))
        if (choix == "6"):
            partie(nbmot)
        if (choix == "3"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_jeu = temp_langue
                traduction_phrase_du_jeu()
                print(trad_menu("la langue du jeu est désormais le " + constants.LANGUAGES[langue_jeu]))
        if (choix=="8"):
            for i in range (8,12):
                print(liste_phrase_menu[i])
            choixdif=input(liste_phrase_menu[4])
            if (choixdif=="1"):
                if (mode_jeu!="mot"):
                    print(str(trad_menu("Il n'est pas possible de générer aléatoirement des phrases")))
                    print(str(trad_menu("les phrases proposées n'ont pas été modifiées")))
                else:
                    print(str(trad_menu("les questions proposées ont bien été modifié")))
                    difficulte = "aléatoire"
                    liste_phrase_special[3] = str(trad_menu("les mots proposés sont générés aléatoirement , pour les modifier entrez 8"))

            elif(choixdif=="2"):
                difficulte = "simple"
                liste_phrase_special[3] = str(trad_menu("les questions propsés font partie de la liste simple : pour les modifier entrez 8",))
                print(str(trad_menu("les questions proposées ont bien été modifié")))
            elif (choixdif == "3"):
                difficulte = "moyen"
                liste_phrase_special[3] = str(trad_menu("les questions propsées font partie de la liste moyenne : pour les modifier entrer 8",))
                print(str(trad_menu("les questions proposées ont bien été modifié")))
            elif (choixdif == "4"):
                liste_phrase_special[3] = str(trad_menu("les questions propsées font partie de la liste difficile : pour les modifier entrez 8",))
                print(str(trad_menu("les questions proposées ont bien été modifié")))
                difficulte = "difficile"
            else:
                print(liste_phrase_menu[5])
        if (choix=="9"):
            if (mode_jeu=="mot"):
                mode_jeu="phrase"
                if (difficulte=="aléatoire"):
                    difficulte="simple"
                    liste_phrase_special[3] = str(trad_menu("les questions proposées font partie de la liste simple : pour les modifier entrez 8", ))
            else:
                mode_jeu="mot"

def division_phrase(traduction_possile):
    tab_phrase_split=[]
    for each in traduction_possile:
        tab_phrase_split.append(each.split())
    return tab_phrase_split

def score_phrase(propostion,tab_phrase_split):
    longeur=len(tab_phrase_split[0])
    point=100/longeur
    score=0
    trouve=0
    liste_proposition=propostion.split()
    for each in liste_proposition:
        for i in range (0,len(tab_phrase_split)):
            if (each in tab_phrase_split[i]):
                trouve=1
        if (trouve==1):
            score=score+point
            print(str(trad_menu("le mot "+each+" fait bien partie de la phrase")))
            trouve = 0
        else:
            print(str(trad_menu("le mot " + each + " ne fait pas partie de la phrase")))
            score=score-point

    if (score>100):
        score=100
    if (score<0):
        score=0
    print(str(trad_menu("votre score sur cette phrase est de "+str(int(score))+" % de réussite")))
    return score


def partie(nbmot):
    motactuel = 1
    nbbonnereponse = 0
    nbmauvaisereponse = 0
    global mode_jeu
    tab_score=[]
    max_score_essaie=0

    while (nbmot >= motactuel):
        mot_a_traduire = generation_mot()
        traduction = translator.translate(mot_a_traduire, dest=langue_destination, src=langue_source)
        traduction_possible = recuperation_trad(traduction)
        if mode_jeu!="mot":
            tab_phrase_split=division_phrase(traduction_possible)
        nbechec = 0
        while (nbechec >= 0 and nbechec < 3):
            proposition = str.upper(input(liste_phrase_jeu[0] +" "+ mot_a_traduire + " : "))
            if mode_jeu=="mot":
                if (proposition in traduction_possible):
                    print(liste_phrase_jeu[1] + " " + mot_a_traduire + " " + liste_phrase_jeu[2] + " " + proposition)
                    nbbonnereponse = nbbonnereponse + 1
                    motactuel = motactuel + 1
                    nbechec = -1
                else:
                    print(liste_phrase_jeu[3] + " " + mot_a_traduire + " " + liste_phrase_jeu[4] + " " + proposition)
                    nbechec = nbechec + 1
                    if (nbechec == 3):
                        print(liste_phrase_jeu[5] + " ", end="")
                        print(traduction_possible, end="")
                        print(liste_phrase_jeu[6] + " ")
                        nbmauvaisereponse = nbmauvaisereponse + 1
                        motactuel = motactuel + 1
            else:
                score_essaie=score_phrase(proposition,tab_phrase_split)
                if (score_essaie>max_score_essaie):
                    max_score_essaie=score_essaie
                if (score_essaie==100):
                    print(liste_phrase_jeu[1])
                    motactuel = motactuel + 1
                    nbechec = -1
                    tab_score.append(100)
                else:
                    nbechec=nbechec+1
                    print(liste_phrase_jeu[9])
                if (nbechec == 3):
                    print(liste_phrase_jeu[5] + " ", end="")
                    print(traduction_possible, end="")
                    print(liste_phrase_jeu[6] + " ")
                    motactuel = motactuel + 1
                    print(str(trad_menu("votre meilleurs socre pour cette phrase était de "+str(int(max_score_essaie)))))
                    tab_score.append(max_score_essaie)
                    max_score_essaie=0
    if (mode_jeu=="mot"):
        print(liste_phrase_jeu[7] +" "+ str(nbbonnereponse) +" "+ liste_phrase_jeu[1]+" "+ liste_phrase_jeu[8] +" "+ str(nbmauvaisereponse) +" "+ liste_phrase_jeu[3])
    else:
        score_total=0
        for each in tab_score:
            score_total=score_total+each

        print(str(trad_menu("votre score moyen pour cette partie est de "+str(int(score_total/len(tab_score)))+ "% de réussite")))
    menu()


menu()
