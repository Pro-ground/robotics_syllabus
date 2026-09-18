# Problem 26 — stop if the last good input is too old
#
# This file is the worked answer for 026_watchdog.py. Try that file first.

import math


def is_finite_command(cmd):
    return math.isfinite(cmd["v"]) and math.isfinite(cmd["w"])


def zero_command():
    return {"v": 0.0, "w": 0.0}


def apply_watchdog(cmd, now, last_good_time, timeout):
    if not is_finite_command(cmd):
        return zero_command()
    if now - last_good_time > timeout:
        return zero_command()
    return dict(cmd)


# ----- ASSERTION ------

assert is_finite_command({"v": 0.2, "w": -0.1}) is True
assert is_finite_command({"v": float("inf"), "w": 0.0}) is False
assert is_finite_command({"v": 0.0, "w": float("nan")}) is False
assert zero_command() == {"v": 0.0, "w": 0.0}

cmd = {"v": 0.4, "w": 0.1}
kept = apply_watchdog(cmd, 10.0, 9.9, 0.5)
assert kept == {"v": 0.4, "w": 0.1}
assert kept is not cmd
cmd["v"] = 9
assert kept["v"] == 0.4

assert apply_watchdog({"v": 0.4, "w": 0.1}, 10.0, 9.0, 0.5) == {"v": 0.0, "w": 0.0}
assert apply_watchdog({"v": 0.4, "w": 0.1}, 10.0, 9.5, 0.5) == {"v": 0.4, "w": 0.1}
assert apply_watchdog({"v": float("nan"), "w": 0.0}, 10.0, 9.9, 0.5) == {"v": 0.0, "w": 0.0}

print("ok")
