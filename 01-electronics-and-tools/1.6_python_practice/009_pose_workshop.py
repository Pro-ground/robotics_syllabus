# Problem 9 — pose, twist, and a short history
#
# A pose is where a body is on a flat plane: x, y, and heading. Heading
# here is an angle in radians (a full turn is 2 * pi). A twist is how
# that body is moving: a forward speed and a turning rate.
#
# You take a forward speed and a turning rate, advance them by a small
# time interval dt, and update position and heading. There is no
# calculus — only adding a little motion onto the last pose.
#
# Do not silently change the values you were given. Return new
# dictionaries and lists. Leave the inputs as they were.
#
# What you will need
#
# Packages: the math module (import math).
#
# Ideas to have in place before you start:
# - x grows by (forward speed) * cos(heading) * dt
# - y grows by (forward speed) * sin(heading) * dt
# - heading grows by (turning rate) * dt
# - math.cos and math.sin expect radians.
# - dict(...) or a new {} so you do not write back into the pose you
#   were given (from 006).
#
# Tools to look up if you do not know them yet:
# - math.cos, math.sin
# - default arguments (from 008), if you want a default max history length
#
# You do not need: NumPy or files.
#
# Snippets
#
#   import math
#   x = pose["x"] + twist["v"] * math.cos(pose["theta"]) * dt
#   y = pose["y"] + twist["v"] * math.sin(pose["theta"]) * dt
#   theta = pose["theta"] + twist["w"] * dt
#
#   kept = list(history)
#   kept.append(dict(pose))
#   if len(kept) > max_len:
#       kept = kept[-max_len:]
#
# ----- EXERCISE -----
#
# 1. make_pose(x, y, theta)
#    Return a new dictionary with keys "x", "y", "theta".
#    Your answer:

def make_pose(x, y, theta):
    pass


# 2. make_twist(v, w)
#    v is forward speed in metres per second.
#    w is turning rate in radians per second.
#    Return a new dictionary with keys "v" and "w".
#    Your answer:

def make_twist(v, w):
    pass


# 3. step_pose(pose, twist, dt)
#    Return a new pose after moving for dt seconds.
#    Do not change pose or twist.
#    Do not wrap the heading; that comes later.
#    Your answer:

def step_pose(pose, twist, dt):
    pass


# 4. remember_pose(history, pose, max_len=5)
#    history is a list of pose dictionaries.
#    Return a new list: the old items plus a copy of pose, then keep only
#    the last max_len items.
#    Do not change history. Do not store pose itself; store a copy.
#    If history is already longer than max_len, still return at most
#    max_len items after the append.
#    Your answer:

def remember_pose(history, pose, max_len=5):
    pass


# ----- ASSERTION ------

import math

p = make_pose(1.0, 2.0, 0.0)
assert p == {"x": 1.0, "y": 2.0, "theta": 0.0}
p["x"] = 0
assert make_pose(1.0, 2.0, 0.0)["x"] == 1.0

t = make_twist(1.0, 0.5)
assert t == {"v": 1.0, "w": 0.5}

start = make_pose(0.0, 0.0, 0.0)
moved = step_pose(start, make_twist(1.0, 0.0), 0.5)
assert abs(moved["x"] - 0.5) < 1e-12
assert abs(moved["y"] - 0.0) < 1e-12
assert abs(moved["theta"] - 0.0) < 1e-12
assert start == {"x": 0.0, "y": 0.0, "theta": 0.0}

turned = step_pose(make_pose(0.0, 0.0, 0.0), make_twist(0.0, 2.0), 0.25)
assert abs(turned["x"] - 0.0) < 1e-12
assert abs(turned["y"] - 0.0) < 1e-12
assert abs(turned["theta"] - 0.5) < 1e-12

diag = step_pose(make_pose(0.0, 0.0, math.pi / 2), make_twist(2.0, 0.0), 0.5)
assert abs(diag["x"] - 0.0) < 1e-12
assert abs(diag["y"] - 1.0) < 1e-12

history = [make_pose(0, 0, 0)]
pose = make_pose(1, 0, 0)
out = remember_pose(history, pose, max_len=3)
assert len(history) == 1
assert len(out) == 2
assert out[1] == {"x": 1, "y": 0, "theta": 0}
assert out[1] is not pose
pose["x"] = 99
assert out[1]["x"] == 1

long_hist = [
    make_pose(0, 0, 0),
    make_pose(1, 0, 0),
    make_pose(2, 0, 0),
]
trimmed = remember_pose(long_hist, make_pose(3, 0, 0), max_len=3)
assert len(trimmed) == 3
assert trimmed[0]["x"] == 1
assert trimmed[-1]["x"] == 3

print("ok")
