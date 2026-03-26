def average_ratios(numbers: list[float]) -> float:
    """
    Calculate the average of 100 divided by each number in the list.
    Skips zero values to avoid division by zero.

    Args:
        numbers (list[float]): List of numbers.

    Returns:
        float: The average ratio.

    Raises:
        ValueError: If no valid (non-zero) numbers are provided.
    """
    total = 0.0
    count = 0
    for num in numbers:
        if num != 0:
            total += 100 / num
            count += 1
    if count == 0:
        raise ValueError("No valid numbers to calculate average")
    return total / count


print(average_ratios([10, 5, 0]))
