import numpy as np


def calculate_sigmoid(x):
    return 1 / (1 + np.exp(-x))


print(f"Sigmoid of 0: {calculate_sigmoid(0)}")
print(f"Sigmoid of 10: {calculate_sigmoid(10)}")
print(f"Sigmoid of possitive infinity: {calculate_sigmoid(np.inf)}")
print(f"Sigmoid of -10: {calculate_sigmoid(-10)}")
print(f"Sigmoid of negative infinity: {calculate_sigmoid(-np.inf)}")
