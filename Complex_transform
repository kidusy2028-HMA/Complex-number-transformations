"""
Complex Number Transformation Engine

Mathematical model:

z' = r * (cos(theta) + i*sin(theta)) * z + (a + bi)

Supports:
- Rotation
- Scaling
- Translation
- Combined transformations
"""

import cmath
import math


def rotate(z, angle_degrees):
    """
    Rotate a complex number counterclockwise.

    Parameters:
        z: Complex number representing a point
        angle_degrees: Rotation angle in degrees

    Returns:
        Rotated complex number
    """

    theta = math.radians(angle_degrees)

    multiplier = cmath.exp(1j * theta)

    return z * multiplier


def scale(z, factor):
    """
    Scale a point relative to the origin.
    """

    if factor < 0:
        raise ValueError("Scale factor cannot be negative.")

    return z * factor


def translate(z, dx, dy):
    """
    Translate a point horizontally and vertically.
    """

    return z + complex(dx, dy)


def transform(z, angle=0, factor=1, dx=0, dy=0):
    """
    Apply rotation, scaling, and translation.

    z' = factor * exp(i*theta) * z + (dx + i*dy)
    """

    if factor < 0:
        raise ValueError("Scale factor cannot be negative.")

    theta = math.radians(angle)

    multiplier = factor * cmath.exp(1j * theta)

    translation = complex(dx, dy)

    return multiplier * z + translation


def transform_points(points, angle=0, factor=1, dx=0, dy=0):
    """
    Transform a collection of complex-number points.
    """

    return [
        transform(
            z,
            angle=angle,
            factor=factor,
            dx=dx,
            dy=dy
        )
        for z in points
    ]


def modulus(z):
    """
    Return the magnitude of a complex number.
    """

    return abs(z)


def argument(z):
    """
    Return the argument of a complex number in degrees.
    """

    return math.degrees(cmath.phase(z))
