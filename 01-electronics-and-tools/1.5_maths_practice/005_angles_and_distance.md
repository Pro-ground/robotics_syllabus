# 005 — Degrees, radians, wrap, distance, heading

Do `004` first. Do this file before `1.6_python_practice/005_angles.py`. Datasheets and later robot code mix both angle units. When you later ask Python for the sine or cosine of an angle — the two standard functions that turn an angle into a pair of coordinates — you must pass radians, not degrees.

A full turn is **360 degrees**. The same full turn is **2π radians**, where **π** (pi) is about 3.14159. A **radian** is just the other common unit for the same quantity. Half a turn is 180° and also π radians.

```
radians = degrees x π / 180
degrees = radians x 180 / π
```

So 90° is π/2 radians (about 1.5708). 0 is 0 in both units.

Angles on a robot wander past 180° and below −180° if you keep adding gyroscope steps. Two numbers that differ by a whole turn (360°) point the same way: 190° and −170° are the same direction. **Wrapping** means shifting by whole turns of 360° so the number you keep sits in a useful range. The range this syllabus uses is (−180, 180]: 180 stays 180, and −180 becomes 180 (same direction).

A practical way to wrap into that range: add or subtract 360 until the value is greater than −180 and at most 180. If you land on −180, write 180.

The straight-line distance between two points is the long side of a right triangle whose other sides are the difference in x and the difference in y. If those differences are `dx` and `dy`, then

```
distance = square root of (dx x dx + dy x dy)
```

The 3-4-5 triangle is the one you should recognise without a calculator: if the differences are 3 and 4, the distance is 5.

**Heading** here means the direction of a point `(x, y)` from the origin `(0, 0)`, as an angle. This syllabus measures it from the positive x axis: positive x is 0°, positive y is 90°, negative x is 180°, negative y is −90°. If both x and y are 0, the heading is 0. Python will use `atan2(y, x)` for points that are not on those axes. You only need the axes and the 45° line `(1, 1)` by hand.

## Worked example

Convert 180° to radians: `180 x π / 180 = π`.

Wrap 190°: 190 − 360 = −170, which is already in (−180, 180].

Distance from (0, 0) to (3, 4): `sqrt(9 + 16) = sqrt(25) = 5`.

Heading of (0, 1): 90°.

## Problems

Use π ≈ 3.14159 if you need a decimal. Leaving an answer as a multiple of π is fine where it is exact.

1. Convert 90° to radians.

2. Convert π radians to degrees.

3. Convert −90° to radians.

4. Wrap each of these into (−180, 180]: 0, 180, −180, 190, −190, 360, 540.

5. Distance from (1, 1) to (1, 1). Distance from (−1, 0) to (2, 4).

6. Heading, in degrees, of (1, 0), (0, 1), (−1, 0), (0, −1), (0, 0), and (1, 1).

## How you know you are done

You can convert either way, wrap a messy angle, and get a 3-4-5 distance without a formula sheet. File `006` is next.

---

## Answers

1. `π / 2` radians, about 1.5708

2. `180°`

3. `−π / 2` radians, about −1.5708

4. 0 → 0; 180 → 180; −180 → 180; 190 → −170; −190 → 170; 360 → 0; 540 → 180  
   (540 − 360 = 180)

5. 0. From (−1, 0) to (2, 4): `dx = 3`, `dy = 4`, distance 5.

6. 0°, 90°, 180°, −90°, 0°, 45°
