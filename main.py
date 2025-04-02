from typing import List

def calculate_average(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0

print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(calculate_average([]))  # Output: 0.0

