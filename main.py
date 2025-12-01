def select_patients(patients, k):
    """
    Select the first k patients by:
    1. Lower severity first (ascending)
    2. Lower arrival_order next (ascending)
    If k is 0 or patients is empty, return []
    Return a list of patient names.
    """

    if k <= 0 or not patients:
        return []

    # Sort by severity, then arrival_order
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Take the first k and return only names
    return [p["name"] for p in sorted_patients[:k]]


if __name__ == "__main__":
    sample = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample, 2))
