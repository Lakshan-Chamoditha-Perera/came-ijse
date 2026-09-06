model_name = "baseline_tree"
accuracy = 0.8735
sample_count = 1250
threshold = 0.85
accepted = accuracy >= threshold

print(
    f"Model: {model_name} | Accuracy: {accuracy:.2%} | Samples: {sample_count} | Status: {accepted}"
)
