import unittest

from CrossWorldEnv import CrossWorldEnv
from arc_consistency import arc_consistency


class TestArcConsistency(unittest.TestCase):
    def test_arc_consistency(self):
        env = CrossWorldEnv()
        domains, constraint_checks = arc_consistency(env)

        print(domains)

        print(f"Number of arc constraint checks: {constraint_checks}")

        self.assertEqual(54, constraint_checks)