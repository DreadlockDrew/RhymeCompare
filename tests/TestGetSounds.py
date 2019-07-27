import unittest
from rhymes import RhymingDictionary

class TestGetSounds(unittest.TestCase):

    def testGoodCase(self):
        fileName='data/cmudict-0.7b'

        self.assertEqual(RhymingDictionary.getSounds(fileName,'ORANGE'),['AO1', 'R', 'AH0', 'N', 'JH'])

    def testLowerCase(self):
        fileName='data/cmudict-0.7b'
        self.assertEqual(RhymingDictionary.getSounds(fileName,'bab'),['B', 'AE1', 'B'])

    def testFailedCase(self):
        fileName='data/cmudict-0.7b'
        self.assertEqual(RhymingDictionary.getSounds(fileName,'NUINFQO'),[])





if __name__ == '__main__':
    unittest.main()