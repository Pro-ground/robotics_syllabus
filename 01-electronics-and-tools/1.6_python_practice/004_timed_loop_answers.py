# Problem 4 — a loop that keeps time
#
# This file is the worked answer for 004_timed_loop.py. Try that file first.

# ----- EXERCISE -----

def leftover_sleep(elapsed, period):
    leftover = period - elapsed
    if leftover < 0:
        return 0.0
    return float(leftover)


def step_angle(angle, gyro_dps, dt):
    return angle + (gyro_dps * dt)


def run_fixed_rate(n_steps, period, now_fn, sleep_fn, body_fn):
    for i in range(n_steps):
        start = now_fn()
        body_fn(i)
        finish = now_fn()
        elapsed = finish - start
        sleep_fn(leftover_sleep(elapsed, period))


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
