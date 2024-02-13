"""
Test unitaire pour la fonction showSummary du module server.
"""

import unittest
from server import app

class TestShowSummary(unittest.TestCase):
    """
    Classe de test pour la fonction showSummary.
    """

    def setUp(self):
        """
        Configuration des tests.
        """
        app.config['TESTING'] = True
        self.app = app.test_client()  # Configuration du serveur de test

    def test_show_summary(self):
        """
        Test de la fonction showSummary.
        """
        data = {'email': 'admin@irontemple.com'} 
        response = self.app.post('/showSummary', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
