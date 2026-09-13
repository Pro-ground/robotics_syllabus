# Problem 2 — decide what to do with a number
# No external packages, only the stdlib.
#
# A robot constantly asks "is this reading large enough to act on?" These
# functions practise that kind of choice.
#
# What you will need
#
# Packages: none. Use only what Python gives you with no additional install.
#
# Ideas to have in place before you start:
# - A comparison such as > or < produces True or False. That kind of value
#   is called a boolean.
# - abs(x) is the size of x with the sign removed, so abs(-3) is 3.
# - You choose between paths with if, elif (else-if), and else.
#
# Tools to look up if you do not know them yet:
# - if / elif / else
# - abs
# - returning a string or a boolean from a function
#
# You do not need: loops, files, or extra packages. Do not import anything.
#
# 1. clamp(value, low, high)
#    Return value, but never below low and never above high.
#    If value is below low, return low.
#    If value is above high, return high.
#    Otherwise return value unchanged.
#    Assume low is less than or equal to high.
#
# 2. in_deadband(value, centre, width)
#    A deadband is a range around a centre where you treat the value as
#    "close enough to ignore."
#    Return True if value is at most width away from centre (including the
#    edges). Return False otherwise.
#    width is never negative.
#
# 3. motor_command(error, deadband_width)
#    error is how far you are from the target. Positive means "too far
#    forward / too far right" in whatever units you are using; negative
#    means the other way.
#    Return one of these exact strings:
#      "stop"      if the error is inside the deadband around 0
#      "forward"   if the error is above the deadband
#      "backward"  if the error is below the deadband
#    Use in_deadband if you want; you do not have to.
#
#
# Examples
#
# clamp(5, 0, 10)    ->  5
# clamp(-1, 0, 10)   ->  0
# clamp(12, 0, 10)   ->  10
# clamp(0, 0, 10)    ->  0
# clamp(10, 0, 10)   ->  10
#
# in_deadband(0.2, 0, 0.5)   ->  True
# in_deadband(0.5, 0, 0.5)   ->  True
# in_deadband(0.6, 0, 0.5)   ->  False
# in_deadband(-0.4, 0, 0.5)  ->  True
#
# motor_command(0.2, 0.5)    ->  "stop"
# motor_command(0.8, 0.5)    ->  "forward"
# motor_command(-0.8, 0.5)   ->  "backward"
# motor_command(0.5, 0.5)    ->  "stop"

# ----- EXERCISE -----
def clamp(value:int, low:int, high:int) -> int:
    if value < low: return low
    elif value > high: return high
    else: return value

def in_deadband(value:int, centre:int, width:int)-> bool:
    if abs(centre) + abs(width) >= abs(value): return True
    else: return False 

def motor_command(error, deadband_width):
  if abs(error) <= deadband_width: return "stop"
  elif error > 0: return "forward"
  else: return "backward"


#----- ASSERTION ------

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
