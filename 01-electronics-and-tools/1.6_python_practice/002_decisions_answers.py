# Problem 2 — decide what to do with a number
#
# This file is the worked answer for 002_decisions.py. Try that file first.

# ----- EXERCISE -----

def clamp(value, low, high):
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value


def in_deadband(value, centre, width):
    return abs(value - centre) <= width


def motor_command(error, deadband_width):
    if in_deadband(error, 0, deadband_width):
        return "stop"
    elif error > 0:
        return "forward"
    else:
        return "backward"


# ----- ASSERTION ------

assert clamp(5, 0, 10) == 5
assert clamp(-1, 0, 10) == 0
assert clamp(12, 0, 10) == 10
assert clamp(0, 0, 10) == 0
assert clamp(10, 0, 10) == 10
assert clamp(3.2, 3.2, 3.2) == 3.2

assert in_deadband(0.2, 0, 0.5) is True
assert in_deadband(0.5, 0, 0.5) is True
assert in_deadband(0.6, 0, 0.5) is False
assert in_deadband(-0.4, 0, 0.5) is True
assert in_deadband(-0.5, 0, 0.5) is True
assert in_deadband(-0.51, 0, 0.5) is False
assert in_deadband(21.5, 21.5, 0) is True
assert in_deadband(21.6, 21.5, 0) is False

assert motor_command(0.2, 0.5) == "stop"
assert motor_command(0.8, 0.5) == "forward"
assert motor_command(-0.8, 0.5) == "backward"
assert motor_command(0.5, 0.5) == "stop"
assert motor_command(-0.5, 0.5) == "stop"
assert motor_command(0.0, 0.1) == "stop"
assert motor_command(0.11, 0.1) == "forward"
assert motor_command(-0.11, 0.1) == "backward"

print("ok")
