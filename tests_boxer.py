import unittest
import boxer


class TestBoxer(unittest.TestCase):
    def test_SergeyCovalevAgeRight(self):
        self.assertEqual(boxer.SergeyCovalev.age, 33)

    def test_HennadiyGolovkinWeightRight(self):
        self.assertEqual(boxer.HennadiyGolovkin.weight, 72)

    def test_SaulAlvarezHeightRight(self):
        self.assertEqual(boxer.SaulAlvarez.height, 182)

    def test_SaulAlvarezHeightComputeRight(self):
        self.assertEqual(boxer.SaulAlvarez.height, 5 - 3 + 50 * 2 + 160 / 2)

    def test_SaulAlvarezWeightComputeWrong(self):
        self.assertEqual(boxer.SaulAlvarez.weight, 100 + 31)

    def test_HennadiyGolovkinAgeWrong(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, 25)

    def test_SaulAlvarezWeightWrong(self):
        self.assertEqual(boxer.SaulAlvarez.weight, 55)

    def test_SergeyCovalevHeightWrong(self):
        self.assertEqual(boxer.SergeyCovalev.height, 181)

    def test_SergeyCovalevAgeEmpty(self):
        self.assertEqual(boxer.SergeyCovalev.age, '')

    def test_HennadiyGolovkinWeightEmpty(self):
        self.assertEqual(boxer.HennadiyGolovkin.weight, '')

    def test_SaulAlvarezHeightEmpty(self):
        self.assertEqual(boxer.SaulAlvarez.height, '')

    def test_SaulAlvarezAgeZero(self):
        self.assertEqual(boxer.SaulAlvarez.age, 0)

    def test_SergeyCovalevAgeMinus(self):
        self.assertEqual(boxer.SergeyCovalev.age, -33)

    def test_HennadiyGolovkinHeigtLettersLatin(self):
        self.assertEqual(boxer.HennadiyGolovkin.height, 'one hundred eighty five')

    def test_SergeyCovalevAgeString(self):
        self.assertEqual(boxer.SergeyCovalev.age, '33')







