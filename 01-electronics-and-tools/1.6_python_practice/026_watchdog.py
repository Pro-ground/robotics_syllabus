# Problem 26 — stop if the last good input is too old
#
# A watchdog is a comparison against the clock: if the last good command
# is older than a timeout, publish zeros and sit still. Also reject
# values that are not finite (not a real number: inf or NaN).
#
# This is the safety rule the rest of the stack assumes. Stay at rates
# Python can honestly hold — tens of times per second.
#
# What you will need
#
# Packages: the math module (import math).
#
# Ideas to have in place before you start:
# - math.isfinite(x) is True when x is a real number.
# - age is now minus last_good_time (from 013).
# - A zero command is {"v": 0.0, "w": 0.0}.
#
# Tools to look up if you do not know them yet:
# - math.isfinite
# - float("nan") and float("inf") if you want to try bad values
#
# Snippets
#
#   import math
#   if not math.isfinite(cmd["v"]) or not math.isfinite(cmd["w"]):
#       return {"v": 0.0, "w": 0.0}
#   if now - last_good_time > timeout:
#       return {"v": 0.0, "w": 0.0}
#
# ----- EXERCISE -----
#
# 1. is_finite_command(cmd)
#    cmd is {"v", "w"}.
#    Return True if both v and w are finite. Return False otherwise.
#    Your answer:

def is_finite_command(cmd):
    pass


# 2. zero_command()
#    Return {"v": 0.0, "w": 0.0}.
#    Your answer:

def zero_command():
    pass


# 3. apply_watchdog(cmd, now, last_good_time, timeout)
#    If cmd is not a finite command, return zeros.
#    If now - last_good_time is greater than timeout, return zeros.
#    Otherwise return a copy of cmd (not cmd itself).
#    timeout is in seconds. now and last_good_time are seconds.
#    Your answer:

def apply_watchdog(cmd, now, last_good_time, timeout):
    pass


# ----- ASSERTION ------

import math

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
