import unittest

from CrossWorldEnv import CrossWorldEnv


class TestCrossWorldEnv(unittest.TestCase):
    def test_init(self):
        env = CrossWorldEnv()
        self.assertEqual(15, len(env.words))
        self.assertEqual(8, len(env.variables))
        self.assertEqual(8, len(env.domains))

    def test_5_letter_domain(self):
        env = CrossWorldEnv()
        self.assertEqual(5, len(env.domains['1A']))

    def test_4_letter_domain(self):
        env = CrossWorldEnv()
        self.assertEqual(5, len(env.domains['4A']))
