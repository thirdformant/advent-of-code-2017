import unittest
import advent_of_code.day1 as day1

class Day1Tests(unittest.TestCase):

    def test_next_sum_matches(self):
        self.assertTrue(day1.sum_matches('1122', 1) == 3,
                        msg='Sum of matching digits of 1122 != 3')

        self.assertTrue(day1.sum_matches('1111', 1) == 4,
                        msg='Sum of matching digits of 1111 != 4')

        self.assertTrue(day1.sum_matches('1234', 1) == 0,
                        msg='Sum of matching digits of 1234 != 0')

        self.assertTrue(day1.sum_matches('91212129', 1) == 9,
                        msg='Sum of matching digits of 91212129 != 9')

    def test_half_sum_matches(self):
        self.assertTrue(day1.sum_matches('1212', int(len('1212')/2)) == 6,
                        msg='Sum of matching digits of 1212 != 6')

        self.assertTrue(day1.sum_matches('1221', int(len('1221')/2)) == 0,
                        msg='Sum of matching digits of 1221 != 0')

        self.assertTrue(day1.sum_matches('123425', int(len('123425')/2)) == 4,
                        msg='Sum of matching digits of 123425 != 4')

        self.assertTrue(day1.sum_matches('123123', int(len('123123')/2)) == 12,
                        msg='Sum of matching digits of 123123 != 12')

        self.assertTrue(day1.sum_matches('12131415', int(len('12131415')/2)) == 4,
                        msg='Sum of matching digits of 12131415 != 4')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
