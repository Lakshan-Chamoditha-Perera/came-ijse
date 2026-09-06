# 2nd row
# 3rd column
# 2nd row to below
# specific

import numpy as np

array = np.array(
    [
        [1, 9, 5, 8],
        [4, 5, 3, 6],
        [6, 5, 4, 10],
    ]
)

print(f"Second row: {array[1, :]} \n")
print(f"Third col : {array[:, 2]} \n")
print(f"2nd row to below: {array[1:]} \n")
print(f"Specific : {array[:2, 1:]} \n \n")

c = np.array([[1, 2], [3, 4]])
d = np.array([[1, 2], [1, 2]])

print(c * d)
