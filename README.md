Ancienne version :
def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

   Dans l'ancienne version, la fonction loadClubs ouvre un fichier nommé "clubs.json" situé dans le répertoire actuel. Il charge ensuite les données JSON à partir de ce fichier et extrait la liste des clubs avant de la retourner.
   
Nouvelle version :
def loadClubs(filename="clubs.json"):
    with open(filename) as c:
       listOfClubs = json.load(c)['clubs']
       return listOfClubs
Dans la nouvelle version, la fonction loadClubs prend un argument optionnel filename qui spécifie le nom du fichier à ouvrir. Par défaut, le nom du fichier est "clubs.json". Cette modification permet à l'utilisateur de spécifier un fichier différent s'il le souhaite. Le reste du code est inchangé par rapport à la version précédente.
