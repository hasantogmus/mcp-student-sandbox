"""
Module for processing data with clean, modular functions.
"""

def calculate_adjusted_value(value: float) -> float:
    """
    Calculate the adjusted value by multiplying with a factor.

    Args:
        value (float): The input value.

    Returns:
        float: The adjusted value.
    """
    return value * 1.15


def format_total(value: float) -> str:
    """
    Format the value as a total string.

    Args:
        value (float): The value to format.

    Returns:
        str: The formatted total string.
    """
    return f"Total: {value:.2f}"


def display_total(message: str) -> None:
    """
    Display the total message to the console.

    Args:
        message (str): The message to display.
    """
    print(message)


def log_results(results: list[float]) -> None:
    """
    Log the results to a file.

    Args:
        results (list[float]): The list of results to log.
    """
    with open("log.txt", "a") as f:
        f.write(str(results) + "\n")


def process_data(data: list[float]) -> list[float]:
    """
    Process the input data by calculating adjusted values, displaying totals, and logging results.

    Args:
        data (list[float]): The list of input values.

    Returns:
        list[float]: The list of adjusted values.
    """
    results = []
    for value in data:
        adjusted_value = calculate_adjusted_value(value)
        total_message = format_total(adjusted_value)
        display_total(total_message)
        results.append(adjusted_value)
    log_results(results)
    return results
