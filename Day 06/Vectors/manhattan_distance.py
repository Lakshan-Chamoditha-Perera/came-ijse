a = [1, -1, 3]
b = [3, 2, -2]


def manhatton_distance(v1, v2):
    try:
        if len(v1) != len(v2):
            print("Vectors must be of the same length")
            raise ValueError("Vectors must be of the same length")

        # sum = 0;
        # for i in range(len(v1)):
        #     sum += abs(v1[i]-v2[i])
        # return sum;

        return sum(abs(v1[i] - v2[i]) for i in range(len(v1)))

    except Exception as error:
        print("An error occurred: " + str(error))
        return None


l2_distance_value = manhatton_distance(a, b)
print(f"L2 distance : {l2_distance_value:.2f}")
