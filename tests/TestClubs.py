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




class TestClubs(unittest.TestCase):
    def test_loadClubs(self):
        expected_clubs = [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"},
            {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "18"},
            {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "30"},
            
        ]
        actual_clubs = loadClubs('clubs.json')
        self.assertEqual(sorted(actual_clubs, key=lambda x: x['name']), sorted(expected_clubs, key=lambda x: x['name']))

if __name__ == '_main_':
     unittest.main()