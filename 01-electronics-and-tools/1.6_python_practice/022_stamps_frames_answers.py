# Problem 22 — time on a message, and a named place
#
# This file is the worked answer for 022_stamps_frames.py. Try that file first.

import math


def stamp_pose(x, y, theta, stamp, frame):
    return {"x": x, "y": y, "theta": theta, "stamp": stamp, "frame": frame}


def message_age(now, stamp):
    age = now - stamp
    if age < 0:
        return 0.0
    return float(age)


def scan_point(range_m, angle_rad):
    return [
        float(range_m * math.cos(angle_rad)),
        float(range_m * math.sin(angle_rad)),
    ]


def scan_points(ranges, angle_min, angle_increment):
    points = []
    for i in range(len(ranges)):
        range_m = ranges[i]
        if range_m > 0:
            angle = angle_min + i * angle_increment
            points.append(scan_point(range_m, angle))
    return points


# ----- ASSERTION ------

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
assert abs(pts[1][0] - (-1.0)) < 1e-12
assert abs(pts[1][1] - 0.0) < 1e-12

print("ok")
