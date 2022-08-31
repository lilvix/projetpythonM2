from googletrans import Translator
from random_word import RandomWords

r = RandomWords()
translator = Translator()
langue_destination='en'
langue_source='fr'
nbechec=0
maxechec=3
motactuel=1
nbbonnereponse=0
nbmauvaisereponse=0


def generation_mot():
    randomen = r.get_random_word(hasDictionaryDef=True, minCorpusCount=20000)
    # peut changer la valeur pour modfier le niveau de difficulté; et prendre des mots plus ou moins commun
    mot_a_traduiref = translator.translate(randomen, dest=langue_source, src='en')
    return mot_a_traduiref.text


def recuperation_trad(traduction):       # sert à récupérer les différentes traductions possible du mot
    nb_trad = len(traduction.extra_data["possible-translations"][0][2])  # pour avoir le nombre de traduction alternative
    tab_tradalt = []
    for i in range(nb_trad):
        tab_tradalt.append(traduction.extra_data["possible-translations"][0][2][i][0])

    return tab_tradalt

# langue_destination=input("en qu'elle langue voulez vous traduire la phrase : ")
# langue_source = input("vous voulez traduire des mots de quelle langue : ")
# ca on le mettra quand on aura choisit lequelle on prend ,

nbmot=int(input("combien de mot voulez vous chercher : "))

mot_a_traduire = generation_mot()


while(nbmot>=motactuel):
    mot_a_traduire = generation_mot()
    traduction = translator.translate(mot_a_traduire, dest=langue_destination, src=langue_source)
    traduction_possible = recuperation_trad(traduction)
    nbechec=0
    while (nbechec>=0 and nbechec <3):
        proposition = input("donner la traduction du mot " + mot_a_traduire + " : ")
        if (proposition in traduction_possible):
            print("bonne réponse " + mot_a_traduire + " est bien traduit par " + proposition)
            nbbonnereponse = nbbonnereponse + 1
            motactuel = motactuel + 1
            nbechec=-1
        else:
            print("mauvaise réponse " + mot_a_traduire + " n'est pas traduit par " + proposition)
            nbechec = nbechec + 1
            if (nbechec == 3):
                print("dommage vous n'avez pas trouver les bonne réponse était : ", end="")
                print(traduction_possible,end="")
                print(" vous ferez mieux au mot suivant")
                nbmauvaisereponse = nbmauvaisereponse + 1
                motactuel = motactuel + 1


print("vous avez eu "+str(nbbonnereponse)+" bonne réponse et "+str(nbmauvaisereponse)+" mauvaise réponse" )


# le mot donner en premier par random word sera différent , de celui qu'on doit trouver après mais c'est
# le comportement normal de google traduction
