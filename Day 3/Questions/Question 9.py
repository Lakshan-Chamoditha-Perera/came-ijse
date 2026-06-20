labels = ["cat", "dog", "bird", "cat", "fish", "dog", "cat"]

first_three_labels = labels[:3]
print(f"First three labels: {first_three_labels}")

last_two_labels = labels[-2:]
print(f"Last two labels: {last_two_labels}")

every_second_label = labels[::2]
print(f"Every second label: {every_second_label}")

reversed_middle_labels = labels[1:-1][::-1]
print(f"Reversed middle labels: {reversed_middle_labels}")
