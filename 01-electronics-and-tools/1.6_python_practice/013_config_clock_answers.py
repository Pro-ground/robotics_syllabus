# Problem 13 — load settings and a clock that only moves forward
#
# This file is the worked answer for 013_config_clock.py. Try that file first.

def load_params(filename):
    params = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            name, raw = line.split(":", 1)
            params[name.strip()] = float(raw.strip())
    return params


def advance_clock(last_time, new_time):
    if new_time > last_time:
        return new_time
    return last_time


def age_seconds(now, stamp):
    age = now - stamp
    if age < 0:
        return 0.0
    return float(age)


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
