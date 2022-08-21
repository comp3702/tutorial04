from typing import Tuple

from CrossWorldEnv import CrossWorldEnv


def arc_consistency(env: CrossWorldEnv) -> Tuple[dict[str, Tuple[str, ...]], int]:
    constraint_checks = 0
    domains = env.domains.copy()

    # we are going from dict of {var: ( (constraint1), (constraint2)), ...}
    # to a list of constraints so the var now needs to be a part of the tuple
    container = [(variable,) + constraint for variable, constraints in env.intersect_constraints.items() for constraint in constraints]

    while container:
        constraint_checks += 1
        var1, index1, var2, index2 = container.pop(0)

        prior_len = len(domains[var1])
        # letters from var1's domain with index1
        avail_letters1 = set(word[index1] for word in domains[var1])
        # letters from var2's domain with index2
        avail_letters2 = set(word[index2] for word in domains[var2])
        # only keep those that appear in both sets
        result = avail_letters1.intersection(avail_letters2)

        # Only keep words with intersecting letters
        domains[var1] = tuple(word for word in domains[var1] if word[index1] in result)

        if not domains[var1]:  # No solution exists
            return None
        elif len(domains[var1]) != prior_len:
            # If domain changes, re-apply constraints for the rest of the constraints of this variable
            for child_index1, child_var2, child_index2 in env.intersect_constraints[var1]:
                if child_var2 != var2:
                    container.append((child_var2, child_index2, var1, child_index1))

    return domains, constraint_checks

