# Problem 4 — a loop that keeps time
# Write a single file, e.g. 004_timed_loop.py. No extra packages. You may
# use the time module in your own experiments; the graded functions do not
# need it.
#
# On a robot, "loop" usually means: do one pass of work, then wait so that
# each pass starts a fixed time after the last. That fixed time is the
# period. The leftover wait is period minus how long the work already took.
# The time between two passes is called dt (delta time: the change in time).
#
# The angle step here is the same idea as "angle = angle + gyro * dt" when
# you later estimate tilt from a gyroscope.
#
# Do 1.5_maths_practice/004_rate_and_dt.md before this file. That sheet is
# the numbers. This file is the same idea in Python.
#
# What you will need
#
# Packages: none required. time is optional for your own checks.
#
# Ideas to have in place before you start:
# - A period is how long one full pass should last, in seconds.
# - elapsed is how long the work on this pass already took.
# - If the work took longer than the period, you do not sleep; you are late.
# - dt is a time step in seconds. Multiplying a rate (units per second) by
#   dt gives the change during that step.
#
# Tools to look up if you do not know them yet:
# - for and range (from 003)
# - if / else (from 002)
# - Calling a function that was passed in as an argument (now_fn, sleep_fn,
#   body_fn). You write now_fn(), not a hard-coded clock. That lets the
#   tests fake the clock.
#
# You do not need: files, NumPy, or a real robot. Do not call time.sleep
# inside the graded functions; call the sleep_fn you were given.
#
# 1. leftover_sleep(elapsed, period)
#    Both arguments are numbers of seconds, and both are greater than or
#    equal to 0.
#    Return how many seconds you should still wait so this pass lasts
#    exactly period.
#    If elapsed is already greater than or equal to period, return 0.0.
#    Always return a float.
#
# 2. step_angle(angle, gyro_dps, dt)
#    angle is the current angle in degrees.
#    gyro_dps is angular speed in degrees per second (positive or negative).
#    dt is the time step in seconds.
#    Return the new angle: the old angle plus (gyro_dps times dt).
#    Do not wrap the angle; that is 005.
#
# 3. run_fixed_rate(n_steps, period, now_fn, sleep_fn, body_fn)
#    Run a timed loop n_steps times. n_steps is an integer >= 0.
#    For each step with index i (0, then 1, then 2, ...):
#      - Record the start time by calling now_fn() with no arguments.
#      - Call body_fn(i).
#      - Record the time again with now_fn().
#      - Compute elapsed as (time after the body) minus (start time).
#      - Call sleep_fn(leftover) where leftover comes from leftover_sleep.
#    Return None.
#    If n_steps is 0, do nothing.
#
#
# Examples
#
# leftover_sleep(0.005, 0.020)  ->  0.015
# leftover_sleep(0.020, 0.020)  ->  0.0
# leftover_sleep(0.030, 0.020)  ->  0.0
#
# step_angle(10.0, 20.0, 0.1)   ->  12.0
# step_angle(0.0, -10.0, 0.5)   ->  -5.0
#
# # Fake clock: first now_fn call returns 0.0, second returns 0.005,
# # then 1.0 and 1.03. period is 0.02.
# # Step 0 sleeps 0.015; step 1 sleeps 0.0 because it ran long.
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 004_timed_loop.py
# All of it should print ok and not raise.
#

# ----- EXERCISE -----
# Write your code below.


# 1. leftover_sleep(elapsed, period)
#    Both arguments are numbers of seconds, and both are greater than or
#    equal to 0.
#    Return how many seconds you should still wait so this pass lasts
#    exactly period.
#    If elapsed is already greater than or equal to period, return 0.0.
#    Always return a float.

def leftover_sleep(elapsed:int, period:int) -> int:
    if elapsed >= period: return 0
    else:
        return period - elapsed

# 2. step_angle(angle, gyro_dps, dt)
#    angle is the current angle in degrees.
#    gyro_dps is angular speed in degrees per second (positive or negative).
#    dt is the time step in seconds.
#    Return the new angle: the old angle plus (gyro_dps times dt).
#    Do not wrap the angle; that is 005.
 
def step_angle(angle, gyro_dps, dt):
    return angle + (gyro_dps * dt)

# 3. run_fixed_rate(n_steps, period, now_fn, sleep_fn, body_fn)
#    Run a timed loop n_steps times. n_steps is an integer >= 0.
#    For each step with index i (0, then 1, then 2, ...):
#      - Record the start time by calling now_fn() with no arguments.
#      - Call body_fn(i).
#      - Record the time again with now_fn().
#      - Compute elapsed as (time after the body) minus (start time).
#      - Call sleep_fn(leftover) where leftover comes from leftover_sleep.
#    Return None.
#    If n_steps is 0, do nothing.

def run_fixed_rate(n_steps, period, now_fn, sleep_fn, body_fn):
    for i in range(n_steps):
        start = now_fn()
        body_fn(i)
        finish = now_fn()
        elapsed = finish - start
        leftover = leftover_sleep(elapsed, period)
        sleep_fn(leftover)


# ----- ASSERTION ------

assert abs(leftover_sleep(0.005, 0.020) - 0.015) < 1e-12
assert leftover_sleep(0.020, 0.020) == 0.0
assert leftover_sleep(0.030, 0.020) == 0.0
assert abs(leftover_sleep(0.0, 0.02) - 0.02) < 1e-12
assert abs(leftover_sleep(0.019, 0.02) - 0.001) < 1e-12

assert abs(step_angle(10.0, 20.0, 0.1) - 12.0) < 1e-12
assert abs(step_angle(0.0, -10.0, 0.5) - (-5.0)) < 1e-12
assert abs(step_angle(45.0, 0.0, 1.0) - 45.0) < 1e-12
assert abs(step_angle(0.0, 10.0, 0.01) - 0.1) < 1e-12

sleeps = []
body_calls = []
times = [0.0, 0.005, 1.0, 1.03]


def now_fn():
    return times.pop(0)


def sleep_fn(seconds):
    sleeps.append(seconds)


def body_fn(i):
    body_calls.append(i)


run_fixed_rate(2, 0.02, now_fn, sleep_fn, body_fn)
assert body_calls == [0, 1]
assert len(sleeps) == 2
assert abs(sleeps[0] - 0.015) < 1e-12
assert sleeps[1] == 0.0
assert times == []

body_calls.clear()
sleeps.clear()
run_fixed_rate(0, 0.02, now_fn, sleep_fn, body_fn)
assert body_calls == []
assert sleeps == []

print("ok")
