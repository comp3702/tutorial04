# Constraint Satisfaction Problem (CSP)

Again, different from the official solutions:

- fixes many weird design choices
- adds non-repeat condition in recursive backtracking algo
- adds a [random crossword](docs/investigations-crossword-puzzle-answers.pdf) puzzle from [printable crossword puzzles](https://www.englishhints.com/printable-crossword-puzzles.html)

### Dependencies
Python 3.10, but it should work with any 3.x.
There are some extra dependencies (e.g. matplotlib, networkx), there is [environment.yml](environment.yml).

To create/restore the environment:

    conda env create -f environment.yml

To update the file:

    conda env export > environment.yml

### Running
Again, the intended use is through the unittests located in `tests` that can be run either from an IDE or command line:

    python -m unittest discover -s tests -t tests

There's also main.py that can be used as a playground and can be run like this:

    python main.py