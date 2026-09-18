# Problem 22 — time on a message, and a named place
#
# A stamp is a single time number on a message. Subtract stamps to see
# how old a reading is (from 013). A frame is a named coordinate system,
# such as "base_link" or "odom". Every pose needs a stamp and a frame
# name.
#
# Laser data arrives as a range and an angle. On the plane that pair
# becomes an x and a y. Keep units explicit: metres, radians.
#
# What you will need
#
# Packages: the math module (import math).
#
# Ideas to have in place before you start:
# - x = range_m * cos(angle_rad)
# - y = range_m * sin(angle_rad)
# - A stamped pose is a dictionary with "x", "y", "theta", "stamp",
#   and "frame".
# - age is now minus stamp, never negative (from 013).
#
# Tools to look up if you do not know them yet:
# - math.cos, math.sin
#
# You do not need: ROS 2 message types. A dict is enough here.
#
# Snippets
#
#   x = range_m * math.cos(angle_rad)
#   y = range_m * math.sin(angle_rad)
#
#   pose = {
#       "x": x, "y": y, "theta": theta,
#       "stamp": stamp, "frame": frame,
#   }
#
# ----- EXERCISE -----
#
# 1. stamp_pose(x, y, theta, stamp, frame)
#    Return a dictionary with keys "x", "y", "theta", "stamp", "frame".
#    Your answer:

def stamp_pose(x, y, theta, stamp, frame):
    pass


# 2. message_age(now, stamp)
#    Return now minus stamp as a float, or 0.0 if that would be negative.
#    Your answer:

def message_age(now, stamp):
    pass


# 3. scan_point(range_m, angle_rad)
#    Return [x, y] for one laser hit, as plain Python floats.
#    range_m is metres. angle_rad is radians from the robot x axis.
#    Your answer:

def scan_point(range_m, angle_rad):
    pass


# 4. scan_points(ranges, angle_min, angle_increment)
#    ranges is a list of range readings in metres.
#    The first reading is at angle_min. Each next reading adds
#    angle_increment radians.
#    Return a list of [x, y] points in the same order.
#    Skip a range if it is not greater than 0.
#    Your answer:

def scan_points(ranges, angle_min, angle_increment):
    pass


# ----- ASSERTION ------

import math

p = stamp_pose(1.0, 2.0, 0.3, 10.0, "odom")
assert p == {"x": 1.0, "y": 2.0, "theta": 0.3, "stamp": 10.0, "frame": "odom"}

assert message_age(10.5, 10.0) == 0.5
assert message_age(10.0, 10.0) == 0.0
assert message_age(9.0, 10.0) == 0.0

pt = scan_point(1.0, 0.0)
assert abs(pt[0] - 1.0) < 1e-12
assert abs(pt[1] - 0.0) < 1e-12
pt90 = scan_point(2.0, math.pi / 2)
assert abs(pt90[0] - 0.0) < 1e-12
assert abs(pt90[1] - 2.0) < 1e-12

pts = scan_points([1.0, 0.0, 1.0], 0.0, math.pi / 2)
assert len(pts) == 2
assert abs(pts[0][0] - 1.0) < 1e-12
assert abs(pts[0][1] - 0.0) < 1e-12
# The zero range is skipped, but it still occupied an angle step.
# The third reading is at angle_min + 2 * increment = pi.
assert abs(pts[1][0] - (-1.0)) < 1e-12
assert abs(pts[1][1] - 0.0) < 1e-12

print("ok")
