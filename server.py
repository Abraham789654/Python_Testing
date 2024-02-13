import json
from flask import Flask, render_template, request, redirect, flash, url_for

def load_clubs():
    """
    Charge la liste des clubs depuis le fichier JSON.
    """
    with open('clubs.json', encoding='utf-8') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs

def load_competitions():
    """
    Charge la liste des compétitions depuis le fichier JSON.
    """
    with open('competitions.json', encoding='utf-8') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()

@app.route('/')
def index():
    """
    Affiche la page d'accueil.
    """
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def show_summary():
    """
    Affiche un résumé des informations pour un club donné.
    """
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/book/<competition>/<club>')
def book(competition, club):
    """
    Réserve une place pour une compétition pour un club donné.
    """
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong - please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    """
    Achète des places pour une compétition donnée.
    """
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    flash('Great - Booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display

@app.route('/logout')
def logout():
    """
    Redirige vers la page d'accueil.
    """
    return redirect(url_for('index'))
