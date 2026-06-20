# Write a function that returns True only when all of the following conditions are met:
# - age is a string that can be converted to an integer greater than 18
# - income is a number greater than 0
# - email is a non-empty string after .strip() is called on it
# - is_active is True
# - notes is None

age = "42"
income = 0
email = ""
is_active = False
notes = None


def is_training_ready():
    try:
        age_int = int(age)
    except ValueError:
        return False

    if (
        age_int <= 18
        or income <= 0
        or not email.strip()
        or not is_active
        or notes is not None
    ):
        return False

    return True
