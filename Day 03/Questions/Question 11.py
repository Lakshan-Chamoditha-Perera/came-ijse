# label, confidence
results = [("cat", 0.97), ("dog", 0.62), ("bird", 0.88), ("cat", 0.75)]

# Filter results with confidence >= 0.85
best_results = []
for label, confidence in results:
    if confidence >= 0.85:
        print(f"{label} -> {confidence}")
        best_results.append((label, confidence))

print(best_results)
