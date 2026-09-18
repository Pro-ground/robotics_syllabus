# Problem 14 — NumPy for robotics
# Write a single file, e.g. 014_numpy_robotics.py. Requires NumPy.
#
# Do 005_angles.py and 013_numpy_basics.py first so degrees-versus-radians
# and arrays are not new at the same time as rotation.
# 015 puts the whole folder together in one short motion-sensor log project.
#
# What you will need
#
# Packages: NumPy only (import numpy as np).
#
# Ideas to have in place before you start:
# - Blending two angle guesses, from 1.5_maths_practice/006_mean_and_blend.md
# - A 2D rotation matrix is a 2-by-2 grid of numbers that turns a point
#   around the origin. You build it from cos and sin of the angle.
# - NumPy's cos and sin use radians. Convert from degrees first (005).
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
# These functions use the same NumPy foundations from Problem 13 but applied
# to the actual objects that appear in robotics: rotation matrices, vectors,
# and noisy sensor data.
#
# Spec
#
# 1. rotate_point_2d(point: list[float], angle_degrees: float) -> list[float]
#    Given a 2D point [x, y] and an angle in degrees, return the rotated
#    point as [x', y']. Build the 2×2 rotation matrix using numpy and
#    apply it to the point.
#    The standard 2D rotation matrix for counter-clockwise rotation by θ is:
#      [cos(θ)  -sin(θ)]
#      [sin(θ)   cos(θ)]
#    Return the result as a plain Python list of two floats, not a numpy array.
#
#    Examples:
#      rotate_point_2d([1.0, 0.0], 90)   →  [0.0, 1.0]
#      rotate_point_2d([1.0, 0.0], 0)    →  [1.0, 0.0]
#      rotate_point_2d([1.0, 0.0], 180)  →  [-1.0, 0.0]
#
# 2. combine_transforms(t1: dict, t2: dict) -> dict
#    A transform is represented as a dict with keys "tx", "ty", "theta_deg"
#    (translation in x, translation in y, rotation in degrees counter-clockwise).
#    Given two transforms, apply t2 after t1 (i.e., rotate first by t1,
#    translate by t1, then rotate by t2, translate by t2) and return the
#    combined transform as a single dict.
#
#    The combined rotation is just the sum of the angles.
#    The combined translation is t2's translation plus the t1-rotated version
#    of t2's translation vector. In other words, if t2 translates by (dx, dy)
#    and the combined rotation is θ, the effective translation is:
#      tx_combined = t1["tx"] + dx*cos(θ) - dy*sin(θ)
#      ty_combined = t1["ty"] + dx*sin(θ) + dy*cos(θ)
#      theta_combined = t1["theta_deg"] + t2["theta_deg"]
#
#    Use NumPy for the trigonometric and multiplication work.
#
#    Example:
#      t1 = {"tx": 10, "ty": 0, "theta_deg": 0}
#      t2 = {"tx": 0, "ty": 5, "theta_deg": 0}
#      combine_transforms(t1, t2) → {"tx": 10, "ty": 5, "theta_deg": 0}
#
# 3. simple_complementary_filter(gyro_readings: list[float], accel_angle: float,
#   dt: float, alpha: float = 0.98) -> float
#    Implements the complementary filter used for IMU angle estimation.
#    gyro_readings is a list of angular velocity samples (degrees/second).
#    accel_angle is a single angle estimate from the accelerometer (assumed
#    correct at the current instant, but noisy).
#    dt is the time between samples in seconds.
#    alpha is the blending factor (default 0.98).
#
#    Start with angle = accel_angle (the filter's initial state).
#    For each gyro reading ω in gyro_readings:
#      angle = alpha * (angle + ω * dt) + (1 - alpha) * accel_angle
#
#    Return the final angle after processing all gyro samples.
#    This simulates what a real robot would do at every control loop step.
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 014_numpy_robotics.py
# All of it should print ok and not raise.
#

# ----- EXERCISE -----
# Write your code below.
#

#
#
#
#
#
#
#
#
#
#
#
# ----- ASSERTION ------
#

import numpy as np

# --- rotate_point_2d ---
r = rotate_point_2d([1.0, 0.0], 90)
assert abs(r[0] - 0.0) < 1e-9 and abs(r[1] - 1.0) < 1e-9, f"Got {r}"

r = rotate_point_2d([1.0, 0.0], 0)
assert abs(r[0] - 1.0) < 1e-9 and abs(r[1] - 0.0) < 1e-9

r = rotate_point_2d([1.0, 0.0], 180)
assert abs(r[0] - (-1.0)) < 1e-9 and abs(r[1] - 0.0) < 1e-9

r = rotate_point_2d([0.0, 1.0], 90)
assert abs(r[0] - (-1.0)) < 1e-9 and abs(r[1] - 0.0) < 1e-9

# 45 degrees: [1,0] should rotate to [cos(45°), sin(45°)] ≈ [0.7071, 0.7071]
r = rotate_point_2d([1.0, 0.0], 45)
assert abs(r[0] - 0.7071067811865476) < 1e-9
assert abs(r[1] - 0.7071067811865476) < 1e-9

# --- combine_transforms ---
c = combine_transforms(
    {"tx": 10, "ty": 0, "theta_deg": 0},
    {"tx": 0, "ty": 5, "theta_deg": 0},
)
assert abs(c["tx"] - 10.0) < 1e-9
assert abs(c["ty"] - 5.0) < 1e-9
assert abs(c["theta_deg"] - 0.0) < 1e-9

# Rotation changes the translation
c2 = combine_transforms(
    {"tx": 0, "ty": 0, "theta_deg": 90},
    {"tx": 5, "ty": 0, "theta_deg": 0},
)
# Combined rotation = 90°. t2 translates by (5, 0). After 90° rotation,
# that vector becomes (0, 5). So combined translation = (0, 5).
assert abs(c2["tx"] - 0.0) < 1e-9
assert abs(c2["ty"] - 5.0) < 1e-9
assert abs(c2["theta_deg"] - 90.0) < 1e-9

# --- simple_complementary_filter ---
# Gyro reads 0°/s for 5 steps: angle should stay at accel_angle
angle = simple_complementary_filter([0.0, 0.0, 0.0, 0.0, 0.0], 45.0, 0.01)
assert abs(angle - 45.0) < 1e-9, f"Expected 45.0, got {angle}"

# Gyro reads 10°/s for 5 steps at dt=0.01: integrated change = 10*0.01*5 = 0.5°
# But complementary filter blends back toward accel_angle each step,
# so the angle will be closer to 45.0 than to 45.5.
angle2 = simple_complementary_filter([10.0, 10.0, 10.0, 10.0, 10.0], 45.0, 0.01)
# The unfiltered integration would give 45.5, but with alpha=0.98 the
# blended result is somewhere between 45.0 and 45.5.
assert 45.0 < angle2 < 45.5, f"Expected between 45.0 and 45.5, got {angle2}"

# Single sample: angle = 0.98*(45 + 10*0.01) + 0.02*45 = 0.98*45.1 + 0.9 = 44.198 + 0.9 = 45.098
angle3 = simple_complementary_filter([10.0], 45.0, 0.01)
assert abs(angle3 - 45.098) < 1e-6, f"Expected 45.098, got {angle3}"

print("ok")
