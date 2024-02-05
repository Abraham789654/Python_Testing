Ancienne version :
def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions
Dans l'ancienne version, la fonction loadCompetitions ouvre un fichier nommé "competitions.json" situé dans le répertoire actuel. Elle charge ensuite les données JSON à partir de ce fichier et extrait la liste des compétitions avant de la retourner.

Nouvelle version :
def loadCompetitions(filename="competitions.json"):
    with open(filename) as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions
Dans la nouvelle version, la fonction loadCompetitions prend un argument optionnel filename qui spécifie le nom du fichier à ouvrir. Par défaut, le nom du fichier est "competitions.json". Cette modification permet à l'utilisateur de spécifier un fichier différent s'il le souhaite. Le reste du code est inchangé par rapport à la version précédente.
