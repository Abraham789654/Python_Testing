import json
from datetime import datetime, date
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs(filename="clubs.json"):
    with open(filename) as c:
       listOfClubs = json.load(c)['clubs']
       return listOfClubs


def loadCompetitions(filename="competitions.json"):
    with open(filename) as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html', clubs = clubs, competitions = competitions)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    email = request.form['email']
    club = next((club for club in clubs if club['email'] == email), None)
    # Définir la variable today avec la date actuelle
    
    if club:
        today = date.today()
        return render_template('welcome.html', club=club, competitions=competitions, today=today, datetime=datetime)
    else:
        today = date.today()
        error_message = 'Error - Email not found.'
    return render_template('index.html', error_message=error_message,today=today, datetime=datetime)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = next((c for c in clubs if c['name'] == club), None)
    foundCompetition = next((c for c in competitions if c['name'] == competition), None)

    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong - please try again", "error")
        return render_template('erreure.html')


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    today = date.today()
    competition_name = request.form['competition']
    club_name = request.form['club']
    places_required = int(request.form['places'])

    # Recherche de la compétition et du club dans les données existantes
    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)

    # Vérification si la compétition et le club existent
    if competition is None or club is None:
        flash('Error - Competition or club not found!')
        return render_template('welcome.html', club=club, competitions=competitions, datetime=datetime.now(), today=today)

    # Vérification du nombre de places disponibles
    current_places = int(competition['numberOfPlaces'])
    if places_required <= 0 or places_required > current_places:
        flash('Error - Invalid number of places requested!')
        return render_template('welcome.html', club=club, competitions=competitions, datetime=datetime.now(), today=today)

    # Conversion de la valeur des points du club en entier
    club_points = int(club['points'])

    # Vérification du nombre de points disponibles du club
    if club_points < places_required:
        flash('Error - Insufficient points!')
        return render_template('welcome.html', club=club, competitions=competitions, datetime=datetime.now(), today=today)

    # Vérification si le nombre total de places demandées dépasse la limite
    if places_required > 12:
        flash('Error - Maximum 12 places can be booked at once!')
        return render_template('welcome.html', club=club, competitions=competitions, datetime=datetime.now(), today=today)

    # Vérification si le nombre total de places demandées plus les places déjà vendues ne dépasse pas la limite
    if places_required + (12 - current_places) > 12:
        flash('Error - Maximum 12 places can be booked for this competition!')
        return render_template('welcome.html', club=club, competitions=competitions, datetime=datetime.now(), today=today)

    # Mise à jour du nombre de places après l'achat
    competition['numberOfPlaces'] = current_places - places_required

    # Mise à jour du nombre de points disponibles du club
    club['points'] = club_points - places_required

    flash('Great - Booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions, datetime=datetime.now(), today=today)

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))