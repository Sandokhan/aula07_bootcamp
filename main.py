from typing import List

def calculate_average(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0

print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(calculate_average([]))  # Output: 0.0

def filter_greater_than(values: List[float], threshold: float) -> List[float]:
    return [value for value in values if value > threshold]

print(filter_greater_than([1, 2, 3, 4, 5], 3))  # Output: [4, 5]

def count_unique(values: List[float]) -> int:
    return len(set(values))

print(count_unique([1, 2, 2, 3, 4, 4, 5]))  # Output: 5

def celsius_to_fahrenheit(celsius: List[float]) -> float:
    return [(temp * 9/5) + 32 for temp in celsius]

print(celsius_to_fahrenheit([0, 20, 37]))  # Output: [32.0, 68.0, 98.6]