import unittest
from unittest.mock import patch
from server import app

class TestLogout(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_logout_redirect(self):
        with self.app as client:
            response = client.get('/logout')
            # Assurez-vous que la réponse renvoie un code de redirection
            self.assertEqual(response.status_code, 302)
            # Assurez-vous que la redirection est effectuée vers la page d'accueil
            self.assertEqual(response.location, 'http://localhost/')

if __name__ == '__main__':
    unittest.main()
