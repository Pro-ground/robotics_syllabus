# Problem 9 — pose, twist, and a short history
#
# This file is the worked answer for 009_pose_workshop.py. Try that file first.

import math


def make_pose(x, y, theta):
    return {"x": x, "y": y, "theta": theta}


def make_twist(v, w):
    return {"v": v, "w": w}


def step_pose(pose, twist, dt):
    return {
        "x": pose["x"] + twist["v"] * math.cos(pose["theta"]) * dt,
        "y": pose["y"] + twist["v"] * math.sin(pose["theta"]) * dt,
        "theta": pose["theta"] + twist["w"] * dt,
    }


def remember_pose(history, pose, max_len=5):
    kept = list(history)
    kept.append(dict(pose))
    if len(kept) > max_len:
        kept = kept[-max_len:]
    return kept


# ----- ASSERTION ------

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
