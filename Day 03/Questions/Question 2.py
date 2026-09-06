raw_lables = [
    " Positive ",
    "NEGATIVE",
    "neutral",
    "positive",
    " Negative ",
    "pos",
    " negative ",
]

valid_labels = ["positive", "negative"]
clean_labels = []
rejected_count = 0


for label in raw_lables:
    cleaned_label = label.strip().lower()
    if cleaned_label not in valid_labels:
        rejected_count += 1
        continue
    clean_labels.append(cleaned_label)

print("Rejected labels count: ", rejected_count)
print("Clean labels: ", clean_labels)
