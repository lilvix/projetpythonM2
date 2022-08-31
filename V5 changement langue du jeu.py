from googletrans import Translator , constants
from random_word import RandomWords

r = RandomWords()
translator = Translator()

langue_destination='en'
langue_source='fr'
maxechec=3
langue_jeu='fr'


def generation_mot():
    randomen = r.get_random_word(hasDictionaryDef=True, minCorpusCount=20000)
    # peut changer la valeur pour modfier le niveau de difficulté; et prendre des mots plus ou moins commun
    mot_a_traduiref = translator.translate(randomen, dest=langue_source, src='en')
    return mot_a_traduiref.text


def recuperation_trad(traduction):       # sert à récupérer les différentes traductions possible du mot
    nb_trad = len(traduction.extra_data["possible-translations"][0][2])  # pour avoir le nombre de traduction alternative
    tab_tradalt = []
    for i in range(nb_trad):
        tab_tradalt.append(str.upper(traduction.extra_data["possible-translations"][0][2][i][0]))
    return tab_tradalt

def trad_menu(phrase_a_traduire):
    traduction = translator.translate(phrase_a_traduire, dest=langue_jeu, src="fr")
    return traduction.text

def choix_langue():
    temp_source = input(trad_menu("enter le nom de la langue que vous voulez utiliser : ") + " ")
    for clef in constants.LANGUAGES:
        if constants.LANGUAGES[clef] == temp_source:
            return clef

    print(trad_menu("la langue que vous avez entrer n'est pas disponible"))
    print(trad_menu("peut ètre que l'orthographe est mauvaise vous pouvez consulter la liste des langues disponibles dans le menu"))
    return None



def menu():
    choix = 0
    trouve = 0
    nbmot = 3
    global langue_source
    global langue_destination
    global langue_jeu

    while (choix != "3"):
        print(trad_menu("La langue du mot proposé à la traduction est le "+constants.LANGUAGES[langue_source]+" : pour la changer entrer 1"))
        print(trad_menu("La langue dans laquelle le mot doit ètre traduit est "+constants.LANGUAGES[langue_destination]+" : pour la changer entrer 2"))
        print(trad_menu("Pour commencer une partie : entrer 3"))
        print(trad_menu("Pour voir les langues disponibles : entrer 4"))
        print(trad_menu("Il y a actuelement "+str(nbmot)+" mots a trouver : pour modifier le nombre de mot à trouver entrer 5"))
        print(trad_menu("Le jeu est actuellement en "+constants.LANGUAGES[langue_jeu]+" : pour la changer entrer 6"))
        print(trad_menu("pour fermer le jeu : entrer 7"))

        choix = input(trad_menu("choix : ")+" ")

        if (choix == "4"):
            choix = 0
            print(trad_menu("langues disponibles :"))
            for clef in constants.LANGUAGES:
                print(constants.LANGUAGES[clef])
        if (choix == "1"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_source = temp_langue
                print(trad_menu("la langue des mots proposer à la traduction est désormait le " + constants.LANGUAGES[langue_source]))
        if (choix == "2"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                langue_destination = temp_langue
                print(trad_menu("la langue dans laquelle il faut traduire est désormait le " + constants.LANGUAGES[langue_destination]))

        if ((int(choix) < 1) or (int(choix) > 7)):
            print("choix incorecte")
        if (choix=="5"):
            nbmot=int(input("combien de mot voulez vous chercher : "))
        if (choix=="3"):
            partie(nbmot)
        if(choix=="6"):
            temp_langue = choix_langue()
            if (temp_langue != None):
                    langue_jeu = temp_langue


def partie(nbmot):
    motactuel = 1
    nbbonnereponse = 0
    nbmauvaisereponse = 0

    mot_a_traduire = generation_mot()

    while (nbmot >= motactuel):
        mot_a_traduire = generation_mot()
        traduction = translator.translate(mot_a_traduire, dest=langue_destination, src=langue_source)
        traduction_possible = recuperation_trad(traduction)
        nbechec = 0
        while (nbechec >= 0 and nbechec < 3):
            proposition = str.upper(input("donner la traduction du mot " + mot_a_traduire + " : "))
            if (proposition in traduction_possible):
                print("bonne réponse " + mot_a_traduire + " est bien traduit par " + proposition)
                nbbonnereponse = nbbonnereponse + 1
                motactuel = motactuel + 1
                nbechec = -1
            else:
                print("mauvaise réponse " + mot_a_traduire + " n'est pas traduit par " + proposition)
                nbechec = nbechec + 1
                if (nbechec == 3):
                    print("dommage vous n'avez pas trouver les bonne réponse était : ", end="")
                    print(traduction_possible, end="")
                    print(" vous ferez mieux au mot suivant")
                    nbmauvaisereponse = nbmauvaisereponse + 1
                    motactuel = motactuel + 1

    print("vous avez eu " + str(nbbonnereponse) + " bonne réponse et " + str(nbmauvaisereponse) + " mauvaise réponse")
    menu()




menu()
