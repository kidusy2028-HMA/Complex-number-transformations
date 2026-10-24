"""
Automated Tests for Complex Transformations
"""

import unittest

from complex_transform import (
    rotate,
    scale,
    translate,
    transform,
    transform_points,
    modulus,
    argument
)


class TestComplexTransformations(unittest.TestCase):

    def assertComplexAlmostEqual(self, actual, expected):

        self.assertAlmostEqual(
            actual.real,
            expected.real,
            places=7
        )

        self.assertAlmostEqual(
            actual.imag,
            expected.imag,
            places=7
        )


    def test_identity(self):

        z = 3 + 4j

        result = transform(z)

        self.assertComplexAlmostEqual(
            result,
            z
        )


    def test_rotation_90(self):

        z = 3 + 4j

        result = rotate(z, 90)

        self.assertComplexAlmostEqual(
            result,
            -4 + 3j
        )


    def test_rotation_180(self):

        z = 3 + 4j

        result = rotate(z, 180)

        self.assertComplexAlmostEqual(
            result,
            -3 - 4j
        )


    def test_scaling(self):

        z = 3 + 4j

        result = scale(z, 2)

        self.assertComplexAlmostEqual(
            result,
            6 + 8j
        )


    def test_translation(self):

        z = 3 + 4j

        result = translate(z, 2, 3)

        self.assertComplexAlmostEqual(
            result,
            5 + 7j
        )


    def test_combined_transformation(self):

        z = 3 + 4j

        result = transform(
            z,
            angle=90,
            factor=2,
            dx=1,
            dy=2
        )

        self.assertComplexAlmostEqual(
            result,
            -7 + 8j
        )


    def test_modulus(self):

        z = 3 + 4j

        self.assertAlmostEqual(
            modulus(z),
            5
        )


    def test_argument(self):

        z = 1 + 1j

        self.assertAlmostEqual(
            argument(z),
            45
        )


    def test_transform_points(self):

        points = [
            1 + 0j,
            0 + 1j
        ]

        results = transform_points(
            points,
            angle=90
        )

        self.assertComplexAlmostEqual(
            results[0],
            0 + 1j
        )

        self.assertComplexAlmostEqual(
            results[1],
            -1 + 0j
        )


    def test_negative_scale(self):

        with self.assertRaises(ValueError):

            scale(3 + 4j, -2)


if __name__ == "__main__":
    unittest.main()
