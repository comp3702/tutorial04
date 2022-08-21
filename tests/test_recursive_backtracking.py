import unittest

from CrossWorldEnv import CrossWorldEnv
from recursive_backtracking import recursive_backtracking


class TestRecursiveBacktracking(unittest.TestCase):
    def test_recursive_backtracking(self):
        env = CrossWorldEnv()

        assignments = {variable: '' for variable in env.variables}
        result, expanded = recursive_backtracking(env, assignments, 0)
        print(f"Expanded: {expanded}")
        print(result)