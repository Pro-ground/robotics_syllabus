# Problem 13 — load settings and a clock that only moves forward
#
# A settings file is often YAML: plain text with one name, a colon, a
# space, and a value on each line. You will read that shape without an
# extra package.
#
# On a robot, time is a single number that must not jump backwards. If a
# new stamp is older than the last one you accepted, keep the last one.
#
# What you will need
#
# Packages: none. Use open, strip, and split from 011.
#
# Ideas to have in place before you start:
# - float("0.4") turns the text 0.4 into a number.
# - A clock here is only the last accepted time, not the calendar date.
# - If the new time is greater than the last accepted time, take it.
#   Otherwise keep the last accepted time.
#
# Tools to look up if you do not know them yet:
# - split(":", 1) so a value may contain colons later
# - float(...)
#
# You do not need: PyYAML, NumPy, or a real clock.
#
# Snippets
#
#   name, raw = line.split(":", 1)
#   name = name.strip()
#   value = float(raw.strip())
#
#   if new_time > last_time:
#       last_time = new_time
#
# Example settings file:
#   stop_distance: 0.4
#   max_speed: 0.5
#
# ----- EXERCISE -----
#
# 1. load_params(filename)
#    Read a file of lines "name: number". Skip empty lines.
#    Return a dictionary mapping each name to a float.
#    If the file does not exist, raise FileNotFoundError.
#    Your answer:

def load_params(filename):
    pass


# 2. advance_clock(last_time, new_time)
#    Both arguments are numbers of seconds.
#    Return new_time if it is greater than last_time.
#    Otherwise return last_time.
#    Your answer:

def advance_clock(last_time, new_time):
    pass


# 3. age_seconds(now, stamp)
#    now and stamp are times in seconds.
#    Return now minus stamp. If that would be negative, return 0.0.
#    Always return a float.
#    Your answer:

def age_seconds(now, stamp):
    pass


# ----- ASSERTION ------

import os

test_yaml = "013_test_params.yaml"
with open(test_yaml, "w") as f:
    f.write("stop_distance: 0.4\n")
    f.write("\n")
    f.write("max_speed: 0.5\n")
    f.write("max_turn: 1.2\n")

params = load_params(test_yaml)
assert params["stop_distance"] == 0.4
assert params["max_speed"] == 0.5
assert params["max_turn"] == 1.2

assert advance_clock(1.0, 1.5) == 1.5
assert advance_clock(1.5, 1.5) == 1.5
assert advance_clock(1.5, 1.2) == 1.5
assert advance_clock(0.0, 0.01) == 0.01

assert abs(age_seconds(10.0, 9.7) - 0.3) < 1e-12
assert age_seconds(10.0, 10.0) == 0.0
assert age_seconds(10.0, 11.0) == 0.0

try:
    load_params("013_does_not_exist.yaml")
    assert False, "Should have raised FileNotFoundError"
except FileNotFoundError:
    pass

os.remove(test_yaml)

print("ok")
