def get_priority(label: str, confidence: float) -> str:
    if confidence < 0.50 or label.lower().strip() == "unknown":
        return "HIGH"
    elif confidence < 0.80:
        return "MEDIUM"
    else:
        return "LOW"


print(get_priority("unknown", 0.4))  # HIGH
print(get_priority("class1", 0.6))  # MEDIUM
print(get_priority("class2", 0.9))  # LOW
print(get_priority("unknown", 0.9))  # HIGH
