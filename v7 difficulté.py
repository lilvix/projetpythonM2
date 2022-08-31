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

difficulte = "aléatoire"

liste_phrase_choix_langue=["enter le nom de la langue que vous voulez utiliser :",
                           "la langue que vous avez entrer n'est pas disponible",
                           "peut ètre que l'orthographe est mauvaise vous pouvez consulter la liste des langues disponibles dans le menu"]

liste_phrase_menu=["Pour voir les langues disponibles : entrer 4",
                   str("Il y a actuelement " + str(nbmot) + " mots a trouver : pour modifier le nombre de mot à trouver entrer 5"),
                   "Pour commencer une partie : entrer 6",
                   "pour fermer le jeu : entrer 7",
                   "choix : ",
                   "langues disponibles :",
                   "choix incorecte",
                   "combien de mot voulez vous chercher (minimum 1, maximum 15) : ",
                   "pour utiliser les mots aléatoire : entrer 1 ",
                   "pour utiliser la liste de mot facile : entrer 2 ",
                   "pour utiliser la liste de mot moyen : entrer 3 ",
                   "pour utiliser la liste de mot difficile : entrer 4 "]

# ses variable servent à ne pas àvoir à rapeller l'API , à chaque fois que l'on veut faire un print ou input,
# elle stock intialement ce qui correspond à des valeurs par défault utiliser lors du lancement du jeu
# on ne stock que celle qui risque d'ètre apeller plusieurs fois pour donner le meme résultat

liste_phrase_special=["La langue du mot proposé à la traduction est le francais : pour la changer entrer 1",
                      "La langue dans laquelle le mot doit ètre traduit est l'anglais : pour la changer entrer 2",
                      "La langue du jeu est actuellement le francais : pour la changer entrer 3",
                      "les mots proposé sont générer aléatoirement : pour les modifier entrer 8"]

# les phrases qui sont modifié lors d'une action de l'utilisateur et pas au changement de langue

liste_phrase_jeu=["donner la traduction du mot ",
                  " bonne réponse ",
                  " est bien traduit par ",
                  " mauvaise réponse ",
                  " n'est pas traduit par ",
                  "dommage vous n'avez pas trouver les bonne réponse était : ",
                  " vous ferez mieux au mot suivant",
                  "vous avez eu ",
                  "et"
                  ]

liste_mot_simple=["jambe", "pied", "nez", "père", "sœur", "maison", "lit", "lampe", "verre", "table",
                   "robe", "rue", "moto", "nuit", "orange"  ]

liste_mot_moyen=["quereller", "engouler", "convenance", "moustache", "vidange", "figer", "contacter",
                 "prostate", "boulon", "cacahuète", "patiente", "chopper", "piratage", "information",
                 "rétracter"]

liste_mot_difficile=["doxycycline", "interopérabilité", "convenance", "hirsute", "précipitamment",
                     "pintade", "chiropracteur", "zircon", "lotissement", "amandine", "pasteurisation",
                     "entrebâiller", "contentieux", "philanthrope", "psychothérapie"]


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
        liste_phrase_special[2] = str(trad_menu("La langue du jeu est actuellement le " + constants.LANGUAGES[langue_jeu] + " : pour la changer entrer 3"))
        liste_phrase_special[1] = str(trad_menu("La langue dans laquelle le mot doit ètre traduit est " + constants.LANGUAGES[langue_destination] + " : pour la changer entrer 2"))
        liste_phrase_special[0] = str(trad_menu("La langue du mot proposé à la traduction est le " + constants.LANGUAGES[langue_source] + " : pour la changer entrer 1"))
        liste_phrase_special[3] = str(trad_menu(liste_phrase_special[3]))


def generation_mot():
    global difficulte
    global liste_mot_difficile
    global liste_mot_moyen
    global liste_mot_simple

    if difficulte=="simple":
        nb=randint(0,len(liste_mot_simple)-1)
        return liste_mot_simple[nb]
    if difficulte=="moyen":
        nb=randint(0,len(liste_mot_simple)-1)
        return liste_mot_moyen[nb]
    if difficulte=="difficile":
        nb=randint(0,len(liste_mot_simple)-1)
        return liste_mot_difficile[nb]
    if difficulte=="aléatoire":
        randomen = r.get_random_word(hasDictionaryDef=True, minCorpusCount=20000)
        # peut changer la valeur pour modfier le niveau de difficulté; et prendre des mots plus ou moins commun
        mot_a_traduiref = translator.translate(randomen, dest=langue_source, src='en')
        return mot_a_traduiref.text


def recuperation_trad(traduction):  # sert à récupérer les différentes traductions possible du mot
    nb_trad = len(
        traduction.extra_data["possible-translations"][0][2])  # pour avoir le nombre de traduction alternative
    tab_tradalt = []
    for i in range(nb_trad):
        tab_tradalt.append(str.upper(traduction.extra_data["possible-translations"][0][2][i][0]))
    return tab_tradalt


def trad_menu(phrase_a_traduire):
    global langue_jeu
    traduction = translator.translate(phrase_a_traduire, dest=langue_jeu, src="fr")
    return traduction.text


