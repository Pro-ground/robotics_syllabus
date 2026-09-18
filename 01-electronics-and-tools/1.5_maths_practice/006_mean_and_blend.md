# 006 — Mean of readings, and blending two guesses

Do `004` and `005` first. Do this file before the Python files that average or fuse readings (`017_numpy_basics.py`, `018_numpy_robotics.py`). Module 2 uses the blend on a real accelerometer and gyroscope.

The **mean** of a list of numbers is their sum divided by how many there are. For three temperature readings 21.5, 22.0, and 21.8:

```
mean = (21.5 + 22.0 + 21.8) / 3 = 65.3 / 3 = 21.7666...
```

That is the figure you will compute in a loop later. You do not need a statistics course for it.

A robot often has two imperfect guesses for the same thing. A gyroscope tracks short-term motion well and slowly drifts. An accelerometer gives an angle from gravity that jitters. One useful combination is a **weighted blend**: pick a weight `w` between 0 and 1, trust the first guess that much, and the second guess the rest.

```
result = w x first + (1 - w) x second
```

If `w` is 0.98, you take 98% of the first guess and 2% of the second. The two weights add to 1, so the result stays on the same scale as the inputs.

Module 2 writes one step of this for tilt as

```
angle = 0.98 x (old angle + gyro x dt) + 0.02 x accelerometer angle
```

The piece in brackets is the rate-times-time step from `004`. This file only asks you to do the arithmetic.

## Worked example

Old angle 45°. Gyro 10° per second. `dt` 0.01 s. Accelerometer angle 45°. Weight 0.98.

```
gyro guess = 45 + 10 x 0.01 = 45.1
result = 0.98 x 45.1 + 0.02 x 45 = 44.198 + 0.9 = 45.098°
```

## Problems

1. Find the mean of 10, 10, 10.

2. Find the mean of 1, 2, 3, 4, 5.

3. Blend first guess 10 and second guess 20 with weight `w = 0.5`. What do you get, and why is that the same as the ordinary mean of the two numbers?

4. Blend first guess 0 and second guess 10 with `w = 0.98`.

5. Old angle 0°, gyro 20° per second, `dt` 0.1 s, accelerometer angle 0°, `w = 0.98`. Compute the gyro guess, then the blended result.

6. Same as the worked example, but the accelerometer now reads 40° while the gyro guess is still 45.1°. What is the blended angle? Say in one sentence which way the accelerometer pulled the result, and why a small weight on that sensor still moves the number.

## How you know you are done

You can compute a mean and a one-step blend by hand. You are ready for the matching Python files, and for the tilt-sensor task in Module 2. Extra maths for later labs waits until Module 4.

---

## Answers

1. `10`

2. `15 / 5 = 3`

3. `0.5 x 10 + 0.5 x 20 = 15`. Equal weights on two numbers is their mean.

4. `0.98 x 0 + 0.02 x 10 = 0.2`

5. Gyro guess: `0 + 20 x 0.1 = 2`. Blend: `0.98 x 2 + 0.02 x 0 = 1.96°`

6. `0.98 x 45.1 + 0.02 x 40 = 44.198 + 0.8 = 44.998°`. The accelerometer is lower than the gyro guess, so the result is pulled down a little. Two percent of a 5.1° disagreement is about 0.1°, which is small on one step and adds up over many steps.
