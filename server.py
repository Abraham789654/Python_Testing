import json
from flask import Flask,render_template,request,redirect,flash,url_for


# def loadClubs():
#     with open('clubs.json') as c:
#          listOfClubs = json.load(c)['clubs']
#          return listOfClubs


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
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    email = request.form['email']
    club = next((club for club in clubs if club['email'] == email), None)
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        error_message = 'Error - Email not found.'
        return render_template('index.html', error_message=error_message)


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
    
    if  places_required == 12 :
        flash('Info - You cannot buy more than 12 places!')
        return render_template('welcome.html', club=club, competitions=competitions)


    # Mise à jour du nombre de places après l'achat
    competition['numberOfPlaces'] = current_places - places_required

    flash('Great - Booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))