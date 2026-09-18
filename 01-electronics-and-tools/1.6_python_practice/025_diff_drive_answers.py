# Problem 25 — drive forward, turn, and limit a command
#
# This file is the worked answer for 025_diff_drive.py. Try that file first.

import math


def wrap_angle(rad):
    wrapped = (rad + math.pi) % (2 * math.pi) - math.pi
    if wrapped == -math.pi:
        return math.pi
    return wrapped


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def integrate_odom(pose, wheel_v, wheel_w, dt):
    return {
        "x": pose["x"] + wheel_v * math.cos(pose["theta"]) * dt,
        "y": pose["y"] + wheel_v * math.sin(pose["theta"]) * dt,
        "theta": wrap_angle(pose["theta"] + wheel_w * dt),
    }


def command_to_point(pose, target, v, gain, max_w):
    desired = math.atan2(target["y"] - pose["y"], target["x"] - pose["x"])
    error = wrap_angle(desired - pose["theta"])
    return {"v": v, "w": clamp(gain * error, -max_w, max_w)}


# ----- ASSERTION ------

assert abs(wrap_angle(math.pi) - math.pi) < 1e-12
assert abs(wrap_angle(-math.pi) - math.pi) < 1e-12
assert clamp(12, -1, 1) == 1
assert clamp(-12, -1, 1) == -1
assert clamp(0.2, -1, 1) == 0.2

start = {"x": 0.0, "y": 0.0, "theta": 0.0}
odom = integrate_odom(start, 1.0, 0.0, 0.5)
assert abs(odom["x"] - 0.5) < 1e-12
assert abs(odom["y"] - 0.0) < 1e-12
assert start["x"] == 0.0

turned = integrate_odom({"x": 0.0, "y": 0.0, "theta": 0.0}, 0.0, math.pi, 0.5)
assert abs(turned["theta"] - math.pi / 2) < 1e-12

pose = {"x": 0.0, "y": 0.0, "theta": 0.0}
target = {"x": 0.0, "y": 1.0}
cmd = command_to_point(pose, target, 0.4, 2.0, 1.0)
assert abs(cmd["v"] - 0.4) < 1e-12
assert abs(cmd["w"] - 1.0) < 1e-12
assert pose["theta"] == 0.0

aligned = command_to_point(
    {"x": 0.0, "y": 0.0, "theta": math.pi / 2},
    {"x": 0.0, "y": 2.0},
    0.3,
    2.0,
    1.0,
)
assert abs(aligned["w"] - 0.0) < 1e-12

print("ok")
