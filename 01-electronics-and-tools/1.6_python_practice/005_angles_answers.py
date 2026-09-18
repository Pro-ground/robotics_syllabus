# Problem 5 — degrees, radians, distance, and heading
# Write a single file, e.g. 005_angles.py. No extra packages. Use the math
# module from the standard library.
#
# Python's sin and cos expect radians, not degrees. A radian is another
# unit for angle: 180 degrees is pi radians (about 3.14159). Datasheets and
# later robot code mix both units.
#
# * Do section 1.5_maths_practice of 01-electronics-and-tools.md before this file. That
# sheet is the numbers. This file is the same idea in Python.
#
# What you will need
#
# Packages: the math module only (import math). No NumPy in this file.
#
# Ideas to have in place before you start:
# - Degrees: a full turn is 360.
# - Radians: a full turn is 2 * pi.
# - Heading is the direction of a point (x, y) from the origin, as an angle.
# - math.atan2(y, x) gives that direction in radians. The argument order is
#   y first, then x. That is easy to get backwards.
# - math.hypot(dx, dy) is the straight-line distance for a pair of
#   differences. Look it up if you have not used it.
#
# Tools to look up if you do not know them yet:
# - math.pi, math.radians, math.degrees (you may use these, or write the
#   multiply-and-divide yourself)
# - math.atan2
# - math.hypot
# - the % remainder operator, if you wrap the angle yourself
#
# You do not need: NumPy, loops over files, or classes.
#
# 1. degrees_to_radians(deg)
#    Convert deg to radians and return a float.
#
# 2. radians_to_degrees(rad)
#    Convert rad to degrees and return a float.
#
# 3. wrap_degrees(deg)
#    Return an angle equal to deg, but shifted by whole turns of 360 so the
#    result is in the range (-180, 180].
#    That means 180 stays 180, and -180 becomes 180 (same direction).
#    190 becomes -170. -190 becomes 170. 360 and 0 both become 0.
#
# 4. distance(x1, y1, x2, y2)
#    Return the straight-line distance between (x1, y1) and (x2, y2).
#
# 5. heading_degrees(x, y)
#    Return the heading of the point (x, y) from (0, 0), in degrees, wrapped
#    with wrap_degrees.
#    The positive x axis is 0. Positive y is 90. Negative x is 180.
#    Negative y is -90.
#    If x and y are both 0, return 0.0.
#
#
# Examples
#
# degrees_to_radians(180)     is math.pi
# radians_to_degrees(math.pi) is 180
#
# wrap_degrees(0)     ->  0
# wrap_degrees(180)   ->  180
# wrap_degrees(-180)  ->  180
# wrap_degrees(190)   ->  -170
# wrap_degrees(-190)  ->  170
# wrap_degrees(360)   ->  0
#
# distance(0, 0, 3, 4)  ->  5
#
# heading_degrees(1, 0)   ->  0
# heading_degrees(0, 1)   ->  90
# heading_degrees(-1, 0)  ->  180
# heading_degrees(0, -1)  ->  -90
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 005_angles.py
# All of it should print ok and not raise.
#

# ----- EXERCISE -----

# 1. degrees_to_radians(deg)
#    Convert deg to radians and return a float.
import math

def degrees_to_radians(deg):
    return float(math.radians(deg))


# 2. radians_to_degrees(rad)
#    Convert rad to degrees and return a float.
def radians_to_degrees(rad):
    return float(math.degrees(rad))

# 3. wrap_degrees(deg)
#    Return an angle equal to deg, but shifted by whole turns of 360 so the
#    result is in the range (-180, 180].
#    That means 180 stays 180, and -180 becomes 180 (same direction).
#    190 becomes -170. -190 becomes 170. 360 and 0 both become 0.

def wrap_degrees(deg):
     return 180 - (180 - deg) % 360

# 4. distance(x1, y1, x2, y2)
#    Return the straight-line distance between (x1, y1) and (x2, y2).

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

# 5. heading_degrees(x, y)
#    Return the heading of the point (x, y) from (0, 0), in degrees, wrapped
#    with wrap_degrees.
#    The positive x axis is 0. Positive y is 90. Negative x is 180.
#    Negative y is -90.
#    If x and y are both 0, return 0.0.

def heading_degrees(x, y):
    if x == 0 and y == 0:
        return 0.0

    degrees = math.degrees(math.atan2(y, x))
    return wrap_degrees(degrees)

# ----- ASSERTION ------
#

import math

assert abs(degrees_to_radians(180) - math.pi) < 1e-12
assert abs(degrees_to_radians(0) - 0.0) < 1e-12
assert abs(degrees_to_radians(90) - (math.pi / 2)) < 1e-12
assert abs(radians_to_degrees(math.pi) - 180.0) < 1e-12
assert abs(radians_to_degrees(0.0) - 0.0) < 1e-12
assert abs(radians_to_degrees(-math.pi / 2) - (-90.0)) < 1e-12

assert wrap_degrees(0) == 0 or abs(wrap_degrees(0) - 0.0) < 1e-12
assert abs(wrap_degrees(180) - 180) < 1e-12
assert abs(wrap_degrees(-180) - 180) < 1e-12
assert abs(wrap_degrees(190) - (-170)) < 1e-12
assert abs(wrap_degrees(-190) - 170) < 1e-12
assert abs(wrap_degrees(360) - 0) < 1e-12
assert abs(wrap_degrees(-360) - 0) < 1e-12
assert abs(wrap_degrees(540) - 180) < 1e-12
assert abs(wrap_degrees(-540) - 180) < 1e-12
assert abs(wrap_degrees(45) - 45) < 1e-12

assert abs(distance(0, 0, 3, 4) - 5) < 1e-12
assert abs(distance(1, 1, 1, 1) - 0) < 1e-12
assert abs(distance(-1, 0, 2, 4) - 5) < 1e-12

assert abs(heading_degrees(1, 0) - 0) < 1e-12
assert abs(heading_degrees(0, 1) - 90) < 1e-12
assert abs(heading_degrees(-1, 0) - 180) < 1e-12
assert abs(heading_degrees(0, -1) - (-90)) < 1e-12
assert abs(heading_degrees(0, 0) - 0) < 1e-12
assert abs(heading_degrees(1, 1) - 45) < 1e-12

print("ok")
