# Write a function that takes two vectors as input and returns their sum.
# The function should handle cases where the vectors are of different lengths by raising an exception.

v = [1, 2, 3]
w = [4, 5, 6]


def sum_vectors(vector1, vector2):
    try:
        if len(vector1) != len(vector2):
            print("Vectors must be of the same length")
            raise ValueError("Vectors must be of the same length")
        # return [vector1[i] + vector2[i] for i in range(len(vector1))]
        sum_vector = []
        for i in range(len(vector1)):
            sum_vector.append(vector1[i] + vector2[i])
        return sum_vector

    except Exception as error:
        print("An error occurred: " + str(error))
        return None


sum_vector = sum_vectors(v, w)
print(sum_vector)
