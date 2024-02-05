import unittest
import json
from server import loadClubs
from server import loadCompetitions
from unittest.mock import patch
from server import app, showSummary
from flask import Response 
from server import book 
from flask import  flash
from server import app, competitions, clubs


class TestBook(unittest.TestCase):
    @patch('server.render_template')
    @patch('server.flash')
    def test_book_success(self, mock_flash, mock_render_template):
        # Mock des données
        clubs = [{'name': 'Club1'}, {'name': 'Club2'}]
        competitions = [{'name': 'Competition1'}, {'name': 'Competition2'}]

        # Exécution de la fonction
        with patch('server.clubs', clubs), patch('server.competitions', competitions):
            result = book('Competition1', 'Club1')

        # Vérification des appels de fonction et des arguments passés
        mock_render_template.assert_called_once_with('booking.html', club=clubs[0], competition=competitions[0])
        mock_flash.assert_not_called()  # Aucun message flash d'erreur

        # Ajoutez d'autres assertions si nécessaire pour vérifier le résultat de la fonction

    @patch('server.render_template')
    @patch('server.flash')
    def test_book_failure(self, mock_flash, mock_render_template):
        # Mock des données
        clubs = [{'name': 'Club1'}, {'name': 'Club2'}]
        competitions = [{'name': 'Competition1'}, {'name': 'Competition2'}]

        # Exécution de la fonction avec des données qui ne correspondent pas
        with patch('server.clubs', clubs), patch('server.competitions', competitions):
            result = book('InvalidCompetition', 'InvalidClub')

        # Vérification des appels de fonction et des arguments passés
        mock_render_template.assert_called_once_with('erreure.html')  # Redirigé vers la page d'erreur
        mock_flash.assert_called_once_with("Something went wrong - please try again", "error")

        # Ajoutez d'autres assertions si nécessaire pour vérifier le résultat de la fonction

if __name__ == '__main__':
    unittest.main()