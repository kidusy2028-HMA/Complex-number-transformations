"""
Complex Number Transformation Experiments

Demonstrates:
1. Rotation
2. Scaling
3. Translation
4. Combined transformations
"""

from complex_transform import (
    rotate,
    scale,
    translate,
    transform,
    modulus,
    argument
)


z = 3 + 4j


print("=== COMPLEX NUMBER TRANSFORMATIONS ===")

print("\nOriginal point:", z)

print("Modulus:", modulus(z))

print("Argument:", argument(z))


# Experiment 1: Rotation

rotated = rotate(z, 90)

print("\nExperiment 1: Rotation by 90 degrees")

print("Result:", rotated)


# Experiment 2: Scaling

scaled = scale(z, 2)

print("\nExperiment 2: Scaling by factor 2")

print("Result:", scaled)


# Experiment 3: Translation

translated = translate(z, 2, 3)

print("\nExperiment 3: Translation by 2 + 3i")

print("Result:", translated)


# Experiment 4: Combined transformation

combined = transform(
    z,
    angle=90,
    factor=2,
    dx=1,
    dy=2
)

print("\nExperiment 4: Combined Transformation")

print("Result:", combined)


# Experiment 5: Transform a triangle

triangle = [
    0 + 0j,
    3 + 0j,
    1.5 + 3j
]

transformed_triangle = [
    transform(
        point,
        angle=45,
        factor=1.5,
        dx=2,
        dy=1
    )
    for point in triangle
]

print("\nExperiment 5: Triangle Transformation")

for original, new in zip(triangle, transformed_triangle):

    print(original, "->", new)
