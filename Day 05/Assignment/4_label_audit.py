"""Question 4 - Label ledger audit."""


def main():
    """Count distinct labels and detect duplicates, honoring directives."""
    labels = []
    fold = False
    bind_name = None

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

        if stripped.startswith("FOLD case"):
            fold = True
            continue

        if stripped.startswith("BIND duplicate "):
            bind_name = stripped[len("BIND duplicate ") :]
            continue

        labels.append(stripped)

    if fold:
        compared = [label.casefold() for label in labels]
    else:
        compared = [label for label in labels]

    counts = {}
    for label in compared:
        counts[label] = counts.get(label, 0) + 1

    if bind_name is not None:
        key = bind_name.casefold() if fold else bind_name
        if counts.get(key, 0) >= 2:
            print("unique=1")
            print("has_duplicates=yes")
            return

    unique = len(counts)
    has_duplicates = any(count > 1 for count in counts.values())

    print("unique=" + str(unique))
    print("has_duplicates=yes" if has_duplicates else "has_duplicates=no")


if __name__ == "__main__":
    main()
