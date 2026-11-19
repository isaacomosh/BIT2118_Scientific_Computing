"""Task 12: Polynomial and Nonlinear Equation Solving
Intersections of circle x^2 + y^2 = 4 and parabola y = x^2 - 1.
"""
import numpy as np
from scipy.optimize import root


def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]


for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()

# Bonus: polynomial roots, x^2 - 5x + 6 = 0
print("Roots of x^2 - 5x + 6:", np.roots([1, -5, 6]))
