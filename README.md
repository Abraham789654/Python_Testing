Ancienne version :

def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)
    
Dans l'ancienne version, la fonction showSummary récupère un club en fonction de l'email soumis dans le formulaire. Elle recherche ce club dans la liste clubs et le transmet ensuite au modèle "welcome.html" avec la liste des compétitions.

Nouvelle version :

def showSummary():
    email = request.form['email']
    club = next((club for club in clubs if club['email'] == email), None)
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        error_message = 'Error - Email not found.'
        return render_template('index.html', error_message=error_message)

Dans la nouvelle version, la fonction showSummary est définie comme une vue Flask associée à l'URL '/showSummary'. Elle récupère l'email soumis dans le formulaire, recherche le club correspondant dans la liste clubs, puis renvoie le modèle "welcome.html" avec les détails du club et la liste des compétitions. Si l'email n'est pas trouvé, un message d'erreur est renvoyé au modèle "index.html".
