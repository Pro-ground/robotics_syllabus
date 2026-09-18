# Problem 18 — rotate a point and blend two angle guesses
#
# Do 005_angles.py and 017_numpy_basics.py first so degrees-versus-radians
# and arrays are not new at the same time as rotation.
#
# A 2D rotation matrix is a 2-by-2 grid of numbers that turns a point
# around the origin. You build it from cos and sin of the angle.
# NumPy's cos and sin use radians. Convert from degrees first (005).
#
# What you will need
#
# Packages: NumPy only (import numpy as np).
#
# Ideas to have in place before you start:
# - Blending two angle guesses, from 1.5_maths_practice/006_mean_and_blend.md
# - A transform here is a slide (tx, ty) plus a turn (theta_deg). Combining
#   two transforms means "do the first, then the second."
# - A complementary filter blends two angle estimates: one from adding up
#   gyroscope steps (gyro * dt, from 004), and one from the
#   accelerometer. alpha is how much you trust the gyro side.
#
# Tools to look up if you do not know them yet:
# - np.radians or the same conversion you wrote in 005
# - np.cos, np.sin
# - np.array and multiplying a matrix by a vector (@ or np.dot)
# - a for loop over gyro samples (from 003)
# - float() or .tolist() so you return a plain Python list where asked
#
# You do not need: SciPy, a real motion sensor, or to derive the rotation
# matrix from scratch; the spec writes the grid down.
#
# Snippets
#
#   theta = np.radians(angle_degrees)
#   c = np.cos(theta)
#   s = np.sin(theta)
#   rotation = np.array([[c, -s], [s, c]])
#   moved = rotation @ np.array(point)
#   return [float(moved[0]), float(moved[1])]
#
#   angle = alpha * (angle + omega * dt) + (1 - alpha) * accel_angle
#
# ----- EXERCISE -----
#
# 1. rotate_point_2d(point, angle_degrees)
#    point is [x, y]. angle_degrees is a counter-clockwise turn.
#    Return the rotated point as a plain Python list of two floats.
#    The 2-by-2 rotation matrix is:
#      [cos(θ)  -sin(θ)]
#      [sin(θ)   cos(θ)]
#
#    Examples
#    rotate_point_2d([1.0, 0.0], 90)   ->  [0.0, 1.0]
#    rotate_point_2d([1.0, 0.0], 0)    ->  [1.0, 0.0]
#    rotate_point_2d([1.0, 0.0], 180)  ->  [-1.0, 0.0]
#    Your answer:

def rotate_point_2d(point, angle_degrees):
    pass


# 2. combine_transforms(t1, t2)
#    A transform is a dict with keys "tx", "ty", "theta_deg"
#    (translation in x, translation in y, rotation in degrees
#    counter-clockwise).
#    Apply t2 after t1. Return one combined dict.
#    The combined rotation is the sum of the angles.
#    If t2 translates by (dx, dy) and the combined rotation is θ:
#      tx_combined = t1["tx"] + dx*cos(θ) - dy*sin(θ)
#      ty_combined = t1["ty"] + dx*sin(θ) + dy*cos(θ)
#      theta_combined = t1["theta_deg"] + t2["theta_deg"]
#    Use NumPy for the trigonometric and multiplication work.
#
#    Examples
#    t1 = {"tx": 10, "ty": 0, "theta_deg": 0}
#    t2 = {"tx": 0, "ty": 5, "theta_deg": 0}
#    combine_transforms(t1, t2) -> {"tx": 10, "ty": 5, "theta_deg": 0}
#    Your answer:

def combine_transforms(t1, t2):
    pass


# 3. simple_complementary_filter(gyro_readings, accel_angle, dt, alpha=0.98)
#    gyro_readings is a list of angular velocity samples (degrees/second).
#    accel_angle is a single angle estimate from the accelerometer.
#    dt is the time between samples in seconds.
#    alpha is the blending factor (default 0.98).
#    Start with angle = accel_angle.
#    For each gyro reading ω in gyro_readings:
#      angle = alpha * (angle + ω * dt) + (1 - alpha) * accel_angle
#    Return the final angle after processing all gyro samples.
#    Your answer:

def simple_complementary_filter(gyro_readings, accel_angle, dt, alpha=0.98):
    pass


# ----- ASSERTION ------

import numpy as np

r = rotate_point_2d([1.0, 0.0], 90)
assert abs(r[0] - 0.0) < 1e-9 and abs(r[1] - 1.0) < 1e-9, f"Got {r}"

r = rotate_point_2d([1.0, 0.0], 0)
assert abs(r[0] - 1.0) < 1e-9 and abs(r[1] - 0.0) < 1e-9

r = rotate_point_2d([1.0, 0.0], 180)
assert abs(r[0] - (-1.0)) < 1e-9 and abs(r[1] - 0.0) < 1e-9

r = rotate_point_2d([0.0, 1.0], 90)
assert abs(r[0] - (-1.0)) < 1e-9 and abs(r[1] - 0.0) < 1e-9

r = rotate_point_2d([1.0, 0.0], 45)
assert abs(r[0] - 0.7071067811865476) < 1e-9
assert abs(r[1] - 0.7071067811865476) < 1e-9

c = combine_transforms(
    {"tx": 10, "ty": 0, "theta_deg": 0},
    {"tx": 0, "ty": 5, "theta_deg": 0},
)
assert abs(c["tx"] - 10.0) < 1e-9
assert abs(c["ty"] - 5.0) < 1e-9
assert abs(c["theta_deg"] - 0.0) < 1e-9

c2 = combine_transforms(
    {"tx": 0, "ty": 0, "theta_deg": 90},
    {"tx": 5, "ty": 0, "theta_deg": 0},
)
assert abs(c2["tx"] - 0.0) < 1e-9
assert abs(c2["ty"] - 5.0) < 1e-9
assert abs(c2["theta_deg"] - 90.0) < 1e-9

angle = simple_complementary_filter([0.0, 0.0, 0.0, 0.0, 0.0], 45.0, 0.01)
assert abs(angle - 45.0) < 1e-9, f"Expected 45.0, got {angle}"

angle2 = simple_complementary_filter([10.0, 10.0, 10.0, 10.0, 10.0], 45.0, 0.01)
assert 45.0 < angle2 < 45.5, f"Expected between 45.0 and 45.5, got {angle2}"

angle3 = simple_complementary_filter([10.0], 45.0, 0.01)
assert abs(angle3 - 45.098) < 1e-6, f"Expected 45.098, got {angle3}"

print("ok")
