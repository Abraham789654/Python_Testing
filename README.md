Ancienne version :

def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

Dans l'ancienne version, la fonction purchasePlaces recherche la compétition et le club correspondants dans les listes competitions et clubs respectivement, en fonction des noms soumis dans le formulaire. Ensuite, elle déduit le nombre de places requises de la compétition et renvoie un message flash indiquant que la réservation a été effectuée avec succès, avant de rendre le modèle "welcome.html".

Nouvelle version :

def purchasePlaces():
    competition_name = request.form['competition']
    club_name = request.form['club']
    places_required = int(request.form['places'])

    # Recherche de la compétition et du club dans les données existantes
    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)

    # Vérification si la compétition et le club existent
    if competition is None or club is None:
        flash('Error - Competition or club not found!')
        return render_template('welcome.html', club=club, competitions=competitions)

    # Vérification du nombre de places disponibles
    current_places = int(competition['numberOfPlaces'])
    
    if places_required <= 0 or places_required > current_places:
        flash('Error - Invalid number of places requested!')
        return render_template('welcome.html', club=club, competitions=competitions)
    
    if places_required == 12:
        flash('Info - You cannot buy more than 12 places!')
        return render_template('welcome.html', club=club, competitions=competitions)

    # Mise à jour du nombre de places après l'achat
    competition['numberOfPlaces'] = current_places - places_required

    flash('Great - Booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

Dans la nouvelle version, la fonction purchasePlaces prend des noms de compétition, de club et un nombre de places soumis dans le formulaire. Elle recherche ensuite la compétition et le club correspondants dans les listes competitions et clubs, respectivement, et vérifie si le nombre de places demandées est valide. Si tout est en ordre, elle met à jour le nombre de places disponibles pour la compétition et affiche un message flash indiquant que la réservation a été effectuée avec succès. Sinon, elle affiche un message d'erreur approprié.
