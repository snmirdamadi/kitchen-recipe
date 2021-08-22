from django.test import TestCase
from app.calc import add, subtract

class CalcTest(TestCase):

    def test_and_numbers(self):
        """Test that numbers are added together"""
        self.assertEqual(add(3,8), 11)


    def test_subtract_numbers(self):
        """Test That numbers are subtracted"""
        self.assertEqual(subtract(5, 11), 6)
