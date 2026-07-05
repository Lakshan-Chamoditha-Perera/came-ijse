a = [-3, 4, -1]
b = [8, 0, 6]


def calculate_dotproduct(v1, v2):
    try:
        if len(v1) != len(v2):
            print("Vectors must be of the same length")
            raise ValueError("Vectors must be of the same length")

        # sum = 0
        # for i in range(len(v1)):
        #     sum += v1[i] * v2[i]
        # return sum

        return sum(v1[i] * v2[i] for i in range(len(v1)))

    except Exception as error:
        print("An error occurred: " + str(error))
        return None


dot_product = calculate_dotproduct(a, b)
print(f"Dot Product : {dot_product:.2f}")
