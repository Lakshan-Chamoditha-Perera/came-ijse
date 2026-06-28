# scale, vector multiplication
# return vrector multiplied by a scalar

vector = [1, 2, 3]
scalar = 5.2


def multiply_vector(vector, scalar):
    try:
        if vector is None or scalar is None:
            raise ValueError("Vector and scalar must not be None")
        if not isinstance(vector, list):
            raise TypeError("Vector must be a list")
        if not all(isinstance(x, (int, float)) for x in vector):
            raise TypeError("All elements of the vector must be numbers")

        return list(map(lambda x: x * scalar, vector))

    except Exception as error:
        print("An error occurred: " + str(error))
        return None


print("Vector:", vector)
multiplied_vector = multiply_vector(vector, scalar)
print("Multiplied Vector:", multiplied_vector)
