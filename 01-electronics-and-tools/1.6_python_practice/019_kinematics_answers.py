# Problem 19 — move a point and a pose on a flat plane
#
# This file is the worked answer for 019_kinematics.py. Try that file first.

import math


def wrap_angle(rad):
    wrapped = (rad + math.pi) % (2 * math.pi) - math.pi
    if wrapped == -math.pi:
        return math.pi
    return wrapped


def rotate_point(point, theta):
    c = math.cos(theta)
    s = math.sin(theta)
    x = point[0]
    y = point[1]
    return [float(c * x - s * y), float(s * x + c * y)]


def transform_point(point, pose):
    rotated = rotate_point(point, pose["theta"])
    return [rotated[0] + pose["x"], rotated[1] + pose["y"]]


def step_pose(pose, twist, dt):
    return {
        "x": pose["x"] + twist["v"] * math.cos(pose["theta"]) * dt,
        "y": pose["y"] + twist["v"] * math.sin(pose["theta"]) * dt,
        "theta": wrap_angle(pose["theta"] + twist["w"] * dt),
    }


def simulate_path(pose, twist, dt, n_steps):
    path = [dict(pose)]
    current = dict(pose)
    for _ in range(n_steps):
        current = step_pose(current, twist, dt)
        path.append(current)
    return path


# ----- ASSERTION ------

assert abs(wrap_angle(0.0) - 0.0) < 1e-12
assert abs(wrap_angle(math.pi) - math.pi) < 1e-12
assert abs(wrap_angle(-math.pi) - math.pi) < 1e-12
assert abs(wrap_angle(3 * math.pi) - math.pi) < 1e-12
assert abs(wrap_angle(-3 * math.pi) - math.pi) < 1e-12
assert abs(wrap_angle(math.pi / 2) - math.pi / 2) < 1e-12

p = rotate_point([1.0, 0.0], math.pi / 2)
assert abs(p[0] - 0.0) < 1e-12
assert abs(p[1] - 1.0) < 1e-12
p2 = rotate_point([1.0, 0.0], 0.0)
assert abs(p2[0] - 1.0) < 1e-12
assert abs(p2[1] - 0.0) < 1e-12

pose = {"x": 3.0, "y": 4.0, "theta": math.pi / 2}
world = transform_point([1.0, 0.0], pose)
assert abs(world[0] - 3.0) < 1e-12
assert abs(world[1] - 5.0) < 1e-12
assert pose["x"] == 3.0

start = {"x": 0.0, "y": 0.0, "theta": 0.0}
moved = step_pose(start, {"v": 1.0, "w": 0.0}, 0.5)
assert abs(moved["x"] - 0.5) < 1e-12
assert abs(moved["y"] - 0.0) < 1e-12
assert start["x"] == 0.0

spun = step_pose({"x": 0.0, "y": 0.0, "theta": math.pi * 0.9}, {"v": 0.0, "w": math.pi}, 0.3)
assert abs(wrap_angle(spun["theta"]) - spun["theta"]) < 1e-12
assert spun["theta"] <= math.pi + 1e-12
assert spun["theta"] > -math.pi

path = simulate_path({"x": 0.0, "y": 0.0, "theta": 0.0}, {"v": 1.0, "w": 0.0}, 0.1, 4)
assert len(path) == 5
assert abs(path[0]["x"] - 0.0) < 1e-12
assert abs(path[-1]["x"] - 0.4) < 1e-12
assert path[0] is not path[1]

print("ok")
