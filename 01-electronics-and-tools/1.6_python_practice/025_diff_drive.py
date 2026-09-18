# Problem 25 — drive forward, turn, and limit a command
#
# A wheeled robot on a plane can drive forward and turn. From those two
# numbers you can say how position and heading change. That is the same
# step as 009 and 019. Odometry is that step applied to what the wheels
# reported.
#
# A command is usually a heading or speed error, scaled and then limited.
# Clamp to a maximum speed and a maximum turn rate.
#
# What you will need
#
# Packages: the math module (import math).
#
# Ideas to have in place before you start:
# - step_pose from 009 / 019: x and y from v * dt, heading from w * dt
# - wrap the heading into (-pi, pi]
# - heading error toward a point is atan2(target_y - y, target_x - x)
#   minus the current heading, then wrapped
# - clamp from 002
#
# Tools to look up if you do not know them yet:
# - math.atan2, math.cos, math.sin
#
# You do not need: a simulator process. These functions are the motion
# model.
#
# Snippets
#
#   import math
#   desired = math.atan2(target["y"] - pose["y"], target["x"] - pose["x"])
#   error = wrap_angle(desired - pose["theta"])
#   w = clamp(gain * error, -max_w, max_w)
#
# ----- EXERCISE -----
#
# 1. wrap_angle(rad)
#    Same range as 015: (-pi, pi], with -pi becoming pi.
#    Your answer:

def wrap_angle(rad):
    pass


# 2. clamp(value, low, high)
#    Same rule as 002.
#    Your answer:

def clamp(value, low, high):
    pass


# 3. integrate_odom(pose, wheel_v, wheel_w, dt)
#    pose is {"x", "y", "theta"}.
#    Return a new pose after applying wheel_v and wheel_w for dt seconds.
#    Wrap the heading. Do not change pose.
#    Your answer:

def integrate_odom(pose, wheel_v, wheel_w, dt):
    pass


# 4. command_to_point(pose, target, v, gain, max_w)
#    target is {"x", "y"}.
#    heading_error is the wrapped difference from the current heading to
#    the heading of the target.
#    Return {"v": v, "w": clamp(gain * heading_error, -max_w, max_w)}.
#    Do not change pose or target.
#    Your answer:

def command_to_point(pose, target, v, gain, max_w):
    pass


# ----- ASSERTION ------

import math

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
