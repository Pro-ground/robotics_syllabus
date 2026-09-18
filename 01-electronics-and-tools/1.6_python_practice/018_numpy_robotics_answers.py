# Problem 18 — rotate a point and blend two angle guesses
#
# This file is the worked answer for 018_numpy_robotics.py. Try that file first.

import numpy as np


def rotate_point_2d(point, angle_degrees):
    theta = np.radians(angle_degrees)
    c = np.cos(theta)
    s = np.sin(theta)
    rotation = np.array([[c, -s], [s, c]])
    moved = rotation @ np.array(point, dtype=float)
    return [float(moved[0]), float(moved[1])]


def combine_transforms(t1, t2):
    theta = np.radians(t1["theta_deg"] + t2["theta_deg"])
    c = np.cos(theta)
    s = np.sin(theta)
    dx = t2["tx"]
    dy = t2["ty"]
    return {
        "tx": float(t1["tx"] + dx * c - dy * s),
        "ty": float(t1["ty"] + dx * s + dy * c),
        "theta_deg": float(t1["theta_deg"] + t2["theta_deg"]),
    }


def simple_complementary_filter(gyro_readings, accel_angle, dt, alpha=0.98):
    angle = accel_angle
    for omega in gyro_readings:
        angle = alpha * (angle + omega * dt) + (1 - alpha) * accel_angle
    return float(angle)


# ----- ASSERTION ------

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
