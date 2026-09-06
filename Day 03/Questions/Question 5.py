samples = [
    {
        "age": 22,
        "label": "ham",
        "score": 0.91,
        "country": "LK",
        "is_premium": False,
        "has_missing_values": False,
    },
    {
        "age": 17,
        "label": "ham",
        "score": 0.91,
        "country": "LK",
        "is_premium": False,
        "has_missing_values": False,
    },
    {
        "age": 30,
        "label": "spam",
        "score": 0.88,
        "country": "US",
        "is_premium": True,
        "has_missing_values": False,
    },
    {
        "age": 40,
        "label": "ham",
        "score": None,
        "country": "US",
        "is_premium": True,
        "has_missing_values": False,
    },
    {
        "age": 50,
        "label": "ham",
        "score": 0.75,
        "country": "US",
        "is_premium": False,
        "has_missing_values": False,
    },
]


def is_eligible(sample_dict: dict) -> bool:
    age_ok = "age" in sample_dict and 18 < sample_dict["age"] <= 65

    label_ok = sample_dict["label"] != "spam"

    score_ok = sample_dict["score"] is not None and sample_dict["score"] >= 0.60

    country_ok = sample_dict["country"] == "LK"

    premium_ok = sample_dict["is_premium"]

    no_missing_values = not sample_dict["has_missing_values"]

    print(f"\nChecking: {sample_dict}")
    print(f"age_ok={age_ok}")
    print(f"label_ok={label_ok}")
    print(f"score_ok={score_ok}")
    print(f"country_ok={country_ok}")
    print(f"premium_ok={premium_ok}")
    print(f"no_missing_values={no_missing_values}")

    eligible = (
        age_ok
        and label_ok
        and score_ok
        and country_ok
        and premium_ok
        and no_missing_values
    )

    print(f"\nEligible={eligible}")

    return eligible


eligible_count = 0

for i, data in enumerate(samples, start=1):
    print(f"\n--- Sample #{i} ---")
    if is_eligible(data):
        eligible_count += 1

print(f"\nEligible count: {eligible_count}")
