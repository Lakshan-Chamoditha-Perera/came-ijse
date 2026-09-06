"""Question 5 - Model registry with class variables."""


class Model:
    """A registered model that reads the framework from the class variable."""

    framework = "CAME-ML"

    def __init__(self, name):
        """Store the model name on the instance."""
        self.name = name


def main():
    """Register each model line and print its name and current framework."""
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

        if stripped.startswith("FRAMEWORK "):
            Model.framework = stripped[len("FRAMEWORK ") :].strip()
            continue

        model = Model(stripped)
        print(model.name + "|" + Model.framework)


if __name__ == "__main__":
    main()
