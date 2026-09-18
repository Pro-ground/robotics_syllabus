# 004 — A rate times a time step

Do `001`–`003` first. Do this file before `1.6_python_practice/004_timed_loop.py`. Module 2 uses the same step on a real motion sensor.

A **rate** is a change per unit of time: metres per second, degrees per second, counts per second. If the rate stays the same for a short stretch of time, the change during that stretch is

```
change = rate x time
```

On a robot the stretch of time between two passes of the control loop is usually called **dt**, for “delta time”: the change in time. If a gyroscope reports how fast the board is turning, in degrees per second, then one update is

```
new angle = old angle + (gyro rate x dt)
```

That is addition and multiplication. The Python file wraps it in a function. The number is the same.

If the work on one pass already took longer than the time you wanted the pass to last, you do not wait; you are late. That affects *when* the next pass starts. It does not change the formula above. You still multiply the rate by the dt you actually had, if you know it.

## Worked example

The angle is 10°. The gyroscope reads 20° per second. `dt` is 0.1 s.

```
new angle = 10 + (20 x 0.1) = 10 + 2 = 12°
```

## Problems

1. Angle 0°, gyro 10° per second, `dt` 0.5 s. What is the new angle?

2. Angle 45°, gyro −10° per second, `dt` 0.2 s. What is the new angle? A negative rate means the angle is decreasing.

3. Angle 0°. Gyro 20° per second. Five steps, each with `dt` 0.1 s. The rate does not change. What is the angle after five steps?

4. A wheel encoder adds 8 counts in 0.02 s. What is the count rate in counts per second?

5. A motor speed is 1200 counts per second. How many counts arrive in 0.025 s?

6. Angle 10°, gyro 20° per second. You wanted `dt` 0.02 s, but the work took 0.03 s, so the step you should apply is 0.03 s. What is the new angle if you use 0.03 s? What (wrong) angle do you get if you ignore the overrun and still use 0.02 s?

## How you know you are done

You can say in one sentence what `angle + gyro * dt` is doing, and you can do it by hand for a few steps. File `005` is next.

---

## Answers

1. `0 + 10 x 0.5 = 5°`

2. `45 + (−10) x 0.2 = 45 − 2 = 43°`

3. Each step adds `20 x 0.1 = 2°`. Five steps: `10°`.

4. `8 / 0.02 = 400` counts per second

5. `1200 x 0.025 = 30` counts

6. With 0.03 s: `10 + 20 x 0.03 = 10.6°`. With 0.02 s: `10 + 20 x 0.02 = 10.4°`. The difference is small here and grows if you stay late every pass.
