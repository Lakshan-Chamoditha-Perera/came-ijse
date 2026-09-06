raw_values = ["0.91", "bad", " ", "0.72", "0.88x", "0.65", ""]
clean_values = []

for value in raw_values:
    try:
        score = float(value.strip())
        clean_values.append(score)
    except ValueError:
        print(f"Skipping invalid value: '{value}'\n")

print("Raw values list   : ", raw_values)
print("Clean values list : ", [f"{score:.2f}" for score in clean_values])
