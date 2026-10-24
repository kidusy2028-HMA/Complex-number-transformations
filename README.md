# Complex Number Image Transformation Simulator

## Project Overview

This project investigates how complex numbers can be used
to perform geometric transformations in two-dimensional
computer graphics.

It demonstrates rotation, scaling, translation, and
combined transformations using complex arithmetic.

## Mathematical Model

Every point is represented by:

z = x + iy

The general transformation is:

z' = r(cos(theta) + i sin(theta))z + (a + bi)

Where:

- z = Original point
- z' = Transformed point
- r = Scale factor
- theta = Rotation angle
- a = Horizontal translation
- b = Vertical translation

## Mathematical Operations

### Rotation

z' = z * e^(i theta)

### Scaling

z' = rz

### Translation

z' = z + (a + bi)

### Combined Transformation

z' = r * e^(i theta) * z + (a + bi)

## Project Files

| File | Description |
|------|-------------|
| complex_transform.py | Core mathematical algorithms |
| demo.py | Mathematical experiments |
| image_transform.py | Image transformation using complex numbers |
| test_transform.py | Automated mathematical tests |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Mathematical Experiments

```bash
python demo.py
```

## Run the Tests

```bash
python -m unittest -v test_transform.py
```

## Transform an Image

Place an image named input.png in the project directory.

Then run:

```bash
python image_transform.py
```

The program will create:

output.png

## Example

Original point:

z = 3 + 4i

Rotate by 90 degrees:

z' = -4 + 3i

Scale by 2:

z' = 6 + 8i

Translate by 2 + 3i:

z' = 5 + 7i

Combined transformation:

z' = -7 + 8i

## Real-World Applications

- Computer graphics
- Image processing
- Two-dimensional animation
- Geometric modeling
- Robotics

## Limitations

The simulator performs two-dimensional transformations.

The image transformation uses inverse mapping and
bilinear interpolation.

The output image retains its original dimensions
unless a different output size is specified.

This is a mathematical simulation, not a
complete professional graphics editor.

## Educational Purpose

The project demonstrates how complex numbers,
Euler's formula, polar representation, and
geometric transformations can be combined
to solve computational problems.
