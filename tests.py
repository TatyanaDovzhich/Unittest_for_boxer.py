import unittest
import boxer


class TestBoxerPositive(unittest.TestCase):
    def test_SergeyCovalev(self):
        self.assertEqual(boxer.SergeyCovalev.age, 33)
        self.assertEqual(boxer.SergeyCovalev.weight, 78)
        self.assertEqual(boxer.SergeyCovalev.height, 180)

    def test_HennadiyGolovkin(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, 28)
        self.assertEqual(boxer.HennadiyGolovkin.weight, 72)
        self.assertEqual(boxer.HennadiyGolovkin.height, 185)

    def test_SaulAlvarez(self):
        self.assertEqual(boxer.SaulAlvarez.age, 35)
        self.assertEqual(boxer.SaulAlvarez.weight, 69)
        self.assertEqual(boxer.SaulAlvarez.height, 182)


class TestBoxerNegativeSergeyCovalev(unittest.TestCase):
    def test_SergeyCovalev1(self):
        self.assertEqual(boxer.SergeyCovalev.age, 33)
        self.assertEqual(boxer.SergeyCovalev.weight, 78)
        self.assertEqual(boxer.SergeyCovalev.height, 190)

    def test_SergeyCovalev2(self):
        self.assertEqual(boxer.SergeyCovalev.age, 33)
        self.assertEqual(boxer.SergeyCovalev.weight, 76)
        self.assertEqual(boxer.SergeyCovalev.height, 190)

    def test_SergeyCovalev3(self):
        self.assertEqual(boxer.SergeyCovalev.age, 30)
        self.assertEqual(boxer.SergeyCovalev.weight, 76)
        self.assertEqual(boxer.SergeyCovalev.height, 190)

    def test_SergeyCovalev4(self):
        self.assertEqual(boxer.SergeyCovalev.age, '')
        self.assertEqual(boxer.SergeyCovalev.weight, 78)
        self.assertEqual(boxer.SergeyCovalev.height, 180)

    def test_SergeyCovalev5(self):
        self.assertEqual(boxer.SergeyCovalev.age, 33)
        self.assertEqual(boxer.SergeyCovalev.weight, '')
        self.assertEqual(boxer.SergeyCovalev.height, 180)

    def test_SergeyCovalev6(self):
        self.assertEqual(boxer.SergeyCovalev.age, 33)
        self.assertEqual(boxer.SergeyCovalev.weight, 78)
        self.assertEqual(boxer.SergeyCovalev.height, '')

    def test_SergeyCovalev7(self):
        self.assertEqual(boxer.SergeyCovalev.age, '')
        self.assertEqual(boxer.SergeyCovalev.weight, '')
        self.assertEqual(boxer.SergeyCovalev.height, '')

class TestBoxerNegativeHennadiyGolovkin(unittest.TestCase):
    def test_HennadiyGolovkin1(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, 28)
        self.assertEqual(boxer.HennadiyGolovkin.weight, 72)
        self.assertEqual(boxer.HennadiyGolovkin.height, 180)

    def test_HennadiyGolovkin2(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, 28)
        self.assertEqual(boxer.HennadiyGolovkin.weight, 70)
        self.assertEqual(boxer.HennadiyGolovkin.height, 170)

    def test_HennadiyGolovkin3(self):
            self.assertEqual(boxer.HennadiyGolovkin.age, 30)
            self.assertEqual(boxer.HennadiyGolovkin.weight, 70)
            self.assertEqual(boxer.HennadiyGolovkin.height, 170)

    def test_HennadiyGolovkin4(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, '')
        self.assertEqual(boxer.HennadiyGolovkin.weight, 72)
        self.assertEqual(boxer.HennadiyGolovkin.height, 185)

    def test_HennadiyGolovkin5(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, 28)
        self.assertEqual(boxer.HennadiyGolovkin.weight, '')
        self.assertEqual(boxer.HennadiyGolovkin.height, 185)

    def test_HennadiyGolovkin6(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, 28)
        self.assertEqual(boxer.HennadiyGolovkin.weight, 72)
        self.assertEqual(boxer.HennadiyGolovkin.height, '')

    def test_HennadiyGolovkin7(self):
        self.assertEqual(boxer.HennadiyGolovkin.age, '')
        self.assertEqual(boxer.HennadiyGolovkin.weight, '')
        self.assertEqual(boxer.HennadiyGolovkin.height, '')

class TestBoxerNegativeSaulAlvarez(unittest.TestCase):
    def test_SaulAlvarez1(self):
        self.assertEqual(boxer.SaulAlvarez.age, 35)
        self.assertEqual(boxer.SaulAlvarez.weight, 69)
        self.assertEqual(boxer.SaulAlvarez.height, 175)

    def test_SaulAlvarez2(self):
        self.assertEqual(boxer.SaulAlvarez.age, 35)
        self.assertEqual(boxer.SaulAlvarez.weight, 55)
        self.assertEqual(boxer.SaulAlvarez.height, 175)

    def test_SaulAlvarez3(self):
        self.assertEqual(boxer.SaulAlvarez.age, 38)
        self.assertEqual(boxer.SaulAlvarez.weight, 55)
        self.assertEqual(boxer.SaulAlvarez.height, 175)

    def test_SaulAlvarez4(self):
        self.assertEqual(boxer.SaulAlvarez.age, '')
        self.assertEqual(boxer.SaulAlvarez.weight, 69)
        self.assertEqual(boxer.SaulAlvarez.height, 182)

    def test_SaulAlvarez5(self):
        self.assertEqual(boxer.SaulAlvarez.age, 35)
        self.assertEqual(boxer.SaulAlvarez.weight, '')
        self.assertEqual(boxer.SaulAlvarez.height, 182)

    def test_SaulAlvarez6(self):
        self.assertEqual(boxer.SaulAlvarez.age, 35)
        self.assertEqual(boxer.SaulAlvarez.weight, 69)
        self.assertEqual(boxer.SaulAlvarez.height, '')

    def test_SaulAlvarez7(self):
        self.assertEqual(boxer.SaulAlvarez.age, '')
        self.assertEqual(boxer.SaulAlvarez.weight, '')
        self.assertEqual(boxer.SaulAlvarez.height, '')

class TestBoxerListEqual(unittest.TestCase):

    def test_List_SergeyCovalev_HennadiyGolovkin(self):
        self.assertListEqual(boxer.SergeyCovalev.boxerSC, 
boxer.HennadiyGolovkin.boxerHG, "The data is unique!")

    def test_List_SergeyCovalev_SaulAlvarez(self):
        self.assertListEqual(boxer.SergeyCovalev.boxerSC, 
boxer.SaulAlvarez.boxerSA, "The data is unique!")

    def test_List_HennadiyGolovkin_SaulAlvarez(self):
        self.assertListEqual(boxer.HennadiyGolovkin.boxerHG, 
boxer.SaulAlvarez.boxerSA, "The data is unique!")

