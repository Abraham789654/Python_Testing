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


class TestCompetition(unittest.TestCase):
    def test_loadCompetitions(self):
        expected_competitions = [
            {"name": "Spring Festival", "date": "2024-03-27 10:00:00", "numberOfPlaces": "25"},
            {"name": "Fall Classic", "date": "2025-10-22 13:30:00", "numberOfPlaces": "13"},
        ]
        actual_competitions =loadCompetitions('competitions.json')
        self.assertEqual(sorted(actual_competitions, key=lambda x: x['name']), sorted(expected_competitions, key=lambda x: x['name']))

if __name__ == '__main__':
     unittest.main()