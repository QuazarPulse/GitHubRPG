##RPG Games by Hugo and Hugo

def launch(scenarioName):
    print('\nYou are now playing ', scenarioName, ' \n Developped by the Prepa Team \n =============Loading============')
    ##fctConstruction Objets(scenarioName)utilisant la fonction fileReader pour obtenir les valeurs des attributs
    fileReader(scenarioName, "\\chests.txt")
    return True

##fct Qui ouvre et lit le fichier demandé. Renvoie
def fileReader(scenarioName, fileName):
    path = "scenarios\\"+ scenarioName + fileName
    file = open(path, "r")
    print("File opened", file.name)
    for ligne in file:
        attributes = file.readline()
        print(attributes)
        ##appel du constructeur d'un objet appelé attributes[0]
    return attributes
    

scenarioName = "test"
launch(scenarioName)
