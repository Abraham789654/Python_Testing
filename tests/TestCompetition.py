"""
Test cases for the competition module.
"""

import unittest
from server import loadCompetitions

class TestCompetition(unittest.TestCase):
    """
    Test cases for the competition module.
    """

    def test_loadCompetitions(self):
        """
        Test case for loading competitions.
        """
        expected_competitions = [
            {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"},
            {"name": "Fall Classic", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"},
        ]
        actual_competitions = loadCompetitions('competitions.json')
        self.assertEqual(sorted(actual_competitions, key=lambda x: x['name']),
                          sorted(expected_competitions, key=lambda x: x['name']))

if __name__ == '__main__':
    unittest.main()
