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
                "1A": ((2, "2D", 0), (4, "3D", 0)),
                "2D": ((0, "1A", 2), (2, "4A", 1),
                       (3, "7A", 0), (4, "8A", 2)),
                "3D": ((0, "1A", 4), (2, "4A", 3),
                       (3, "7A", 2), (4, "8A", 4)),
                "4A": ((1, "2D", 2), (2, "5D", 0), (3, "3D", 2)),
                "5D": ((0, "4A", 2), (1, "7A", 1), (2, "8A", 3)),
                "6D": ((1, "8A", 0),),
                "7A": ((0, "2D", 3), (1, "5D", 1), (2, "3D", 3)),
                "8A": ((0, "6D", 1), (2, "2D", 4),
                       (3, "5D", 2), (4, "3D", 4))
            }
        else:
            self.intersect_constraints = intersect_constraints

        self.domains = {
            variable: tuple(word for word in self.words if len(word) == self.length_constraints[variable])
            for variable in self.variables
        }

    def check_intersect_constraints(self, assignment: dict[str, str]) -> bool:
        only_assigned = {k: v for k, v in assignment.items() if v != ""}

        for variable, assigned_value in only_assigned.items():
            for first_var_index, intersecting_var, inter_var_index in self.intersect_constraints[variable]:
                if intersecting_var in only_assigned and \
                        assigned_value[first_var_index] != only_assigned[intersecting_var][inter_var_index]:
                    return False

        return True

