# 002 — Milli, kilo, and not mixing them

Do `001` first.

Electronics almost never writes a current as `0.012 A` on a diagram. It writes **12 milliamps**. A **milliamp** (mA) is one thousandth of an amp, the same idea as a millimetre being one thousandth of a metre.

```
1 mA = 0.001 A
12 mA = 0.012 A
0.3 A = 300 mA
```

Resistances on a robot board are often thousands of ohms. One **kilohm** (kΩ) is one thousand ohms.

```
1 kΩ = 1000 Ω
4.7 kΩ = 4700 Ω
330 Ω = 0.33 kΩ
```

You will also meet **micro** (µ), which is one millionth. A **microfarad** (µF) is a common size for the capacitor that sits next to a chip's power pins. You do not need to calculate with farads in this file. You only need to recognise that µ means “divide by one million” if a later exercise asks you to.

Ohm's law only works when the three numbers use matching units: volts, amps, and ohms. If you put milliamps or kilohms into `V = I x R` without converting, the answer is usually wrong by a factor of a thousand. That is the most common arithmetic mistake in Module 1.

## Worked example

A 5 V supply and a 10 kΩ resistor. Find the current in amps, then in milliamps.

```
R = 10 kΩ = 10,000 Ω
I = V / R = 5 / 10,000 = 0.0005 A
I in milliamps = 0.0005 x 1000 = 0.5 mA
```

If you had done `5 / 10` and written `0.5 A`, you would be a thousand times too high. The check: 0.5 A through a 10 kΩ resistor would need `V = 0.5 x 10,000 = 5000 V`. That cannot come from a 5 V supply.

## Problems

1. Convert 25 mA to amps.

2. Convert 0.004 A to milliamps.

3. Convert 2.2 kΩ to ohms.

4. Convert 470 Ω to kilohms.

5. A 3.3 V supply and a 1 kΩ resistor. Find the current in amps and in milliamps.

6. A 5 V supply and a 220 Ω resistor. Find the current in milliamps.

7. You measure 2 mA through a 4.7 kΩ resistor. What voltage is across it? Convert both numbers before you multiply.

## How you know you are done

You convert first, then calculate, and you have a habit of asking “if I undo this with `V = I x R`, do I get the supply I started with?” File `003` is next.

---

## Answers

1. `0.025 A`

2. `4 mA`

3. `2200 Ω`

4. `0.47 kΩ`

5. `I = 3.3 / 1000 = 0.0033 A = 3.3 mA`

6. `I = 5 / 220 ≈ 0.0227 A ≈ 22.7 mA`

7. `I = 0.002 A`, `R = 4700 Ω`, `V = 0.002 x 4700 = 9.4 V`
