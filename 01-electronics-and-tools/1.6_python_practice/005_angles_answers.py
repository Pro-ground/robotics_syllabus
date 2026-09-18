# Problem 5 — degrees, radians, distance, and heading
#
# This file is the worked answer for 005_angles.py. Try that file first.

import math

# ----- EXERCISE -----

def degrees_to_radians(deg):
    return float(math.radians(deg))


def radians_to_degrees(rad):
    return float(math.degrees(rad))


def wrap_degrees(deg):
    wrapped = (deg + 180) % 360 - 180
    if wrapped == -180:
        return 180
    return wrapped


def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def heading_degrees(x, y):
    if x == 0 and y == 0:
        return 0.0
    return wrap_degrees(math.degrees(math.atan2(y, x)))


# ----- ASSERTION ------

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
