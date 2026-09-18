# Problem 19 — move a point and a pose on a flat plane
#
# Treat a list of two numbers as a vector: add, scale, take a length.
# You will rotate a point with a two-by-two grid of numbers, then put a
# rotation and a slide together so you can ask: where is this point if I
# am standing over there, facing that way?
#
# Angles in this file are radians. Wrap a heading so it stays in
# (-pi, pi]. That means pi stays pi, and -pi becomes pi.
#
# Build these functions yourself. You may use math or NumPy. Return plain
# Python lists and floats where the spec asks for them.
#
# What you will need
#
# Packages: math, or NumPy if you already installed it in 007.
#
# Ideas to have in place before you start:
# - wrap: shift by whole turns of 2*pi until the angle is in (-pi, pi]
# - rotate [x, y] around the origin with
#     [cos(θ)  -sin(θ)]
#     [sin(θ)   cos(θ)]
# - a pose is {"x", "y", "theta"} as in 009
# - to transform a point into the world: rotate it by the pose heading,
#   then add the pose position
# - step_pose is the same update as 009, then wrap the heading
#
# Tools to look up if you do not know them yet:
# - math.pi, math.cos, math.sin, math.hypot, math.atan2
# - the % remainder operator for wrapping
#
# You do not need: a plot window. simulate_path returns the points you
# would plot.
#
# Snippets
#
#   import math
#   wrapped = (angle + math.pi) % (2 * math.pi) - math.pi
#   if wrapped == -math.pi:
#       wrapped = math.pi
#
#   c = math.cos(theta)
#   s = math.sin(theta)
#   x2 = c * x - s * y
#   y2 = s * x + c * y
#
# ----- EXERCISE -----
#
# 1. wrap_angle(rad)
#    Return rad shifted by whole turns of 2*pi into (-pi, pi].
#    pi stays pi. -pi becomes pi. 3*pi becomes pi. -3*pi becomes pi.
#    Your answer:

def wrap_angle(rad):
    pass


# 2. rotate_point(point, theta)
#    point is [x, y]. theta is a counter-clockwise angle in radians.
#    Return a new list [x2, y2] as plain Python floats.
#    Your answer:

def rotate_point(point, theta):
    pass


# 3. transform_point(point, pose)
#    point is [x, y] in the body frame (straight ahead is +x).
#    pose is {"x", "y", "theta"} of the body in the world.
#    Return the world coordinates: rotate point by pose["theta"], then
#    add pose["x"] and pose["y"].
#    Do not change point or pose.
#    Your answer:

def transform_point(point, pose):
    pass


# 4. step_pose(pose, twist, dt)
#    Same motion as 009, then wrap the heading with wrap_angle.
#    twist is {"v", "w"}. Do not change pose or twist.
#    Your answer:

def step_pose(pose, twist, dt):
    pass


# 5. simulate_path(pose, twist, dt, n_steps)
#    Start from pose. Step n_steps times with the same twist and dt.
#    Return a list of poses of length n_steps + 1: the start, then each
#    new pose. Do not change the pose you were given.
#    Your answer:

def simulate_path(pose, twist, dt, n_steps):
    pass


# ----- ASSERTION ------

import math

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
