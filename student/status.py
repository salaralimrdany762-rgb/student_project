# Checks whether the student passed or not


def check_status(average):
    """Return "ACC" if the average is more than 10, otherwise "REJ"."""
    if average > 10:
        return "ACC"
    else:
        return "REJ"
