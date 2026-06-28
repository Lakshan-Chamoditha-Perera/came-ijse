def vector_magnitude(vector):
    print("Vector:", vector)
    try:
        if vector is None:
            raise ValueError("Vector must not be None")
        if not isinstance(vector, list):
            raise TypeError("Vector must be a list")
        if not all(isinstance(x, (int, float)) for x in vector):
            raise TypeError("All elements of the vector must be numbers")

        magnitude = sum(x**2 for x in vector) ** 0.5
        print(f"Magnitude:  {magnitude:.3}\n")
        return magnitude

    except Exception as error:
        print("An error occurred: " + str(error))
        return None


vector_magnitude([1, 2, 5])
vector_magnitude([-1, -2, 2])
