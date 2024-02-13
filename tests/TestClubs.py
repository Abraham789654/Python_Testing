import unittest
from server import loadClubs

class TestClubs(unittest.TestCase):
    """
    Test cases for the loadClubs function.
    """

    def test_load_clubs(self):
        """
        Test case for loading clubs.
        """
        expected_clubs = [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
            {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
            {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        ]
        actual_clubs = loadClubs('clubs.json')
        self.assertEqual(sorted(actual_clubs, key=lambda x: x['name']), 
                         sorted(expected_clubs, key=lambda x: x['name']))

if __name__ == '__main__':
    unittest.main()
