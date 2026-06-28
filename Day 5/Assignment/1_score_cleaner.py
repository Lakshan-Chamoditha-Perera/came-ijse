"""Question 1 - Metric cleaning with configuration lines."""


def main():
    """Read score lines, apply config rules, print the kept list and average."""
    scores = []
    threshold = None

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

        if stripped.startswith("DROP below="):
            threshold = float(stripped[len("DROP below=") :])
            continue

        try:
            value = float(stripped)
        except ValueError:
            print("Skipping invalid value: " + line)
            continue

        if threshold is not None and value < threshold:
            continue

        scores.append(value)

    kept = [score for score in scores]

    if not kept:
        print("No valid values")
    else:
        print(kept)
        print(round(sum(kept) / len(kept), 3))


if __name__ == "__main__":
    main()