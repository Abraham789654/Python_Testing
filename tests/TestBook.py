import unittest
from unittest.mock import patch
from server import book

class TestBook(unittest.TestCase):
    """
    Test cases for the book function.
    """

    @patch('server.render_template')
    @patch('server.flash')
    def test_book_success(self, mock_flash, mock_render_template):
        """
        Test case for successful booking.
        """
        # Mock des données
        clubs_data = [{'name': 'Club1'}, {'name': 'Club2'}]
        competitions_data = [{'name': 'Competition1'}, {'name': 'Competition2'}]

        # Exécution de la fonction
        with patch('server.clubs', clubs_data), patch('server.competitions', competitions_data):
             book('Competition1', 'Club1')

        # Vérification des appels de fonction et des arguments passés
        mock_render_template.assert_called_once_with('booking.html', club=clubs_data[0],
                                                      competition=competitions_data[0])
        mock_flash.assert_not_called()  # Aucun message flash d'erreur

        # Ajoutez d'autres assertions si nécessaire pour vérifier le résultat de la fonction

    @patch('server.render_template')
    @patch('server.flash')
    def test_book_failure(self, mock_flash, mock_render_template):
        """
        Test case for failed booking.
        """
        # Mock des données
        clubs_data = [{'name': 'Club1'}, {'name': 'Club2'}]
        competitions_data = [{'name': 'Competition1'}, {'name': 'Competition2'}]

        # Exécution de la fonction avec des données qui ne correspondent pas
        with patch('server.clubs', clubs_data), patch('server.competitions', competitions_data):
             book('InvalidCompetition', 'InvalidClub')

        # Vérification des appels de fonction et des arguments passés
        mock_render_template.assert_called_once_with('erreur.html')  # Redirigé vers la page d'erreur
        mock_flash.assert_called_once_with("Something went wrong - please try again", "error")

        # Ajoutez d'autres assertions si nécessaire pour vérifier le résultat de la fonction

if __name__ == '__main__':
    unittest.main()
