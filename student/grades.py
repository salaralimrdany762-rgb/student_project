# Functions for working with a student's grades


def avg(grades):
    """Return the average of the grades."""
    return sum(grades) / len(grades)


def max_grade(grades):
    """Return the highest grade."""
    return max(grades)


def min_grade(grades):
    """Return the lowest grade."""
    return min(grades)
