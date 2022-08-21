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

    def test_check_intersect_constraints(self):
        env = CrossWorldEnv()
        # the constraint is 1A[2] == 2D[0]
        assignment = {'1A': 'LASER', '2D': 'SAILS'}
        self.assertTrue(env.check_intersect_constraints(assignment))

        assignment = {'1A': 'LASER', '2D': 'NAILS'}
        self.assertFalse(env.check_intersect_constraints(assignment))

    if __name__ == '__main__':
        unittest.main()