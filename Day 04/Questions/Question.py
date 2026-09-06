# Write a python program to calculate a hypotenuse of a given right angle triangle.
# You should write this as a function with a return value. Also you should validate the inputs.

# import math


def calculate_hypotenuse(base: float, height: float) -> float:
    try:
        if float(base) <= 0 or float(height) <= 0:
            raise ValueError("Both sides must be positive numbers.")
        hypotenuse = (base**2 + height**2) ** 0.5
        # math.sqrt(base**2 + height**2) # can also use this method to get power of 0.5 or
        # math.hypot(base, height) # using this can calculate the hypotenuse directly
        print(
            f"The hypotenuse of the triangle with base {base} and height {height} is: {hypotenuse:.2f}"
        )
        return hypotenuse
    except ValueError as e:
        print(f"Error: {e}")
        return e


calculate_hypotenuse(5, 12)
calculate_hypotenuse(-5, 12)
calculate_hypotenuse(3, 4)
