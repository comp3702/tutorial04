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

    # def test_rb_hard(self):
    #     env = CrossWorldEnv(
    #         ('infer', 'observe', 'examine', 'revealed', 'inconceivable',
    #          'aspects', 'link', 'detective', 'inquisitive', 'inspect', 'conclude', 'inquiry',
    #          'analyze', 'mental', 'deduce', 'investigate'),
    #         (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
    #         {}
    #     )