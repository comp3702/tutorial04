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

    # see docs/investigation-words-cross-word-puzzle.pdf
    def test_rb_hard(self):
        env = CrossWorldEnv(
            ('infer', 'observe', 'examine', 'revealed', 'inconceivable',
             'aspects', 'link', 'detective', 'inquisitive', 'inspect', 'conclude', 'inquiry',
             'analyze', 'mental', 'deduce', 'investigate'),
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
            {1: 11, 2: 7, 3: 6, 4: 9, 5: 13, 6: 7, 7: 7, 8: 8, 9: 11, 10: 7, 11: 5, 12: 4, 13: 7, 14: 7, 15: 6, 16: 8},
            {
                1: ( (1, 2, 1), (4, 5, 7), (10, 9, 10) ),
                2: ( (1, 1, 1), ),
                3: ((4, 6, 0), ),
                4: ((1, 5, 12), ),
                5: ((7, 1, 4), (12, 4, 1)),
                6: ((0, 3, 4), (6, 7, 0)),
                7: ((0, 6, 6), (4, 9, 6), (6, 14, 6)),
                8: ( (1, 9, 3), (3, 14, 3), (7, 16, 6)),
                9: ( (3, 8, 1), (6, 7, 4), (8, 10, 0), (10, 1, 10) ),
                10: ( (0, 9, 8), (3, 15, 1) ),
                11: ( (3, 15, 5), ),
                12: ( (1, 13, 0), ),
                13: ( (0, 12, 1), (5, 16, 0) ),
                14: ( (3, 8, 3), (6, 7, 6) ),
                15: ( (1, 10, 3), (5, 11, 3) ),
                16: ( (0, 13, 5), )
            }
        )

        assignments = {variable: '' for variable in env.variables}
        result, expanded = recursive_backtracking(env, assignments, 0)
        print(f"Expanded: {expanded}")
        print(result)
        
        # the official solution doesn't have a condition for non-repeat so both 2 and 13 get inspect
        # although the actual solution has inquiry in 2 (see docs/investigation-crossword-puzzle-answers.pdf)
        self.assertEqual('inquiry', result[2])
