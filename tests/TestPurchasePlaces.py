import unittest
from server import app, competitions

class TestPurchasePlaces(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_purchasePlaces(self):
        # Données fictives pour la requête POST
        data = {
            'competition': 'Spring Festival',
            'club': 'Iron Temple',
            'places': '2'
        }

        # Obtention du nombre de places avant la réservation
        competition_before_booking = next((c for c in competitions 
                                           if c['name'] == data['competition']), None)
        places_before_booking = int(competition_before_booking['numberOfPlaces'])

        # Appel de la route purchasePlaces avec les données fictives de test
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)

        # Club et compétition après l'achat
        competition_after_booking = next((c for c in competitions if c['name']
                                           == data['competition']), None)

        # Mise à jour du nombre de places
        places_after_booking = int(competition_after_booking['numberOfPlaces'])
        self.assertEqual(places_after_booking, places_before_booking - int(data['places']))

        # Vérifier si un message flash est présent
        self.assertIn(b'Great - Booking complete!', response.data)

        # Vérifier si welcome renvoie les bonnes données
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
