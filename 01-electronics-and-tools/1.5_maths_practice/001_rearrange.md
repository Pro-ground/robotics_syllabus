# 001 — Find the missing number

Do this file first. You need it for the Falstad exercises and for every resistor you size later.

A formula is a relationship written with symbols. The one you will use most in this module ties three things together:

- **Voltage**, in volts (V): the electrical push the battery provides
- **Current**, in amps (A): how much charge flows per second
- **Resistance**, in ohms (Ω): how much the circuit restricts that flow

Written one way, it says voltage equals current times resistance:

```
V = I x R
```

That is **Ohm's law**. The same relationship written to find current, or to find resistance, is still Ohm's law. Nothing new is added. You are only making the thing you want sit on its own on the left.

```
I = V / R
R = V / I
```

If you have any two, you can find the third. That is the whole skill.

## How to turn the formula around

Whatever you do to one side, do to the other, so both sides stay equal.

To get `I` from `V = I x R`, divide both sides by `R`. You get `V / R = I`.

To get `R` from `V = I x R`, divide both sides by `I`. You get `V / I = R`.

An answer is not finished until it has a unit. Amps times ohms gives volts. Volts divided by ohms gives amps. Volts divided by amps gives ohms.

## Worked example

A 5 V supply and a 1000 Ω resistor in a single loop. You want the current.

You know `V` and `R`, and you want `I`, so:

```
I = V / R = 5 / 1000 = 0.005 A
```

## Problems

Write the formula you will use, then the number and the unit.

1. A resistor has 12 V across it and a resistance of 400 Ω. What current flows through it?

2. A current of 0.02 A flows through a 220 Ω resistor. What voltage is across the resistor?

3. A resistor has 9 V across it and 0.03 A through it. What is its resistance?

4. A light-emitting diode, or **LED**, lets current through in one direction and drops a roughly fixed voltage once it starts conducting. That drop is the **forward voltage**. A red LED's forward voltage is about 2 V.

   You have a 9 V battery, that LED, and you want 0.02 A through the LED. The LED and a resistor sit in a single loop, so the voltages across them add up to 9 V. What voltage is left for the resistor? What resistance do you need?

5. Same idea as 4, with a 5 V supply, a 2 V forward voltage, and a target current of 0.01 A. Find the resistor.

## How you know you are done

You can pick the matching line of `V = I x R`, `I = V / R`, or `R = V / I` from what you know and what you want, without rereading the top of this file. File `002` is next.

---

## Answers

Check these after you have written yours.

1. `I = V / R = 12 / 400 = 0.03 A`

2. `V = I x R = 0.02 x 220 = 4.4 V`

3. `R = V / I = 9 / 0.03 = 300 Ω`

4. Voltage left for the resistor: `9 - 2 = 7 V`. Resistance: `R = 7 / 0.02 = 350 Ω`

5. Voltage left: `5 - 2 = 3 V`. Resistance: `R = 3 / 0.01 = 300 Ω`
