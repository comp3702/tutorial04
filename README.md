# Constraint Satisfaction Problem (CSP)

Again, different from the official solutions:

- fixes many weird design choices
- adds non-repeat condition in recursive backtracking algo
- adds a random crossword puzzle from [printable crossword puzzles](https://www.englishhints.com/printable-crossword-puzzles.html)

### Dependencies
Python 3.10, but it should work with any 3.x.
There are some extra dependencies (e.g. matplotlib, networkx), there is [environment.yml](environment.yml).

To create/restore the environment:

    conda env create -f environment.yml

To update the file:

    conda env export > environment.yml