def choix_langue():
    temp_source = input(liste_phrase_choix_langue[0] + " ")
    for clef in constants.LANGUAGES:
        if constants.LANGUAGES[clef] == temp_source:
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
    choix = 0

    while (choix != "7"):
        for i in range (0,3):
            print(liste_phrase_special[i])
        for i in range(0,4):
            print(liste_phrase_menu[i])
        print(liste_phrase_special[3])
        choix = str(input(liste_phrase_menu[4] + " "))

        if (choix == "4"):
            print(trad_menu(liste_phrase_menu[5]))
            for clef in constants.LANGUAGES:
                print(constants.LANGUAGES[clef])
        if (choix == "1"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_source = temp_langue
                print(trad_menu("la langue des mots proposer à la traduction est désormait le " + constants.LANGUAGES[
                    langue_source]))
                liste_phrase_special[0]=str(trad_menu("La langue du mot proposé à la traduction est le " + constants.LANGUAGES[langue_source] + " : pour la changer entrer 1"))
        if (choix == "2"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_destination = temp_langue
                print(trad_menu("la langue dans laquelle il faut traduire est désormait le " + constants.LANGUAGES[
                    langue_destination]))
                liste_phrase_special[1] = str(trad_menu("La langue dans laquelle le mot doit ètre traduit est " + constants.LANGUAGES[langue_destination] + " : pour la changer entrer 2"))

        if ((int(choix) < 1) or (int(choix) > 8)):
            print(liste_phrase_menu[6])
        if (choix == "5"):
            nbmot = int(input(liste_phrase_menu[7]))
            if(nbmot<1):
                nbmot=1
            elif(nbmot>15):
                nbmot=15
            liste_phrase_menu[1]=trad_menu(str("Il y a actuelement " + str(nbmot) + " mots a trouver : pour modifier le nombre de mot à trouver entrer 5"))
        if (choix == "6"):
            partie(nbmot)
        if (choix == "3"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_jeu = temp_langue
                traduction_phrase_du_jeu()
                print(trad_menu("la langue du jeu est désormait le " + constants.LANGUAGES[langue_jeu]))
        if (choix=="8"):
            for i in range (8,12):
                print(liste_phrase_menu[i])
            choixdif=input(liste_phrase_menu[4])
            if (choixdif=="1"):
                difficulte="aléatoire"
                liste_phrase_special[3]=str(trad_menu("les mots proposé sont générer aléatoirement , pour les modifier entrer 8"))
                print(str(trad_menu("les mots ont proposé ont bien été modifié")))
            elif(choixdif=="2"):
                difficulte = "simple"
                liste_phrase_special[3] = str(trad_menu("les mots propsés font partie de la liste de mot simple : pour les modifier entrer 8",))
                print(str(trad_menu("les mots ont proposé ont bien été modifié")))
            elif (choixdif == "3"):
                difficulte = "moyen"
                liste_phrase_special[3] = str(trad_menu("les mots propsés font partie de la liste de mot moyen : pour les modifier entrer 8",))
                print(str(trad_menu("les mots ont proposé ont bien été modifié")))
            elif (choixdif == "4"):
                liste_phrase_special[3] = str(trad_menu("les mots propsés font partie de la liste de mot difficile : pour les modifier entrer 8",))
                print(str(trad_menu("les mots ont proposé ont bien été modifié")))
                difficulte = "difficile"
            else:
                print(liste_phrase_menu[5])


def partie(nbmot):
    motactuel = 1
    nbbonnereponse = 0
    nbmauvaisereponse = 0

    while (nbmot >= motactuel):
        mot_a_traduire = generation_mot()
        traduction = translator.translate(mot_a_traduire, dest=langue_destination, src=langue_source)
        traduction_possible = recuperation_trad(traduction)
        nbechec = 0
        while (nbechec >= 0 and nbechec < 3):
            proposition = str.upper(input(liste_phrase_jeu[0] +" "+ mot_a_traduire + " : "))
            if (proposition in traduction_possible):
                print(liste_phrase_jeu[1] +" "+ mot_a_traduire +" "+ liste_phrase_jeu[2] +" "+ proposition)
                nbbonnereponse = nbbonnereponse + 1
                motactuel = motactuel + 1
                nbechec = -1
            else:
                print(liste_phrase_jeu[3] +" "+ mot_a_traduire +" "+ liste_phrase_jeu[4] +" "+ proposition)
                nbechec = nbechec + 1
                if (nbechec == 3):
                    print(liste_phrase_jeu[5]+" ", end="")
                    print(traduction_possible, end="")
                    print(liste_phrase_jeu[6]+" ")
                    nbmauvaisereponse = nbmauvaisereponse + 1
                    motactuel = motactuel + 1

    print(liste_phrase_jeu[7] +" "+ str(nbbonnereponse) +" "+ liste_phrase_jeu[1]+" "+ liste_phrase_jeu[8] +" "+ str(nbmauvaisereponse) +" "+ liste_phrase_jeu[3])
    menu()


menu()

