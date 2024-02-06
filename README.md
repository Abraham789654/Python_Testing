Ancienne version :

def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


Dans l'ancienne version, la fonction book cherche le club et la compétition correspondants dans les listes clubs et competitions, respectivement, en fonction de leurs noms. Si les deux sont trouvés, elle rend le modèle "booking.html" avec les détails du club et de la compétition. Sinon, elle renvoie un message d'erreur et le modèle "welcome.html".

Nouvelle version :

def book(competition, club):
    foundClub = next((c for c in clubs if c['name'] == club), None)
    foundCompetition = next((c for c in competitions if c['name'] == competition), None)

    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong - please try again", "error")
        return render_template('erreure.html')
        
Dans la nouvelle version, la fonction book utilise next pour rechercher le club et la compétition correspondants dans les listes clubs et competitions respectivement. Si les deux sont trouvés, elle rend le modèle "booking.html" avec les détails du club et de la compétition. Sinon, elle affiche un message d'erreur flash et rend le modèle "erreure.html".
