"""Question 2 - Review routing with watchlist override."""


def main():
    """Read data rows and print a priority for each one."""
    watchlist = set()  # Watchlisted labels; the last WATCHLIST line wins.

    while True:
        try:
            line = input()
        except EOFError:
            break

        # Ignore blank lines.
        if line.strip() == "":
            continue

        # Ignore comment lines whose first non-space character is '#'.
        if line.lstrip()[0] == "#":
            continue

        stripped = line.strip()

        # Configuration line: WATCHLIST a,b,c (comma-separated labels).
        if stripped.startswith("WATCHLIST"):
            labels = stripped[len("WATCHLIST") :].strip()
            watchlist = set(labels.split(",")) if labels else set()
            continue

        # Data row: label,confidence (label may contain spaces).
        label_part, conf_part = stripped.rsplit(",", 1)
        label = label_part.strip().lower()
        confidence = float(conf_part.strip())

        # Watchlist override takes precedence over the band rules.
        if label in watchlist:
            priority = "HIGH"
        elif confidence < 0.50 or label == "unknown":
            priority = "HIGH"
        elif confidence < 0.80:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        print(priority)


if __name__ == "__main__":
    main()
