# Problem 27 — one closed loop
#
# Put 023, 025, and 026 together. A fake robot has a pose. Each step you read a
# range, aim at a point, limit the command, zero it if the last good
# scan is too old or the command is not finite, then integrate odometry.
#
# Stay at a Python rate: one step is one dt, not a real-time thread.
#
# Do not import from the earlier files. You may copy small helpers.
#
# What you will need
#
# Packages: the math module (import math).
#
# Ideas to have in place before you start:
# - command_to_point from 025
# - apply_watchdog from 026
# - integrate_odom from 025
# - if range <= stop_distance, the command is zeros before the watchdog
#
# Tools to look up if you do not know them yet:
# - the helpers you already wrote in 025 and 026
#
# Snippets
#
#   if scan is None or now - scan["stamp"] > timeout:
#       cmd = {"v": 0.0, "w": 0.0}
#   elif scan["range"] <= stop_distance:
#       cmd = {"v": 0.0, "w": 0.0}
#   else:
#       cmd = command_to_point(...)
#   cmd = apply_watchdog(cmd, now, last_good, timeout)
#   pose = integrate_odom(pose, cmd["v"], cmd["w"], dt)
#
# ----- EXERCISE -----
#
# 1. step_closed_loop(pose, target, scan, now, last_good_time, params)
#    params is a dict with keys:
#      "stop_distance", "v", "gain", "max_w", "timeout", "dt"
#    scan is None or {"range": number, "stamp": number}.
#    Return a dict with keys "pose" and "cmd" after one step.
#    Do not change pose, target, scan, or params.
#    Rules, in this order:
#      - If scan is None, or now - scan["stamp"] > timeout, or
#        scan["range"] <= stop_distance, start from zeros.
#      - Otherwise start from command_to_point(pose, target, v, gain, max_w).
#      - Pass that command through apply_watchdog using last_good_time
#        and timeout.
#      - Integrate odometry with the (possibly zeroed) command and dt.
#    Your answer:

def step_closed_loop(pose, target, scan, now, last_good_time, params):
    pass


# ----- ASSERTION ------

import math

params = {
    "stop_distance": 0.4,
    "v": 0.5,
    "gain": 2.0,
    "max_w": 1.0,
    "timeout": 0.3,
    "dt": 0.1,
}

pose = {"x": 0.0, "y": 0.0, "theta": 0.0}
target = {"x": 2.0, "y": 0.0}

# Fresh scan, clear path: move forward.
out = step_closed_loop(pose, target, {"range": 1.0, "stamp": 1.0}, 1.05, 1.0, params)
assert abs(out["cmd"]["v"] - 0.5) < 1e-12
assert abs(out["cmd"]["w"] - 0.0) < 1e-12
assert abs(out["pose"]["x"] - 0.05) < 1e-12
assert pose["x"] == 0.0

# Obstacle inside stop distance: sit still.
stopped = step_closed_loop(pose, target, {"range": 0.2, "stamp": 1.0}, 1.05, 1.0, params)
assert stopped["cmd"] == {"v": 0.0, "w": 0.0}
assert abs(stopped["pose"]["x"] - 0.0) < 1e-12

# Stale scan: sit still.
stale = step_closed_loop(pose, target, {"range": 1.0, "stamp": 0.5}, 1.05, 0.5, params)
assert stale["cmd"] == {"v": 0.0, "w": 0.0}

# No scan: sit still.
empty = step_closed_loop(pose, target, None, 1.05, 1.0, params)
assert empty["cmd"] == {"v": 0.0, "w": 0.0}

print("ok")
