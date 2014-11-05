##RPG Games by Hugo and Hugo

def launch(scenarioName):
    print('\nYou are now playing ', scenarioName, ' \n Developped by the Prepa Team \n =============Loading============')
    ##fctConstruction Objets(scenarioName)utilisant la fonction fileReader pour obtenir les valeurs des attributs
    ##fileReader(scenarioName, "\\chests.txt")##Ligne de test
    ##testFunction1(scenarioName)##Ligne de test
    return True

##fct Qui ouvre et lit le fichier demandé. renvoie une liste contenant le fichier ligne par ligne, nécéssite un traitement ultèrieur. Non valable pour les txt salles
##Lors de la construction objet, on appelle la fonction puis on compte le nombre de lignes afin d'obtenir le nombre d'objet. On l'injecte dans une boucle for qu'on
##fait tourner en séparant chaque mot avec attributes[i].split(',')
def fileReader(scenarioName, fileName):
    path = "scenarios\\"+ scenarioName + fileName
    file = open(path, "r")
    ##print("File opened", file.name)
    attributes = file.read()
    attributes = attributes.splitlines()
    print(attributes)##Ligne de test
    return attributes

##Fct de test de la décomposition en éléments simples du string
def testFunction1(scenarioName):
    attributes = fileReader(scenarioName, "\\chests.txt")
    for i in range(0,len(attributes)):
        data = attributes[i].split(',')
        ##On mettra ici la construction de l'objet à l'aide des données récupérées
        print(data)
    return True

##Fct de lecture des pièces, c'est la fonction main des donjons. Elle est séparée de la fonction principale pour permettre l'implémentation d'un menu ou d'un village
def roomFunction(scenarioName, fileName):
    path = "scenarios\\"+ scenarioName +"\\"+ fileName +".txt"
    file = open(path, "r")
    ##print("File opened", file.name)
    text = file.read().split('/')
    roomName = fileName
    print(text[0],text[1])
    if(fileName=="end"):
        return True
    while(fileName==roomName):
        goodAnswer = False
        userRequest = input("What will you do?: ").lower()
        for i in range(2,len(text),2):##On compare toutes les actions possibles avec la réponse utilisateur
            ##print(text[i].strip()) ##Ligne de test
            if(text[i].strip()==userRequest):
                reference = text[i+1].strip()
                ##on renvoie la référence[2] à une fonction qui trouve la référence parmis les objets créés à l'initialisation
                ##Elle renvoie un autre fileName si il s'agit d'une porte (par exemple room2)
                ##fileName = "end"##ligne de test
                goodAnswer = True
        if (goodAnswer == False):
            print('Nothing happened...')
    roomFunction(scenarioName, fileName)

scenarioName = "test"
launch(scenarioName)
roomFunction(scenarioName, "room0")
print("Donjon terminé!\n Merci d'avoir joué")
