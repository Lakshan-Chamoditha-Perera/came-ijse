"""Question 3 - Training eligibility gate."""


def main():
    """Count samples that pass the eligibility rules and print the total."""
    allow_spam = False
    max_age = 65
    min_age = 18
    eligible = 0

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "":
            continue
        if line.lstrip()[0] == "#":
            continue

        stripped = line.strip()

        if stripped.startswith("ALLOW spam"):
            allow_spam = True
            continue

        if stripped.startswith("AGE max="):
            max_age = int(stripped[len("AGE max=") :].strip())
            continue

        parts = stripped.split("|")
        age = int(parts[0].strip())
        label = parts[1].strip().lower()
        score = parts[2].strip()
        country = parts[3].strip()
        is_premium = parts[4].strip().lower() == "true"
        has_missing = parts[5].strip().lower() == "true"

        age_ok = min_age <= age <= max_age
        label_ok = label != "spam" or allow_spam

        if score == "" or score.upper() == "NONE":
            score_ok = False
        else:
            score_ok = float(score) >= 0.60

        country_ok = country == "LK" or is_premium
        missing_ok = not has_missing

        if age_ok and label_ok and score_ok and country_ok and missing_ok:
            eligible += 1

    print(eligible)


if __name__ == "__main__":
    main()
