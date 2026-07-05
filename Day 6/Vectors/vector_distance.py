import math

a = [1, -1, 3]
b = [3, 2, -2]


def distance(v1, v2):
    try:
        if len(v1) != len(v2):
            print("Vectors must be of the same length")
            raise ValueError("Vectors must be of the same length")

        # sum_vector = []
        # for i in range(len(v1)):
        #     sum_vector.append((v1[i] - v2[i]) ** 2)
        # return sum(sum_vector) ** 0.5
        return math.sqrt(sum((v1[i] - v2[i]) ** 2 for i in range(len(v1))))

    except Exception as error:
        print("An error occurred: " + str(error))
        return None


distance_value = distance(a, b)
print(f"Difference : {distance_value:.2f}")
