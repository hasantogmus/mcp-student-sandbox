# Mystery Module - Quadratic Equation Solver

A professional Python module for solving quadratic equations of the form **ax² + bx + c = 0** using the quadratic formula.

## Overview

This module provides a robust implementation for finding the real roots of quadratic equations. It uses the mathematical quadratic formula to calculate roots based on the coefficients of the equation.

**Mathematical Formula:**

```
For equation: ax² + bx + c = 0

x = (-b ± √(b² - 4ac)) / (2a)

Where:
- Discriminant (Δ) = b² - 4ac
- If Δ > 0: Two distinct real roots
- If Δ = 0: One repeated real root (double root)
- If Δ < 0: No real roots (complex numbers)
```

## Features

✅ **Robust Root Finding** - Accurately calculates real roots using the quadratic formula  
✅ **Type Hints** - Full type annotations for better IDE support and code clarity  
✅ **Comprehensive Documentation** - Detailed docstrings with examples  
✅ **Edge Case Handling** - Validates that the coefficient 'a' is non-zero  
✅ **Clear Return Values** - Returns tuple of roots or None for complex roots  
✅ **Backward Compatibility** - Legacy function name `fn_x` available  

## Installation

Simply import the module in your Python project:

```python
from mystery_module import solve_quadratic_equation
```

## Usage

### Basic Example

```python
from mystery_module import solve_quadratic_equation

# Solve x² - 5x + 6 = 0
roots = solve_quadratic_equation(a=1, b=-5, c=6)
print(roots)  # Output: (3.0, 2.0)
```

### Complete Examples

#### Example 1: Two Distinct Roots
```python
# Solve x² - 5x + 6 = 0
# Factored form: (x - 3)(x - 2) = 0
roots = solve_quadratic_equation(1, -5, 6)
print(f"Roots: {roots}")  # Output: (3.0, 2.0)
```

#### Example 2: No Real Roots (Complex Numbers)
```python
# Solve x² + 1 = 0
# Has complex roots: x = ±i
roots = solve_quadratic_equation(1, 0, 1)
print(f"Roots: {roots}")  # Output: None
```

#### Example 3: Double Root
```python
# Solve x² - 2x + 1 = 0
# Factored form: (x - 1)² = 0
roots = solve_quadratic_equation(1, -2, 1)
print(f"Roots: {roots}")  # Output: (1.0, 1.0)
```

#### Example 4: Scaled Equation
```python
# Solve 2x² + 4x + 2 = 0
# Simplified: x² + 2x + 1 = 0 → (x + 1)² = 0
roots = solve_quadratic_equation(2, 4, 2)
print(f"Roots: {roots}")  # Output: (-1.0, -1.0)
```

## API Reference

### `solve_quadratic_equation(a, b, c)`

**Parameters:**

| Parameter | Type  | Description |
|-----------|-------|-------------|
| `a` | `float` | Coefficient of x² (must be non-zero) |
| `b` | `float` | Coefficient of x |
| `c` | `float` | Constant term |

**Returns:**

| Return Value | Description |
|--------------|-------------|
| `Tuple[float, float]` | A tuple of two roots (x₁, x₂) when real roots exist |
| `None` | When no real roots exist (discriminant < 0) |

**Raises:**

| Exception | Condition |
|-----------|-----------|
| `ValueError` | When `a` is zero (equation is not quadratic) |

## Theory

### Quadratic Formula Derivation

The quadratic formula is derived from completing the square on the standard form ax² + bx + c = 0:

1. Start with: ax² + bx + c = 0
2. Divide by a: x² + (b/a)x + (c/a) = 0
3. Complete the square and solve for x
4. Result: x = (-b ± √(b² - 4ac)) / (2a)

### Discriminant Analysis

The **discriminant (Δ = b² - 4ac)** determines the nature of roots:

| Discriminant | Root Type | Example |
|--------------|-----------|---------|
| Δ > 0 | Two distinct real roots | x² - 5x + 6 = 0 → (3, 2) |
| Δ = 0 | One repeated real root | x² - 2x + 1 = 0 → (1, 1) |
| Δ < 0 | No real roots (complex) | x² + 1 = 0 → None |

## Error Handling

The module validates input and raises appropriate exceptions:

```python
# This will raise ValueError
try:
    roots = solve_quadratic_equation(0, 5, 6)  # a cannot be 0
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Coefficient 'a' cannot be zero. This is not a quadratic equation.
```

## Performance

- **Time Complexity:** O(1) - Constant time computation
- **Space Complexity:** O(1) - Minimal memory footprint

## Legacy Support

For backward compatibility, the original function name is still available:

```python
from mystery_module import fn_x

# These are equivalent
roots1 = solve_quadratic_equation(1, -5, 6)
roots2 = fn_x(1, -5, 6)
print(roots1 == roots2)  # True
```

## Best Practices

1. **Always validate 'a' is non-zero** - The function raises an error, but check your inputs
2. **Handle None returns** - Complex roots will return None:
   ```python
   roots = solve_quadratic_equation(1, 0, 1)
   if roots is None:
       print("No real roots exist (equation has complex roots)")
   ```
3. **Use type hints** - The module provides full type annotations for IDE support
4. **Check discriminant** - For understanding root behavior:
   ```python
   discriminant = b**2 - 4*a*c
   if discriminant < 0:
       print("Complex roots")
   ```

## Common Use Cases

- **Physics:** Projectile motion calculations
- **Engineering:** Circuit analysis and control systems
- **Finance:** Break-even point analysis
- **Mathematics:** Solving polynomial equations
- **Computer Graphics:** Ray-sphere intersection testing

## Testing

The module has been tested with:
- ✅ Two distinct real roots
- ✅ Complex roots (negative discriminant)
- ✅ Double roots (zero discriminant)
- ✅ Scaled coefficients
- ✅ Invalid input (a = 0)

## Version History

| Version | Changes |
|---------|---------|
| 2.0 | Refactored with type hints, docstrings, and better naming |
| 1.0 | Original implementation as `fn_x` |

## Contributing

To improve this module:
1. Ensure all test cases pass
2. Maintain type hints and docstrings
3. Follow PEP 8 style guidelines
4. Test edge cases thoroughly

## License

MIT License - Feel free to use this module in your projects

## References

- [Quadratic Formula - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_formula)
- [Discriminant - MathWorld](https://mathworld.wolfram.com/Discriminant.html)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Author Notes

This module was refactored from its original "mystery" form to provide:
- Clear, descriptive naming
- Complete documentation
- Type safety
- Edge case handling
- Professional code quality

The original function logic remains mathematically identical and accurate.
