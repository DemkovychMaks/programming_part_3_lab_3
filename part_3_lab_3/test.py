import unittest
from main import Hamster


class TestGreddy(unittest.TestCase):

    def test_case_1(self):
        input_file_1 = "ex_1.txt"
        self.assertEqual(Hamster.find_amount_of_hamsters(input_file_1), 2)

    def test_case_2(self):
        input_file_2 = "ex_2.txt"
        self.assertEqual(Hamster.find_amount_of_hamsters(input_file_2), 3)

    def test_case_3(self):
        input_file_3 = "ex_3.txt"
        self.assertEqual(Hamster.find_amount_of_hamsters(input_file_3), 1)
