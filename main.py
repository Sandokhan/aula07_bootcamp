from typing import List

def calculate_average(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0

print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(calculate_average([]))  # Output: 0.0

def filter_greater_than(values: List[float], threshold: float) -> List[float]:
    return [value for value in values if value > threshold]

print(filter_greater_than([1, 2, 3, 4, 5], 3))  # Output: [4, 5]
