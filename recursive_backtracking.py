from CrossWorldEnv import CrossWorldEnv


def recursive_backtracking(env: CrossWorldEnv, assignments: dict[str, str], expanded: int = 0) -> (dict, int):
    unassigned_variables = {variable for variable in assignments if assignments[variable] == ""}

    if len(unassigned_variables) == 0:
        return assignments, expanded

    unassigned = unassigned_variables.pop()
    for word in env.domains[unassigned]:
        # this is missing in official solutions and will fail the 2nd test in test_recursive_backtracking
        if word in assignments.values():
            continue

        assignments[unassigned] = word

        if not env.check_intersect_constraints(assignments):
            continue

        result, expanded = recursive_backtracking(env, assignments.copy(), expanded + 1)
        if result is not None:
            return result, expanded

    return None, expanded
