from typing import Tuple, Dict, Optional


class CrossWorldEnv:
    def __init__(self, words: Optional[Tuple[str]] = None,
                 variables: Optional[Tuple[str]] = None,
                 length_constraints: Optional[Dict[str, int]] = None,
                 intersect_constraints: Optional[Dict[str, Tuple]] = None):
        if words is None:
            self.words = (
                "AFT", "ALE", "EEL", "HEEL",
                "HIKE", "HOSES", "KEEL", "KNOT",
                "LASER", "LEE", "LINE", "SAILS",
                "SHEET", "STEER", "TIE"
            )
        else:
            self.words = words

        if variables is None:
            self.variables = (
                "1A", "2D", "3D", "4A",
                "5D", "6D", "7A", "8A"
            )
        else:
            self.variables = variables

        if length_constraints is None:
            self.length_constraints = {
                "1A": 5, "2D": 5, "3D": 5, "4A": 4,
                "5D": 4, "6D": 3, "7A": 3, "8A": 5
            }
        else:
            self.length_constraints = length_constraints

        if intersect_constraints is None:
            self.intersect_constraints = {
                "1A": (("1A", 2, "2D", 0), ("1A", 4, "3D", 0)),
                "2D": (("2D", 0, "1A", 2), ("2D", 2, "4A", 1),
                       ("2D", 3, "7A", 0), ("2D", 4, "8A", 2)),
                "3D": (("3D", 0, "1A", 4), ("3D", 2, "4A", 3),
                       ("3D", 3, "7A", 2), ("3D", 4, "8A", 4)),
                "4A": (("4A", 1, "2D", 2), ("4A", 2, "5D", 0), ("4A", 3, "3D", 2)),
                "5D": (("5D", 0, "4A", 2), ("5D", 1, "7A", 1), ("5D", 2, "8A", 3)),
                "6D": (("6D", 1, "8A", 0)),
                "7A": (("7A", 0, "2D", 3), ("7A", 1, "5D", 1), ("7A", 2, "3D", 3)),
                "8A": (("8A", 0, "6D", 1), ("8A", 2, "2D", 4),
                       ("8A", 3, "5D", 2), ("8A", 4, "3D", 4))
            }
        else:
            self.intersect_constraints = intersect_constraints

        self.domains = {
            variable: tuple(word for word in self.words if len(word) == self.length_constraints[variable])
            for variable in self.variables
        }
