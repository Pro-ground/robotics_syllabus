# 003 — Sharing a voltage

Do `001` and `002` first. This is the arithmetic behind the two-resistor divider in the Falstad sheet.

When two resistors sit in a single loop, the same current goes through both, and the supply voltage is shared between them. Each resistor's share is in **proportion** to its value: a resistor that is twice as large as the other takes twice the voltage.

If the two values are `R1` (top, nearest the supply) and `R2` (bottom, nearest ground), the voltage at the join, measured to ground, is `R2`'s share of the total:

```
V_out = V_in x R2 / (R1 + R2)
```

Read that as a fraction, not as something to memorise as a new law. `R2 / (R1 + R2)` is the bottom resistor's share of the chain. That share of the input voltage appears at the output. You already know how to get the same number the long way: add the resistances, find the current with `I = V_in / (R1 + R2)`, then `V_out = I x R2`.

## Worked example

`V_in = 5 V`, `R1 = 1 kΩ`, `R2 = 1 kΩ`.

The two resistors are equal, so they share equally. Half of 5 V is 2.5 V.

The fraction: `1 / (1 + 1) = 1/2`, and `5 x 1/2 = 2.5 V`.

## Problems

Resistances in a ratio cancel their units, so you can leave both values in kilohms or convert both to ohms. Do not mix.

1. `V_in = 5 V`, `R1 = 1 kΩ`, `R2 = 3 kΩ`. What is `V_out`? First say the share as a fraction in words, then compute.

2. `V_in = 12 V`, `R1 = 10 kΩ`, `R2 = 2 kΩ`. What is `V_out`?

3. `V_in = 5 V`, `R1 = 3 kΩ`, `R2 = 1 kΩ`. What is `V_out`? Compare this with problem 1 and say in one sentence why the output is smaller.

4. You want `V_out = 1 V` from a 5 V supply. `R2` is 2 kΩ. What should `R1` be?

   You want the bottom share to be `1/5` of the total. So `R2` is one fifth of `R1 + R2`. Find `R1`.

5. Two 1 kΩ resistors in a single loop on 5 V. What current flows (in milliamps)? What voltage is across each resistor? The two voltages should add to 5 V.

## How you know you are done

You can estimate a divider in your head (“bottom is a quarter of the chain, so a quarter of the supply”) and only then do the arithmetic. That estimate is what catches the unit errors from `002`. File `004` is next. Do it before `004_timed_loop.py`.

---

## Answers

1. Bottom is 3 parts out of 4. `V_out = 5 x 3 / 4 = 3.75 V`

2. `V_out = 12 x 2 / (10 + 2) = 12 x 2 / 12 = 2 V`

3. `V_out = 5 x 1 / 4 = 1.25 V`. The bottom resistor is now the smaller share of the chain, so less of the 5 V appears across it.

4. `R2 / (R1 + R2) = 1/5`. So `2 / (R1 + 2) = 1/5`. Then `10 = R1 + 2`, and `R1 = 8 kΩ`.

5. Total resistance `2 kΩ = 2000 Ω`. `I = 5 / 2000 = 0.0025 A = 2.5 mA`. Each resistor: `V = 0.0025 x 1000 = 2.5 V`. The two drops add to 5 V.
