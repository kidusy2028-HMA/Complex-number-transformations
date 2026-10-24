"""
Image Transformation Using Complex Numbers

Supports:
- Rotation
- Scaling
- Translation

Uses inverse mapping and bilinear interpolation.
"""

import math
import numpy as np

from PIL import Image


def transform_image(
    image,
    angle=0,
    scale=1,
    dx=0,
    dy=0,
    output_size=None
):
    """
    Transform an image using complex arithmetic.

    The transformation is:

    z' = scale * exp(i*theta) * z + (dx + i*dy)

    Coordinates are measured relative to the
    center of the image.

    dx and dy are measured in pixels.
    Positive dy moves the image upward.
    """

    if scale <= 0:
        raise ValueError("Scale must be positive.")

    image = image.convert("RGBA")

    source = np.asarray(image, dtype=np.float32)

    height, width = source.shape[:2]

    if output_size is None:
        output_width = width
        output_height = height
    else:
        output_width, output_height = output_size

    if output_width <= 0 or output_height <= 0:
        raise ValueError("Output dimensions must be positive.")

    result = np.zeros(
        (output_height, output_width, 4),
        dtype=np.float32
    )

    theta = math.radians(angle)

    multiplier = scale * complex(
        math.cos(theta),
        math.sin(theta)
    )

    translation = complex(dx, dy)

    source_cx = (width - 1) / 2
    source_cy = (height - 1) / 2

    output_cx = (output_width - 1) / 2
    output_cy = (output_height - 1) / 2

    for y in range(output_height):

        for x in range(output_width):

            # Output position as a complex number.
            # Imaginary axis points upward.

            z_out = complex(
                x - output_cx,
                output_cy - y
            )

            # Inverse complex transformation

            z_source = (
                z_out - translation
            ) / multiplier

            source_x = z_source.real + source_cx

            source_y = source_cy - z_source.imag

            # Bilinear interpolation

            if (
                0 <= source_x <= width - 1
                and 0 <= source_y <= height - 1
            ):

                x0 = int(math.floor(source_x))
                y0 = int(math.floor(source_y))

                x1 = min(x0 + 1, width - 1)
                y1 = min(y0 + 1, height - 1)

                wx = source_x - x0
                wy = source_y - y0

                p00 = source[y0, x0]
                p10 = source[y0, x1]
                p01 = source[y1, x0]
                p11 = source[y1, x1]

                top = (
                    (1 - wx) * p00
                    + wx * p10
                )

                bottom = (
                    (1 - wx) * p01
                    + wx * p11
                )

                pixel = (
                    (1 - wy) * top
                    + wy * bottom
                )

                result[y, x] = pixel

    result = np.clip(
        result,
        0,
        255
    ).astype(np.uint8)

    return Image.fromarray(result, "RGBA")


if __name__ == "__main__":

    image = Image.open("input.png")

    transformed = transform_image(
        image,
        angle=45,
        scale=0.8,
        dx=30,
        dy=20
    )

    transformed.save("output.png")

    print("Image transformed successfully!")
    print("Saved as output.png")
