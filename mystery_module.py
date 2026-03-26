"""
Mystery Module - Quadratic Equation Solver

This module provides functionality to solve quadratic equations of the form:
    ax² + bx + c = 0

Using the quadratic formula to find real roots.
"""

import math
from typing import Optional, Tuple


def solve_quadratic_equation(
    a: float, b: float, c: float
) -> Optional[Tuple[float, float]]:
    """
    Solve a quadratic equation and return its real roots.

    Solves equations of the form: ax² + bx + c = 0

    Args:
        a (float): Coefficient of x² (must be non-zero).
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        Tuple[float, float]: A tuple containing the two roots (x₁, x₂).
                             Returns None if no real roots exist (discriminant < 0).

    Raises:
        ValueError: If a is zero (not a quadratic equation).

    Examples:
        >>> solve_quadratic_equation(1, -5, 6)
        (3.0, 2.0)

        >>> solve_quadratic_equation(1, 0, 1)
        None

        >>> solve_quadratic_equation(2, 4, 2)
        (-1.0, -1.0)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero. This is not a quadratic equation.")

    # Calculate discriminant: b² - 4ac
    discriminant = b**2 - 4 * a * c

    # If discriminant is negative, no real roots exist
    if discriminant < 0:
        return None

    # Calculate and return the two roots using the quadratic formula
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)

    return (root1, root2)


# Legacy function name for backward compatibility
fn_x = solve_quadratic_equation
