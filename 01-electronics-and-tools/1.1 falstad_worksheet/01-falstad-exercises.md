# Module 1: Falstad exercises

Use this alongside `01-electronics-and-tools.md` section 1.1. The last two exercises also cover the PWM and brownout ideas from section 1.2.

Simulator: [Falstad Circuit Simulator](https://www.falstad.com/circuit/). It runs in a browser and needs no account.

**Estimated time:** 6 to 10 hours for exercises A through M. Exercises A through G give you enough grounding to start the physical breadboard tasks. H through M cover the rest of the Module 1 electronics ideas that a simulator can show.

## Why bother with a simulator

Electronics is invisible. You cannot see voltage or current, so beginners tend to build circuits by copying pictures and hoping. A simulator makes the invisible part visible. You can hover over any wire and read the voltage, watch current flow as moving dots, and break things on purpose without buying replacements.

Being good at Falstad is not the point of these exercises. You are building a working picture in your head of how electricity behaves in a circuit, so that when you put real parts on a real breadboard you already know roughly what the meter should say before you touch it. Predicting a value and then checking it is the habit that makes debugging possible later on.

Falstad cannot teach you everything. It will not teach you LiPo battery safety, soldering, how to hold a multimeter probe, static discipline when handling chips, or any Python and Git. Those come later in the module.

## How to work through these exercises

Do them in order. Each one builds on the one before it.

Every exercise follows the same four steps.

1. **Build.** Put the circuit together in Falstad, but do not run it yet.
2. **Read.** Work out how the circuit is wired and decide which calculation you need. This happens on paper, with the simulator untouched.
3. **Predict.** Do the arithmetic and write the number down.
4. **Compare.** Run the simulator and see whether it matches what you wrote.

Step 2 is the one that matters and the one that is easy to skip. Arithmetic is rarely the hard part of electronics. Knowing which relationship applies to the circuit in front of you is the hard part, and you only get it by deciding for yourself rather than being told. The section **How to read a circuit** below is the method, and every exercise from B onwards will send you back to it.

Predicting before you run the simulator matters for the same reason. Building first and reading the answer off the screen teaches you very little, because you never had to commit to an expectation and find out you were wrong.

When your prediction and the simulator disagree, suspect your circuit before your maths, and your maths before Falstad. The most common causes are a wire that is not really connected and a missing ground.

## How to drive Falstad

- Pick a part from the **Draw** menu, then click two points on the canvas to place it.
- Use **File → New Blank Circuit** when you start each new exercise, so old parts do not confuse you.
- **Right-click a part, then choose Edit** to change its value, such as volts or ohms.
- Yellow shading shows voltage. Brighter yellow means higher voltage.
- Moving dots show current. The dots travel in the direction the current flows.
- Hover your mouse over any part or wire to read its voltage and current in the corner of the screen. This is your multimeter for these exercises.
- Always place a **ground** symbol (Draw → Outputs and Labels → Ground, or the ground in the Inputs and Sources menu). Voltage is always measured between two points, so without a ground the simulator has no zero to measure from.
- Resistors are drawn as a zigzag in the US and as a plain rectangle in Europe. Both symbols mean the same part, so use whichever appears.



### How connections work

Falstad only connects parts where their **endpoints** meet. A component has a small terminal at each end, and a wire has one at each tip. A connection exists when two of those terminals sit on the same point.

Laying a wire across the middle of another wire does not connect them. Dropping a resistor on top of a wire does not connect it either. Both look joined on screen while remaining electrically separate in the simulation, which is why a circuit can appear perfect and do nothing at all. This catches almost everyone at least once.

Two signs to watch for:

- A small **dot** where terminals meet means a real connection.
- A **red dot** means Falstad thinks you tried to connect to the middle of something. The simulator treats that point as disconnected.

If you need to attach a new branch partway along an existing wire, select that wire, right-click it, and choose **Split Wire**. That breaks the wire into two pieces and creates a real terminal in the middle, which you can then connect to.

Because of this, the easiest way to work is to build one complete loop first, confirm it behaves, and then add extra branches by drawing them from terminals that already exist.

### Symbol crib

Enough parts to complete this file.


| Thing                 | What to grab                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Battery               | Inputs and Sources → Voltage Source (2-terminal). Long stroke / `+` is positive            |
| Resistor              | Draw → Resistor                                                                            |
| Ground                | Ground symbol. One per circuit is enough if the negative battery terminal is also grounded |
| LED / diode           | Diodes → LED or Diode. Triangle points in the direction current is allowed                 |
| NPN transistor        | Transistors → NPN. Three pins: collector, base, emitter                                    |
| Capacitor             | Draw → Capacitor                                                                           |
| Switch                | Inputs and Sources → Switch (SPST). Space bar often toggles the last one                   |
| Lamp / motor stand-in | Outputs and Labels → Lamp, or a small resistor you treat as the motor                      |


---



## How to read a circuit

This is the most important section in the file. Every exercise from B onwards asks you to read the circuit before you calculate anything, and this is the method. Come back to it each time until you no longer need to.

The hard part of electronics is not the arithmetic. It is knowing which calculation applies. That turns out to be a question about **how the parts are wired together**, not about the numbers in front of you. There are only a handful of relationships available, and the wiring decides which one you need.

### Step 1: find the nodes

A **node** is a stretch of wire. Everything touching that wire is at the same voltage, no matter how much wire is involved or how many corners it turns.

Mark every node on the circuit and give each one a name. Ground is always 0 V, because that is what ground means. Most circuits in this file have three or four nodes.

Counting nodes is the single most useful habit here. Circuits that look tangled usually turn out to have very few nodes, and once they are marked the structure becomes obvious.

### Step 2: classify the parts

Take each pair of components and ask two questions.

- Do they share one node, with nothing else attached to that node? They are **in series**, so the same current flows through both.
- Do they share **both** of their nodes? They are **in parallel**, so the same voltage sits across both.

Write your answer down before continuing. Series means shared current. Parallel means shared voltage. Almost everything in this module follows from those two facts.

### Step 3: say what you know and what you want

One line each. For example: "I know the supply is 5 V and both resistors are 10 kΩ. I want the voltage at the node between them."

This feels like unnecessary bookkeeping and it is the step that makes the next one easy.

### Step 4: pick the move

There are six, and they cover everything in this module.


| If you have                                              | And you want               | Then                    |
| -------------------------------------------------------- | -------------------------- | ----------------------- |
| The voltage across a resistor and its value              | The current through it     | `I = V / R`             |
| The current through a resistor and its value             | The voltage across it      | `V = I x R`             |
| The voltage across a resistor and the current through it | Its resistance             | `R = V / I`             |
| Resistors in series                                      | Their combined value       | Add them                |
| Resistors in parallel                                    | Their combined value       | `(R1 x R2) / (R1 + R2)` |
| Branches leaving a node                                  | The current arriving at it | Add the branch currents |


The first three rows are one relationship written three ways. Ohm's law ties voltage, current and resistance together, so knowing any two of them gives you the third. There is nothing to memorise beyond `V = I x R` and the ability to rearrange it.

Often no single move gets you from what you know to what you want. When that happens, ask which intermediate quantity would bridge the gap, and go and find that first. Two moves in sequence is normal and is not a sign you have missed a shortcut.

### A note on the third row

In the exercises that follow you will rarely need `R = V / I`, because you always know the resistances. You chose them when you placed the parts. Resistance is an input here rather than something to find.

That changes as soon as you leave the simulator, and the row is in the table because of what comes later.

**Sensors whose resistance is the signal.** A thermistor, a light-dependent resistor, a flex sensor and a potentiometer all work by changing their resistance. A microcontroller can only measure voltage, so you read a voltage, work back to the resistance, and convert that into a temperature or a light level. That is exercise D run in reverse, and it is how most analogue sensors on a robot are read.

**Unmarked components.** Put a known voltage across one, measure the current, and divide.

**The internal resistance of a supply.** Measure the output voltage with nothing attached, then again while a known current is being drawn. The amount the voltage sagged, divided by that current, is the supply's internal resistance. Exercises J and K both hand you this figure as a given, and this is how you would obtain it for a real battery.

**Whole circuits rather than single parts.** Applied to a section of a circuit instead of one component, `R = V / I` gives its equivalent resistance. That is how you decide in advance whether attaching something will disturb a divider, which is the problem in exercise E expressed as a number.

### Step 5: check the answer

Three checks, all cheap enough to do every time.

- **Bounds.** No voltage in these circuits can exceed the supply. Calculating 7 V from a 5 V source means something has gone wrong.
- **Loops.** Walk round any closed loop adding the voltage drops. They come to the supply voltage. This is **Kirchhoff's voltage law**.
- **Nodes.** The current arriving at a node equals the current leaving it. This is **Kirchhoff's current law**.

Check the unit as well. Amps times ohms gives volts, and volts divided by ohms gives amps. An answer that is a bare number with no unit attached is not finished.

---



## A. One resistor in a loop

**Why you need it:** This exercise sets up the vocabulary for everything that follows. Voltage, current and resistance are the three quantities you will be reasoning about for the rest of the module, and the relationship between them is the calculation you will reach for most often.

This first exercise is the one place where the theory comes before the circuit, because you cannot read a circuit without knowing what the words mean. From exercise B onwards the order reverses.

### The groundwork

Three quantities describe what is happening in a simple circuit.

- **Voltage**, measured in volts (V), is the electrical push the battery provides.
- **Current**, measured in amps (A), is the rate of flow through the circuit.
- **Resistance**, measured in ohms (Ω), is how much the circuit restricts that flow.

A common analogy is water in a pipe. Voltage is the pressure behind the water, current is how much water flows per second, and resistance is how narrow the pipe is. More pressure gives more flow. A narrower pipe gives less flow.

Ohm's law states this as a formula.

```
current = voltage / resistance          I = V / R
```

Currents in small electronics are usually a fraction of an amp, so we write them in **milliamps** (mA). One milliamp is one thousandth of an amp, in the same way a millimetre is one thousandth of a metre. So 0.012 A is the same as 12 mA, and 0.3 A is the same as 300 mA. Resistances are usually in **kilohms** (kΩ), where one kilohm is one thousand ohms.

### Build

A 5 V source, one 1 kΩ resistor, and a ground on the negative side of the source, all in a single loop.

```
        ┌──────────────┐
        │              │
     [ 5 V ]        [ 1 kΩ ]
        │              │
        └──────┬───────┘
               │
              ─┴─
              GND
```

The top wire is the positive side of the source. Read the diagram as two vertical parts joined by a wire at the top and another at the bottom, which is the shape most of these exercises take.

Steps:

1. Place a voltage source from Inputs and Sources, then right-click it and set it to 5 V.
2. Place a resistor and right-click it to set 1 kΩ.
3. Draw wires so the circuit forms one closed loop from the positive terminal, through the resistor, and back to the negative terminal.
4. Attach a ground symbol to the negative terminal.

Every join must be terminal to terminal. There should be no red dots anywhere.

### Read the circuit

Work through the first three steps of **How to read a circuit** on this one. It is deliberately the simplest circuit in the file, so the answers are short.

1. How many nodes are there? Mark them.
2. Is anything in series with anything else? Is anything in parallel?
3. What do you know, and what do you want?

Answers to compare against, since this is the first time:

There are **two nodes**. One is the top wire joining the source's positive terminal to the top of the resistor. The other is the bottom wire joining the source's negative terminal, the bottom of the resistor and ground. Ground is on the bottom node, so that node is 0 V.

Nothing is in series or parallel with anything, because there is only one component besides the source.

Both ends of the resistor are attached to the source, so the resistor has the whole 5 V across it. You know the voltage across it and its value. You want the current.

Look back at the table in step 4. Knowing voltage and resistance and wanting current gives you exactly one move.

### Predict

```
I = V / R = 5 / 1000 = 0.005
```

Write down the current in amps, then convert it to milliamps. Also write down what you expect the voltage across the resistor to be.

### Check

Hover over the resistor. Compare the current and voltage in the readout against the two figures you wrote down. Watch the moving dots travel round the loop.

If the current reads zero, the loop is not closed. Look for a gap or a red dot.

### Change

Right-click the resistor and set it to 2 kΩ. Predict first, then check.

```
I = V / R = 5 / 2000 = 0.0025
```

Now set it to 500 Ω.

```
I = V / R = 5 / 500 = 0.01
```

Before checking either one, say in words what you expect to happen to the current when the resistance doubles, and then when it halves. Note whether the voltage across the resistor changes at all, and why.

### Write

Answer this in one sentence in your notes: if the voltage stays the same and the resistance goes up, what happens to the current, and why.

### What you just built

The relationship you used is **Ohm's law**, and it is the most used calculation in electronics. Picking a resistor for an LED, working out what a sensor draws, checking whether a wire is thick enough: all Ohm's law.

Note what actually told you to use it. Not the heading, and not the numbers. You knew the voltage across a component and its resistance, and you wanted the current. That combination has exactly one move attached to it. Every exercise from here works the same way, and from now on you find the combination yourself.

---



## B. Two resistors in a single loop

**Why you need it:** Real circuits are chains of parts rather than single resistors, and you need to know how a supply voltage gets shared out along that chain.

### Build

A 9 V source, then a 3 kΩ resistor, then a 6 kΩ resistor, then back to the source. Ground goes on the negative terminal.

```
        ┌──────────────┐
        │              │
        │           [ 3 kΩ ]
        │              │
     [ 9 V ]           ●  A
        │              │
        │           [ 6 kΩ ]
        │              │
        └──────┬───────┘
               │
              ─┴─
              GND
```

The point marked A is where the two resistors meet.

Steps:

1. Place the source and set it to 9 V.
2. Place the 3 kΩ resistor, joining one end to the positive terminal.
3. Place the 6 kΩ resistor so one end sits on the **same terminal** as the free end of the 3 kΩ.
4. Wire the far end of the 6 kΩ back to the negative terminal and attach a ground there.

You should see a connection dot where the two resistors meet.

### Read the circuit

Do not calculate anything yet. Work through the steps in **How to read a circuit** and write your answers down.

1. **Nodes.** How many are there? Which one is at 0 V?
2. **Classify.** Look at node A. What is attached to it, and how many things? Does that make the two resistors series or parallel? What does your answer tell you about the current in each one, or the voltage across each one?
3. **Know and want.** You know the voltage and both resistor values. Say what you want to find.
4. **Pick the move.** Check your answer to question 3 against the table. Can you get there in one move, or do you need an intermediate quantity first? If you need one, name it before you go on.

Question 4 is the one worth sitting with. You want the voltage across a resistor, and the table says that needs the current through it. You do not have the current yet, so finding it is your intermediate step. That is the shape of most circuit problems.

### Predict

Fill in the blanks. The first two lines are the intermediate step you identified.

```
R_total = 3 kΩ + 6 kΩ = 9k
I       = 9 / R_total = 0.001
```

Now the quantity you actually wanted, using the current you just found.

```
across the 3 kΩ:  I x 3000 = 3
across the 6 kΩ:  I x 6000 = 6
```

Before touching the simulator, run the checks from step 5. Add your two voltage drops. Do they come to the supply voltage? Is either one larger than the supply? If the loop check fails, find the error now rather than after building.

Also predict which resistor takes the larger share, and what ratio you expect between the two drops.

### Check

Hover over each resistor in turn and compare against your figures. Confirm your answer to question 2 while you are there, by seeing whether the currents match or the voltages match.

Now hover node A itself. Work out what it should read against ground before you look. Ask yourself which components sit between node A and ground, and what that means.

### Break it

Now short out the 6 kΩ resistor. Shorting means giving the current an easier path around a part, like clipping a plain copper wire across both of its legs. Almost all the current takes the wire instead, so the resistor is effectively removed from the circuit.

To do this in Falstad, draw a wire starting exactly on one terminal of the 6 kΩ and ending exactly on its other terminal. Both ends of the resistor already have terminals, so this is a normal terminal to terminal connection and does not need Split Wire. If nothing changes when you run it, your wire ends missed those terminals.

Predict what happens before you run it. Only the 3 kΩ is left doing anything.

```
I = 9 / 3000 = ?
```

Work out the new current, then say what you expect the voltage across the 3 kΩ to be, and what you expect across the 6 kΩ now that both of its ends are the same electrical point. Then run it and compare all three figures.

### Write

Answer these two in your notes. In a series circuit, how does the current at one point compare with the current at any other point. And what decides how much of the supply voltage each resistor takes.

### What you just built

Node A had exactly two things attached to it, and that is the test for **series**. Parts in series form a single path, so the same current flows through all of them, and the supply voltage gets shared between them in proportion to their resistance. Each part's share is called its **voltage drop**.

Two rules for your toolkit.

```
resistors in series:  R_total = R1 + R2
voltage drop:         V = I x R          (using that resistor's own value)
```

The check you ran, where the two drops added back to the supply, is **Kirchhoff's voltage law**. It is worth getting into the habit of, because it lets you verify a series calculation without the simulator.

Notice the order you had to work in. You wanted a voltage, but the only route to it ran through the current, so you found the current first. Recognising that you need an intermediate quantity, and knowing which one, is most of the skill.

---



## C. Two resistors side by side

**Why you need it:** Everything on a robot hangs off the same power rail. The microcontroller, the sensors and the motor driver are all connected across the battery at the same time, and you need to know what that adds up to. The answer decides your battery size, your wire thickness and your fuse rating.

### What changed since B

Exercise B had one path. This one has two. Before you read the build, note that this is the only structural difference between the two circuits, and watch how much follows from it.

### Build

A 5 V source with ground on its negative terminal, and two 1 kΩ resistors, each running from the positive rail down to ground.

```
        ┌──────────┬──────────┐
        │          │          │
     [ 5 V ]   [ 1 kΩ ]   [ 1 kΩ ]
        │          │          │
        └────┬─────┴──────────┘
            ─┴─
            GND
```

Compare this with the diagram in exercise B, where the two resistors sat one above the other in a single path. Keep both diagrams side by side while you work, because the comparison is the point of this exercise.

Because both resistors must land on the same two nodes, build this in stages.

1. Build a single loop exactly as in exercise A: 5 V source, one 1 kΩ resistor, ground on the negative. Confirm it shows the same current it did in exercise A.
2. Add the second 1 kΩ resistor by drawing it **from terminals that already exist**. The simplest choice is to start on the top terminal of the first resistor and finish on its bottom terminal.
3. If you would rather branch off partway along a rail, select that wire, right-click it, and use **Split Wire** to create a real terminal there first. Then draw the resistor from that new terminal.

You should see a connection dot where the two resistor tops meet, and another where the two bottoms meet. If either resistor reads 0 mA when you run the circuit, that branch never actually joined the rails.

### Read the circuit

Again, no arithmetic yet.

1. **Nodes.** How many are there? This is the question that separates this circuit from exercise B, so count carefully. How many components attach to the top node?
2. **Classify.** Apply the two tests from step 2. Do the resistors share one node or both? Which of series or parallel does that make them, and does it mean they share a current or share a voltage?
3. **Know and want.** Your answer to question 2 gives you something for free that you had to calculate in exercise B. Work out what it is, then decide what you still need.

There are **three** places current flows here, and they are different from each other: through the first resistor, through the second resistor, and along the wire out of the battery. Be specific about which one you are asked for, because that trips people up more than the arithmetic does.

### Predict

Start with one branch. Question 2 should have told you what voltage sits across it without any calculation.

```
each branch:  I = 5 / 1000 = 0.005
```

Now the battery wire. It is a different place in the circuit from either resistor, so neither branch figure answers it directly. Look at the top node and ask what arrives there and what leaves.

```
battery current = branch 1 + branch 2 = 0.01
```

Now get that same battery figure by a second route, treating the two resistors as one combined resistance.

```
R_total = (1000 x 1000) / (1000 + 1000) = 500
I       = 5 / R_total = 0.01
```

Two independent routes agreeing is a stronger check than either one alone. If they disagree, find out which is wrong before you build. Note also whether the combined resistance came out larger or smaller than a single 1 kΩ, and see whether you can say why that makes sense.

### Check

Hover each 1 kΩ resistor and compare with your branch figure. Hover the wire coming out of the positive terminal and compare with your battery figure. Note what voltage each resistor has across it, and whether that matches what you assumed when you did the maths.

### Change

Right-click one resistor and set it to 2 kΩ. Predict all three figures first.

```
1 kΩ branch:  5 / 1000  = 0.005
2 kΩ branch:  5 / 2000  = 0.0025
battery:      branch 1 + branch 2 = 0.0075
```

Before checking, also predict whether the voltage across either branch changes, and whether the current in the 1 kΩ branch is affected at all by what happened in the other one.

Compare that with exercise B, where changing one resistor changed the current everywhere. Say in one sentence why the two circuits behave differently under the same edit.

### Write

Answer these two in your notes. In a parallel circuit, what do all the branches have in common. And how do you work out the current the supply has to provide.

### What you just built

Both resistors landed on the **same two nodes**, which is the test for **parallel**. Parallel parts share a voltage, in the way that series parts share a current. That is the whole difference between B and C, and everything else follows from it.

Two more rules for the toolkit.

```
resistors in parallel:  R_total = (R1 x R2) / (R1 + R2)
current into a node  =  current out of it
```

The second one is **Kirchhoff's current law**, and it is what justified adding the branch currents to get the battery current. Charge does not pile up at a junction, so whatever arrives has to leave.

The combined resistance came out **smaller** than either resistor on its own, which catches people out at first. Adding a second path makes it easier for current to flow, so the total resistance falls.

You have now used every move in the table apart from `R = V / I`, which waits until you meet a component whose resistance you do not already know. Everything from here is a matter of spotting which ones apply.

---



## D. Reading the voltage between two resistors (Module 1 Mandatory)

**Why you need it:** Robot parts run at different voltages. A sensor might output 5 V while your microcontroller only tolerates 3.3 V on its pins, and feeding it 5 V can destroy the pin. This circuit is the standard way to scale a voltage down safely, and it is also how a potentiometer, a joystick and a battery level monitor all work. This is practice task 1 in the syllabus.

### What changed since B

Nothing about the wiring. This is the same shape as exercise B, a chain of two resistors running from the supply down to ground. The only thing that changed is the question.

In B you wanted the voltage **across** a resistor. Here you want the voltage **at the point between the two resistors**, which is called the **mid node**. Voltage is always a difference between two places, so "the voltage at a point" is shorthand for "the voltage between that point and ground".

Work out for yourself which resistor sits between the mid node and ground, and what that tells you.

### Build

A 5 V source with ground on its negative terminal. A top resistor R1 of 10 kΩ running from the positive rail down to the mid node, and a bottom resistor R2 of 10 kΩ running from the mid node down to ground.

```
        ┌──────────────┐
        │              │
        │          [ 10 kΩ ]  R1
        │              │
     [ 5 V ]           ●─── V_out
        │              │
        │          [ 10 kΩ ]  R2
        │              │
        └──────┬───────┘
               │
              ─┴─
              GND
```

The whole exercise depends on both resistors genuinely sharing that middle terminal, so build it in this order.

1. Place the 5 V source and attach ground to its negative terminal.
2. Draw R1 starting at the positive terminal and ending at an empty point below it. That lower end is your mid node. Leave it as a free terminal for now.
3. Draw R2 starting on that **same** terminal and ending at ground.
4. Look for a connection dot at the mid node. If you built it as one long wire first, use **Split Wire** at the midpoint to create a real terminal before attaching anything there.



### Read the circuit

1. **Nodes.** How many, and which is at 0 V? How many components touch the mid node?
2. **Classify.** Series or parallel? Which test did you apply to decide?
3. **Know and want.** You want the voltage at the mid node. Rewrite that as a voltage across a component, so that it matches something in the table.
4. **Pick the move.** With the question rewritten, which row of the table applies? Do you have everything that row needs, or is there an intermediate quantity to find first?

If question 3 stalls you, the useful move is to notice that the mid node and ground are the two ends of R2. So the voltage at the mid node **is** the voltage across R2, and that is now a question the table can answer.

### Predict

Work through the route you identified. The intermediate quantity comes first.

```
R_total = 10 kΩ + 10 kΩ = 20 kΩ
I       = 5 / R_total   = 0.00025
```

Then the voltage across R2, which is what you actually wanted.

```
V_out = I x R2 = 2.5
```

Watch your units on that last line. R2 is 10 kΩ, which is 10,000 Ω, and your current is in amps rather than milliamps. Mixing the two is the single most common slip in this exercise, and it gives answers that are wrong by a factor of a thousand.

Run the bounds check. Is your answer between 0 V and 5 V? Work out the drop across R1 as well, and confirm the two drops add to 5 V.

### Estimate it without calculating

Now try it a different way, with no arithmetic at all. R2 is half the total resistance in the chain. Series resistors share the supply in proportion to their value. So what share of 5 V should appear across R2?

If that reasoning gives you the same answer as your calculation, you have understood the circuit rather than followed a recipe. This estimate is worth doing on every divider you ever meet, because it catches unit errors instantly.

### Check

Hover the mid node and compare with your predicted output. Hover each resistor and check the current is the same through both, and that each drop matches what you calculated.

If the mid node reads 0 V, R2 is probably shorting to ground through a stray wire. If it reads the full 5 V, R2 is likely not connected at all.

### Change

Set R2 to 30 kΩ. Before calculating anything, use the share reasoning to say which direction the output will move and roughly how far. Then calculate it properly and see if you were right.

```
R_total = 10 kΩ + 30 kΩ = 40 kΩ
I       = 5 / R_total   = 0.000125
V_out   = I x R2        = 3.75
```

Say which direction you expect the **current** to move, and why that is a separate question from what happens to the output voltage.

Then work backwards for once. Pick resistor values that should give you 1 V out, and then 4 V out, and check whether they do. Working backwards is how you will actually use this circuit in practice, since you normally know the voltage you need and have to choose parts to get it.

### Write

Answer this in your notes: which resistor would you change, and in which direction, to raise the output voltage without changing the supply. Then say why.

### What you just built

This is a **voltage divider**, and it is one of the most common circuits in existence. The shorthand, with R1 on top and R2 at the bottom, is:

```
V_out = V_in x R2 / (R1 + R2)
```

That formula is not a new move. It is the two moves you already used, Ohm's law for the current and Ohm's law for the drop, collapsed into one line. Check that for yourself by substituting `I = V_in / (R1 + R2)` into `V_out = I x R2`.

Read it as a fraction rather than a formula. R2's share of the total resistance is the share of the input voltage that appears at the output. That is the estimate you did above, and it is the version worth memorising, because you can do it in your head and it tells you when a calculated answer is nonsense.

---



## E. Attaching a third resistor to the middle of the divider

**Why you need it:** This is one of the most common beginner faults in real projects. The divider works perfectly on its own, you connect it to a microcontroller input, and the reading comes back wrong. Understanding why saves hours of chasing a fault that is not really a fault. It also teaches you that connecting a measuring device to a circuit changes the circuit.

### What changed since D

Exercise D assumed nothing else was attached to the mid node. In a real design, something always is, whether that is a microcontroller input, another chip, or a transistor being driven. The general term for the thing you attach is the **load**, and here it is a single resistor called R_L standing in for whatever that component looks like electrically.

This exercise is the first one that needs both of the shapes you have learned in the same circuit. Part of it is series and part of it is parallel, and the work is in seeing where one ends and the other begins.

### Build

Start from the finished exercise D with R1 and R2 both 10 kΩ. Read the mid node and write that figure down as your baseline before you change anything.

Then add a third resistor R_L of 10 kΩ from the mid node down to ground.

```
        ┌──────────────┐
        │              │
        │          [ 10 kΩ ]  R1
        │              │
     [ 5 V ]           ●──────────┐   V_out
        │              │          │
        │          [ 10 kΩ ]  [ 10 kΩ ]
        │             R2         R_L
        │              │          │
        └──────┬───────┴──────────┘
               │
              ─┴─
              GND
```

R_L must start on the same terminal that R1 and R2 already share, and end on the same ground node they use. Draw it from that existing mid node dot straight to the ground terminal. When you are done, three components meet at the mid node.

If the output has not changed at all after you add R_L, the load did not actually connect.

### Read the circuit

1. **Nodes.** Has the number of nodes changed since exercise D? How many components now touch the mid node?
2. **Classify.** Apply both tests to each pair. Are R2 and R_L series or parallel with each other? Is R1 series or parallel with either of them? You should find that the answer differs depending on which pair you look at.
3. **Simplify.** You know how to handle two resistors in parallel, and you know how to handle a chain of two in series. Neither move on its own describes this whole circuit. So which pair would you collapse into a single equivalent resistor first, to turn this into a circuit you have already solved?
4. **Know and want.** State the target the same way you did in D, as a voltage across something rather than a voltage at a point.

Question 3 is the new skill. When a circuit is not a shape you recognise, look for a sub-section of it that is, replace that sub-section with its equivalent value, and see whether what is left is now familiar. Most circuit analysis is this move repeated.

### Predict

Collapse the pair you identified in question 3.

```
R_bottom = (10000 x 10000) / (10000 + 10000) = 5000
```

The circuit is now R1 in series with R_bottom, which is exactly exercise D with a different bottom value. Solve it the way you solved D.

```
V_out = 5 x R_bottom / (10000 + R_bottom) = 1.66
```

Before you check, do the estimate rather than trusting the arithmetic. What share of the total resistance is R_bottom now, and what share of 5 V should that put at the output?

Compare against the baseline you wrote down. Nothing about R1, R2 or the supply changed, so any difference comes purely from connecting the load.

### Check

Read the mid node with R_L removed, then with R_L attached, and compare both against your figures.

Now verify your answer to question 2 by measurement. Hover R2 and R_L and see whether they share a voltage or a current. Then add their two currents and compare the total against the current through R1, which checks Kirchhoff's current law at the mid node.

### Change

Try a much larger load resistor, say 1 MΩ, which is 1000 kΩ.

Before calculating, predict the direction and rough size of the effect. A very large resistor in parallel with a small one barely changes the combination, so ask yourself whether the output should move a lot or hardly at all.

```
R_bottom = (10000 x 1000000) / (10000 + 1000000) = 9900.99009901
V_out    = 5 x R_bottom / (10000 + R_bottom) = 2.487562189
```

Then try a small load of 1 kΩ, again predicting the direction first.

```
R_bottom = (10000 x 1000) / (10000 + 1000) = 909.090909091
V_out    = 5 x R_bottom / (10000 + R_bottom) = 0.416666667
```

Compare the three loads you have now tried and write down roughly how large a load has to be, relative to the divider resistors, before you can ignore it.

### Write

Explain in your own words why a divider that measured correctly on its own reads differently once something is attached to the output. Say what the load does electrically, and what decides how large an effect it has.

Then answer one design question. Very large divider resistors waste almost no current, which sounds like the better choice. What is the drawback, based on what you saw in the Change step.

### What you just built

This is a **loaded divider**, and the reason it behaves differently is that the load sits in parallel with R2, lowering the effective bottom resistance and so lowering R2's share of the supply.

No new formula was needed. You used the parallel rule from C and the divider from D, one after the other. What was new was **deciding to collapse part of the circuit first**, and that is the technique that carries you through everything more complicated than a single loop.

The habit worth taking away: when a circuit does not match a shape you know, do not look for a bigger formula. Look for the piece of it that is a shape you know, replace that piece with one equivalent resistor, and ask the question again.

There is also a general lesson about measurement. Attaching anything to a circuit changes it, which includes attaching a meter. Real multimeters have a very high resistance for exactly the reason you saw with the 1 MΩ load.

---



## F. Introduction to LEDS

**Why you need it:** Almost every project has an indicator LED, and every one of them needs a resistor sized correctly. Get it wrong and the LED burns out in seconds. Diodes also protect circuits from reversed batteries and from the voltage spikes motors produce when they switch off, both of which come up later in the course.

### The new component

Every exercise so far used only resistors. This one introduces a part that does not obey Ohm's law, so you need to know what it does before you can reason about the circuit.

A **diode** allows current to flow in one direction only. Turn it around and it blocks. The schematic symbol is a triangle pointing at a bar, and the triangle points the way current is allowed to travel. An **LED** is a diode that emits light while current passes through it.

The two ends have names. The **anode** is the positive side where current enters, and the **cathode** is the negative side where it leaves. On the symbol the cathode is the bar. On a real LED it is the shorter leg, next to a flat edge on the plastic body.

Here is the part that matters for the calculation. A resistor's voltage drop **depends on** the current through it, which is what `V = I x R` says. A diode instead drops a roughly **fixed** voltage once it starts conducting, no matter how much current flows. That fixed drop is called the **forward voltage**, written V_f, and it is a property of the part rather than something you can calculate. A red LED is usually 1.8 V to 2.2 V, and a plain silicon diode is about 0.7 V.

A diode has no useful resistance value, so none of the patterns in the table above apply to it directly. The point of this exercise is to figure out how to address this.

### Build

A single loop: 5 V source, a 330 Ω resistor, an LED, then back to ground.

```
        ┌──────────────┐
        │              │
        │          [ 330 Ω ]
        │              │
     [ 5 V ]           ▼     anode side, current enters here
        │             ───    cathode bar, facing ground
        │              │
        └──────┬───────┘
               │
              ─┴─
              GND
```

The triangle and the bar together are the LED. The triangle points the way current is allowed to travel, which here is downwards towards ground. Turn the symbol upside down and the circuit blocks instead.

1. Place the source and set 5 V, with ground on the negative terminal.
2. Place the 330 Ω resistor with one end on the positive terminal.
3. Place the LED so its anode joins the free end of the resistor and its cathode faces ground. The cathode is the bar end of the symbol.
4. Wire the cathode to ground.

Each join is terminal to terminal, the same as the series circuit in exercise B.

### Read the circuit

1. **Nodes.** How many, and which is at 0 V?
2. **Classify.** Is the resistor in series or parallel with the LED? What does that tell you about their currents?
3. **Know and want.** You want the current. Which of the two components can you apply Ohm's law to, and which can you not, and why?
4. **Find the missing piece.** Ohm's law on the resistor needs the voltage across the resistor, and you have not been given it. You have been given the supply voltage and, once you look it up, the LED's forward voltage. Which of the checks from step 5 relates those three quantities to each other?

Question 4 is the whole exercise. Kirchhoff's voltage law says the drops around the loop add to the supply. There are two drops, you know one of them, so the other one falls out by subtraction. The law you have been using as a **check** is being used here as a **tool**, and that is a common move once circuits contain parts you cannot apply Ohm's law to.

Note also what your answer to question 2 buys you. The two parts are in series, so the current you find in the resistor is the current in the LED as well. You never have to calculate anything about the LED itself.

### Predict

Right-click the LED and choose Edit to read its forward voltage, since Falstad's default varies. Write that figure down and use it as V_f.

First the missing voltage, using Kirchhoff's voltage law on the loop.

```
voltage across the resistor = 5 - V_f = ?
```

Now the current, using the only component you can apply Ohm's law to.

```
I = (voltage across the resistor) / 330 = ?
```

Convert to milliamps and judge it against the 5 mA to 20 mA range a small LED is happy with. Sizing that resistor so the current lands in a sensible range is the actual engineering task here, and it comes up in the Module 1 assessment.

### Check

Hover the LED and then the resistor. The current is the same through both because there is one path. Compare the current with your prediction, and compare each component's voltage with the figures you used. The LED should be lit on screen.

If the current reads zero and the LED is dark, either the LED is facing the wrong way or a connection is open.

### Reverse the LED

Delete the LED and place it the other way round, so the cathode faces the supply. Predict what the current will do, then run the circuit again.

Nothing is damaged by this, and the circuit simply does not do its job. This is why component orientation on a schematic matters, and why you will spend real time checking which way round parts go on a breadboard.

### Change

Try each of these resistor values. Predict the current before checking, and note how bright you expect the LED to be.

```
150 Ω:   (voltage across the resistor) / 150   = ?
330 Ω:   (voltage across the resistor) / 330   = ?
1 kΩ:    (voltage across the resistor) / 1000  = ?
10 kΩ:   (voltage across the resistor) / 10000 = ?
```

Before you calculate the second, third and fourth, answer one question. Does the numerator change when you change the resistor? Work out why or why not from what you know about the LED, because it is the thing that makes this component different from a resistor.

Watch the brightness change as you go, and note which of the four you would actually choose for an indicator LED.

### Optional

Swap the LED for a plain silicon diode, which has a forward drop of about 0.7 V.

```
voltage across the resistor = 5 - 0.7 = ?
I = (voltage across the resistor) / 330 = ?
```

Predict whether this gives more or less current than the LED did, and explain why in terms of how much voltage was left over. Then reverse it and confirm the current collapses in the same way.

### Write

One sentence on why an LED needs a series resistor, and one sentence on what happens when a diode is connected backwards.

### What you just built

This is a **current-limiting resistor** in series with an LED, and it is one of the most common arrangements in electronics. The shorthand is:

```
I = (V_supply - V_f) / R
```

That is not a new move either. It is Kirchhoff's voltage law to find the leftover voltage, then Ohm's law on the resistor, written as one line. You derived it above.

The reason the resistor is essential comes out of the fixed drop. An LED does not limit its own current, so connected straight across a battery it draws whatever the battery can deliver and destroys itself. The resistor takes the leftover voltage and sets the current to something survivable.

The transferable idea is the one from question 4. When a circuit contains something you cannot apply Ohm's law to, look for what you **do** know about it. Usually that is a fixed voltage drop, and Kirchhoff's voltage law converts a known voltage somewhere into an unknown voltage somewhere else. Exercise G has a component with two of these fixed drops in it.

---



## G. Using a transistor as a switch (Module 1 Mandatory)

**Why you need it:** A microcontroller pin can only supply a tiny current, usually around 20 mA or less, and drawing more than that damages the chip. Motors, relays, lamps and strips of LEDs all need far more. The transistor is the part that bridges that gap. Every motor driver and every relay board on your robot contains this circuit, so understanding it means you can read and repair those boards rather than treating them as mystery modules. This is practice task 2 in the syllabus.

### The new component

A **transistor** is a component where a small current at one terminal controls a much larger current between the other two. Think of a tap. A light touch on the handle controls a flow of water your hand could never push by itself. The handle is the small control input and the water is the load current.

An **NPN transistor** has three terminals.

- The **base** is the control terminal, where a small current flows in.
- The **collector** is where the large load current enters.
- The **emitter** is where both currents leave, usually to ground.

In Falstad it is normally drawn with the collector at the top, the emitter at the bottom, and the base sticking out to the side. The emitter is the terminal with the small arrow on it, and you can hover any pin to confirm which is which.

Feed a small current into the base and the transistor turns on, allowing current to flow from collector to emitter. Remove the base current and it turns off. That is all a switching transistor does.

Two facts about it are what make the arithmetic possible, and both are the same kind of fact you met in exercise F. The base to emitter junction behaves like a diode, so it drops about **0.7 V** when conducting. And when the transistor is fully on, the collector to emitter path drops only a small voltage, typically about **0.2 V**.

Those are fixed drops, given to you rather than calculated. Keep exercise F's lesson in mind, since it is the one this exercise leans on.

### Build

Two parts, built one at a time.

```
        ┌───────────────────┐
        │                   │
        │              [ 220 Ω ]
        │                   │
        │                   ▼   LED
        │                  ───
     [ 5 V ]                │
        │              ─────┴─────
        │              │    C    │
        │              │   NPN   │── B ──[ 1 kΩ ]──┐
        │              │    E    │                 │
        │              ─────┬─────             [ 3.3 V ]
        │                   │                      │
        └───────────────────┴──────────────────────┘
                            │
                           ─┴─
                           GND
```

**The load side**, which is the circuit being switched:

1. Place a 5 V source with ground on its negative terminal.
2. From the positive terminal, place a 220 Ω resistor, then an LED with its cathode pointing towards the transistor.
3. Place an NPN transistor from the Transistors menu. Connect the LED cathode to the **collector**.
4. Connect the **emitter** to ground.

**The control side**, which stands in for a microcontroller pin:

1. Place a second voltage source and set it to 3.3 V.
2. Draw a 1 kΩ resistor from its positive terminal to the **base** of the transistor. The base is already a terminal, so connect straight to it.
3. Connect the 3.3 V source's negative terminal to the **same ground** used by the 5 V source and the emitter.

That last step is the one people get wrong. Two ground symbols placed near each other are only connected if they truly share a node. Draw the wire from an existing ground terminal, using Split Wire if you need a junction partway along.

If the LED refuses to light, check three things in order. Is the LED the right way round, did the 1 kΩ resistor actually land on the base pin, and do both supplies share a ground.

### Read the circuit

This is the biggest circuit in the file so far, and the first thing to notice is that it is not one circuit.

1. **Trace the loops.** Start at the positive terminal of the 5 V source and find your way back to it. Then do the same from the 3.3 V source. You should find two separate loops that meet at the transistor. Sketch each one on its own.
2. **Nodes.** Count them for the whole circuit. Which node do both loops have in common?
3. **Classify, one loop at a time.** In the left loop, what is in series with what? Same question for the right loop. Neither loop should be complicated once it is on its own.
4. **Know and want.** There are two currents to find, one per loop. For each, list the fixed voltage drops you were given and the one resistor you can apply Ohm's law to.
5. **Pick the move.** Each loop is now exercise F in a different arrangement. Which two moves, in which order?

The technique in question 1 is worth naming. A circuit with more than one source is usually best handled as several simple circuits that share a node, not as one complicated circuit. Splitting it that way is often the entire difficulty.

Question 2 has an answer that matters. Both loops return through the emitter to the **same ground**, and if they did not, the control current would have no path back to its source. That is not a tidiness rule but a requirement for the circuit to function.

### Predict

**The control loop.** Work out the leftover voltage first, exactly as you did with the LED in exercise F, then apply Ohm's law to the only resistor in that loop.

```
voltage across the 1 kΩ = 3.3 - 0.7 = ?
I_base                  = (voltage across the 1 kΩ) / 1000 = ?
```

**The load loop.** This one has two fixed drops in it rather than one, the LED's forward voltage and the transistor's 0.2 V. Read V_f from the LED's Edit dialog. Subtract both from the supply, then apply Ohm's law to the 220 Ω.

```
voltage across the 220 Ω = 5 - V_f - 0.2 = ?
I_collector              = (voltage across the 220 Ω) / 220 = ?
```

Compare your two currents and write down the ratio between them. That ratio is the point of the whole circuit, so make sure you are struck by it before moving on.

Then think ahead. If the LED were swapped for a motor drawing a full amp, which of your two figures would change and which would stay the same?

Finally, predict what happens when the 3.3 V source is set to 0 V, in terms of the base current first and the LED second.

### Check

Toggle the control source between 3.3 V and 0 V by editing its voltage, and confirm the LED follows.

Hover the 1 kΩ resistor to read the base current and the 220 Ω resistor to read the load current. Compare both against your predictions, and confirm which of the two is larger.

### Break it

Delete the wire joining the 3.3 V source's negative terminal to the main ground, so the two supplies each have their own separate ground.

The circuit stops working properly. Nothing looks broken on screen, every part is still in place, and the control current has no complete path back to its source. Reconnect the wire and confirm normal behaviour returns.

Remember this one. A missing common ground is among the most frequent faults in real robot wiring, especially when a project has a separate battery for the motors and another supply for the electronics.

### Write

Explain why the microcontroller pin does not have to supply the LED current, and where that current actually comes from. This is the circuit that later allows a 3.3 V pin on an ESP32 to control a motor driver.

### What you just built

This is a **transistor used as a low-side switch**, and it is how almost every microcontroller controls anything that draws real current. The pin supplies the small base current, and the load current comes from the main supply through a path the pin never touches. That is why a 3.3 V pin rated for a few milliamps can control a motor driver.

No new formula appeared. Both halves were exercise F: subtract the fixed drops using Kirchhoff's voltage law, then Ohm's law on the resistor. The only thing that grew was the number of times you did it.

Three things worth carrying forward.

**Split multi-source circuits into loops.** The circuit looked hard and turned out to be two easy circuits sharing a node. Whenever a schematic has more than one supply, find the loops before you do anything else.

**Fixed drops accumulate.** The load loop had two of them. Subtract every fixed drop in the loop from the supply, and whatever is left belongs to the resistors.

**A shared ground is part of the circuit.** The next section demonstrates this, and it is worth doing rather than reading, because nothing looks wrong on screen when it is missing.

---



## H. Holding an input at a known voltage

**Why you need it:** Every button, switch and limit sensor on your robot connects to an input pin, and none of them work reliably without this. Beginners wire a button straight to a pin, find it triggers at random, and conclude the button is faulty when the real cause is a pin left floating. It is a small idea that prevents a whole category of frustrating bugs.

### The problem this solves

A microcontroller input pin senses the voltage applied to it and sorts what it sees into two categories. A voltage near the supply reads as **high**, usually written as 1 or true. A voltage near ground reads as **low**, written as 0 or false.

The problem is what happens when a pin is connected to nothing at all. This is called **floating**. With no path to either the supply or ground, the pin has no defined voltage. Tiny amounts of electrical noise from nearby wires, from the mains, and even from your hand moving near the board are enough to push it around. The pin reads high, then low, then high again, with no input from you.

Now think about a simple push button. When it is pressed, it connects the pin to something. When it is released, it connects the pin to nothing, and the pin floats. So half of the button's behaviour is undefined.

The two builds below each add one resistor to fix this. Your job is to work out what each arrangement does before you run it.

### A new thing to read: switches

A switch changes the shape of the circuit rather than the values in it, which means you have to read the circuit **twice**, once for each position.

For analysis purposes, treat a closed switch as a plain wire with no resistance, so the two nodes it joins become one node at the same voltage. Treat an open switch as an infinite resistance, so no current flows through that branch at all and it may as well not be drawn.

Redrawing the circuit twice, once with the switch as a wire and once with the branch deleted, turns one confusing circuit into two easy ones. Do that on paper for both builds below.

### Build A

The switch goes between the pin and the supply, and the resistor goes between the pin and ground.

```
        ┌──────────┐
        │          │
        │          o
        │           \   switch
        │          o
     [ 5 V ]       │
        │          ●─── IN   (the pin being watched)
        │          │
        │      [ 10 kΩ ]
        │          │
        └────┬─────┘
            ─┴─
            GND
```

1. Place a 5 V source with ground on its negative terminal.
2. Place a switch from Inputs and Sources, running from the positive terminal to an empty point. Call that point `IN`. This is the pin the microcontroller would be watching.
3. Place a 10 kΩ resistor from `IN` down to ground.



### Read the circuit, twice

**Switch open.** Delete the switch branch from your sketch. What is `IN` still connected to, and what is it no longer connected to? With only one component attached to `IN`, is any current flowing through the resistor? If no current flows through a resistor, what does Ohm's law say the voltage across it must be? And since the resistor's other end is at ground, what does that make `IN`?

That chain of reasoning is worth doing slowly, because "no current means no voltage drop" is a move you will use constantly and it is not in the table.

**Switch closed.** Redraw with the switch as a plain wire. Now `IN` connects to both the supply and ground. Which of the two shapes from the toolkit is this? Where does the current flow, and what does that put `IN` at?

Write down your two predicted readings before running anything.

### Check A

Hover over `IN` and toggle the switch. Falstad usually toggles the most recently placed switch with the space bar, and you can also click it. Record whether the pin reads high or low in each position and compare with your two predictions.

### Build B

The resistor and the switch swap places. Everything else is identical.

```
        ┌──────────┐
        │          │
        │      [ 10 kΩ ]
        │          │
     [ 5 V ]       ●─── IN   (the pin being watched)
        │          │
        │          o
        │           \   switch
        │          o
        │          │
        └────┬─────┘
            ─┴─
            GND
```

1. Start a new circuit with a 5 V source and ground.
2. Place a 10 kΩ resistor from the positive terminal down to a point you again call `IN`.
3. Place a switch from `IN` to ground.

Run the same two-position analysis before measuring anything. Switch open, delete the branch and ask what `IN` is connected to and whether current flows. Switch closed, replace it with a wire and ask what `IN` is tied to.

Predict both readings, then measure them.

Once both builds work, compare them. One reads high at rest and low when pressed, the other does the opposite. Note which is which, because one of the two catches most beginners out, and it decides what your code has to treat as a press.

### Remove the resistor

Take the 10 kΩ resistor out of either build, leaving only the switch and the pin.

Predict what each switch position will do now, using the same two-position method. One of the two should still give a definite answer and the other should not.

Run it. With the switch closed the reading is still correct. With the switch open, `IN` connects to nothing and the voltage is meaningless. Falstad may show it stuck at an odd value or jumping about. In real hardware it drifts and picks up noise, which produces button presses that never happened.

### Change the resistor value

Put the resistor back in build B and try some different values. Work out first which switch position puts the full 5 V across the resistor, then calculate the current wasted in that position for each value.

```
10 kΩ:   5 / 10000  = ?
1 kΩ:    5 / 1000   = ?
100 kΩ:  5 / 100000 = ?
```

A smaller resistor holds the pin more firmly against noise and wastes more current. A larger one wastes less and holds the pin more weakly, which starts to matter with long wires that pick up more interference. Look at your three figures and work out why 10 kΩ is the value you see most often.

### Write

Answer this in your notes: if a button connects a pin to ground when pressed, do you need a pull-up or a pull-down resistor, and what voltage will the pin read when the button is not pressed.

### What you just built

Build A is a **pull-down** resistor and build B is a **pull-up**. A pull-down ties the pin to ground so it rests low, and a pull-up ties it to the supply so it rests high. Either way the resistor gives the pin a defined voltage whenever nothing else is driving it.

Pull-ups are the more common of the two, partly because most microcontrollers have one built into each pin that you can switch on in software, saving a component.

The reason 10 kΩ works is the divider from exercise D. With the switch open the resistor carries no current and so drops no voltage, putting the pin at whatever the resistor is tied to. With the switch closed the switch is a near-zero resistance in the divider, and a near-zero resistance next to a 10 kΩ one takes essentially the whole supply share. The resistor is easily overridden, which is exactly what you want.

Two techniques to keep.

**Analyse switched circuits once per position.** Replace a closed switch with a wire and delete an open switch's branch entirely. Two simple circuits beat one circuit with a moving part in it.

**No current means no voltage drop.** Ohm's law run backwards, with I at zero, is how you reason about any component that is connected but idle. It is what tells you a pull-up resistor with nothing pulling against it puts the pin at the full supply voltage rather than somewhere in between.

---



## I. Capacitors and the time constant

**Teaches:** What a capacitor does, and how to work out how quickly it charges.

**Why you need it:** Capacitors are the second most common component after resistors, and unlike resistors their behaviour involves time. They smooth power supplies, filter noise out of sensor readings, and set the timing in oscillator circuits. The next two exercises both depend on understanding what you see here.

### The idea

A **capacitor** stores electrical charge. The usual analogy is a small water tank plumbed into a pipe. Water flows in and fills it, the level rises, and once it is full the flow stops. Connect it to a lower pressure and it empties back out again.

Capacitance is measured in **farads** (F), though a farad is enormous. Practical parts are measured in microfarads (µF), which are millionths of a farad, and nanofarads (nF) and picofarads (pF), which are smaller still.

The behaviour worth remembering is that **a capacitor resists sudden changes in voltage**. It cannot jump from 0 V to 5 V instantly, because charge has to physically flow in to make that happen, and that takes time. How much time depends on the capacitor's size and on how much resistance the charging current has to pass through.

This gives us the **time constant**, written with the Greek letter tau.

```
tau = R x C
```

With R in ohms and C in farads, tau comes out in seconds. It tells you how fast the curve rises. After one time constant the capacitor has reached about 63 percent of the way to its final voltage. After about five time constants it is close enough to fully charged that the remainder does not matter.

The shape of the charging curve is worth noticing. It rises steeply at first and then flattens as it approaches the supply voltage, rather than climbing in a straight line. The capacitor charges fastest when it is empty, because the voltage difference driving the current is largest then.

### Build

A 5 V source, a switch, a 1 kΩ resistor and a 1 µF capacitor to ground.

```
        ┌───o/ o───[ 1 kΩ ]───┐
        │   switch            │
        │                     ●─── scope this node
     [ 5 V ]                  │
        │                   ─────
        │                   ─────  1 µF
        │                     │
        └──────────┬──────────┘
                  ─┴─
                  GND
```

The two short parallel lines are the capacitor. The node between the resistor and the capacitor is the one to watch, because that is the voltage that takes time to change.

1. Place the 5 V source with ground on its negative terminal.
2. From the positive terminal, place a switch, then the 1 kΩ resistor in series after it.
3. Place the capacitor from the free end of the resistor down to ground. The point where the resistor meets the capacitor is the one to watch.
4. Right-click the capacitor and choose **View in Scope**. A graph appears at the bottom showing its voltage against time.

Start with the switch open so the capacitor begins empty.

### Predict

Note that 1 µF is 0.000001 F, so the units come out in seconds.

```
tau = 1000 Ω x 0.000001 F = ?
```

Convert your answer to milliseconds. Then work out what voltage the capacitor should have reached one time constant after the switch closes, using the 63 percent figure and the 5 V supply. Also work out roughly how long it takes to get close to fully charged.

### Check

Close the switch and watch the scope trace rather than only the final number. You are looking for the curved rise, steep at the start and levelling off at the top. Compare the time it takes to level off against your prediction.

If the trace jumps straight up as a vertical line, your time base may be too slow to show the detail. Falstad's simulation speed slider changes how fast events play out on screen.

### Open the switch

Open the switch again. If nothing else provides a path to ground, the capacitor holds its charge and the voltage stays roughly where it was. A capacitor stores energy and releases it when something gives it a route to discharge.

This also shows something important about how capacitors handle steady voltages. Once charged, no more current flows into it. A capacitor passes current only while the voltage across it is changing.

### Change

Set the capacitor to 10 µF and repeat.

```
tau = 1000 x 0.00001 = ?
```

Predict how the curve will differ from the first one before you look, then check whether the trace matches.

Now put the capacitor back to 1 µF and change the resistor to 10 kΩ instead. Work out tau again. Compare it with the 10 µF case above and explain why the two come out as they do, given that tau depends on the product of the two values.

This size and speed relationship explains a distinction you will meet in the next exercise. Small capacitors respond quickly but hold little energy, while large ones hold plenty but react slowly. Real boards use both.

### Write

One sentence on what the time constant tells you, and one sentence on why the charging curve flattens out instead of rising in a straight line.

---



## J. Decoupling capacitors and sudden loads

**Teaches:** Why every integrated circuit needs a capacitor next to its power pins.

**Why you need it:** Look at any commercial circuit board and you will see small capacitors scattered next to every chip. They are there for the reason this exercise demonstrates. Leave them off your own board and you get a design that mostly works, then fails intermittently in ways that are very hard to trace. Knowing what they do also tells you where to put them, which matters as much as having them.

### The idea

Exercises so far have treated the power supply as perfect, able to deliver any current at exactly 5 V. Real supplies are not like that.

Every real supply has some resistance of its own, from the battery's internal chemistry, from the regulator, and from the wires carrying the power. This is called **source resistance** or internal resistance, and you can model it as a small resistor in series with an otherwise perfect supply.

That resistance matters as soon as current flows, because the current passing through it creates a voltage drop, exactly as Ohm's law says it must. The more current the circuit draws, the more voltage is lost before it reaches the chip. So the voltage at the chip sags when the load increases.

Digital chips make this worse by drawing current in sudden bursts rather than smoothly. Every time thousands of transistors switch together, the chip demands a spike of current for a fraction of a microsecond. The supply cannot respond that quickly, so the local voltage dips. Dip far enough and the chip resets or misbehaves.

A **decoupling capacitor** solves this by sitting right beside the chip's power pins as a small local reservoir of charge. When the chip suddenly needs current, it takes it from the nearby capacitor instead of pulling it all the way down the wire from the supply. The capacitor then refills between bursts.

The water analogy holds up here. A tap at the end of a long narrow pipe gives poor pressure when opened suddenly. Put a small tank right next to the tap and the first rush comes from the tank while the pipe catches up.

Position matters. The capacitor has to be physically close to the chip, because any wire between them adds resistance and defeats the purpose.

### Build

You are going to build a deliberately weak supply and then hit it with a sudden load.

```
        ┌──[ 100 Ω ]──●──────────────┐   ● = Vcc, scope this node
        │             │              │
        │           ─────         [ 50 Ω ]
     [ 5 V ]        ─────            │
        │           100 µF           o
        │           (added            \   switch
        │            later)          o
        │             │              │
        └─────────────┴──────────────┘
                      │
                     ─┴─
                     GND
```

The 100 Ω in the top wire is standing in for the supply's own internal resistance, so `Vcc` is the voltage a chip would actually receive rather than the voltage the source produces. Build it without the capacitor first, then add the capacitor and repeat.

1. Place a 5 V source with ground on its negative terminal.
2. Put a **100 Ω** resistor in series with the positive terminal. This stands in for the supply's internal resistance plus thin wiring. Real supplies are much better than this, and the exaggeration makes the effect easy to see.
3. Call the far side of that resistor `Vcc`. This is the point where a chip would be connected.
4. From `Vcc`, place a switch in series with a **50 Ω** load resistor going to ground. Closing the switch represents the chip suddenly demanding a lot of current.
5. Right-click the `Vcc` node and choose View in Scope.



### Predict

Start with the switch open. No current flows, so work out what is dropped across the 100 Ω and what `Vcc` therefore sits at.

With the switch closed, the 100 Ω and the 50 Ω form a voltage divider, which is the same arrangement as exercise D.

```
Vcc = 5 x 50 / (100 + 50) = ?
```

Compare your answer with the 5 V the chip is supposed to receive, and decide whether a chip on that rail would still be working.

### Check without a capacitor

Close the switch and watch the scope. Compare where `Vcc` settles against your prediction, and note how long it stays down.

### Check with a capacitor

Add a **100 µF** capacitor from `Vcc` to ground, connected at the `Vcc` terminal itself. Let it charge with the switch open, then close the switch and watch again.

Predict first, in words rather than numbers. The capacitor is sitting fully charged at 5 V when the load arrives. Say what you expect that to do to the size of the dip, and to how quickly the dip develops.

Then consider where the voltage ends up once the capacitor has been drained, and whether the capacitor changes that final figure at all. This distinction between the initial dip and the settled value is the whole point of the exercise.

### Change

Try a 1000 µF capacitor, and predict from exercise I how the dip will differ given ten times the stored charge.

Then try a small 0.1 µF capacitor, which is the value most commonly printed next to chips on real boards. Watch how much difference it makes here, and work out why, given how long this load stays connected compared with the timescale that capacitor can cover.

Real chips draw their bursts in a tiny fraction of a microsecond, which is the timescale a small capacitor handles well. Once you have tried all three values, explain why a real board carries both large capacitors near the power input and small ones beside each chip.

### Write

Explain in your own words why a chip needs its own capacitor rather than relying on the main supply, and why that capacitor has to be physically close to the chip.

Bear in mind this circuit is a simplification. A real regulator actively corrects its output and behaves better than a plain resistor. The simplification is enough to make the underlying idea concrete.

---



## K. Why a stalled motor resets a microcontroller (Module 1 Optional milestone)

**Teaches:** How a heavy load drags down a shared power rail, and why that resets everything else on it. This is practice task 6 and the subject of the Module 1 verbal milestone.

**Why you need it:** This is the classic first-robot failure. You build something, it drives fine, then the moment a wheel jams against a wall the microcontroller reboots and the robot goes dead. It looks like a software crash or a loose connection, and it is neither. You will meet this the first time you build anything that moves, and being able to recognise it immediately saves days.

### The idea

A **stall** is when a motor is powered but cannot turn, because a wheel is blocked or the robot has driven into something. A spinning motor generates a voltage of its own that opposes the supply and limits the current it draws. A stalled motor generates none of that, so its current is limited only by the resistance of its windings, which is very low. A stalled motor can easily draw five to ten times its normal running current.

Now combine that with what you learned in exercise J. The supply has its own internal resistance, and current flowing through it causes a voltage drop. A large current causes a large drop.

So when the motor stalls, the voltage on the shared power rail collapses. Everything connected to that rail sees the reduced voltage, including the microcontroller. Microcontrollers monitor their own supply and deliberately reset if it falls below a safe threshold, because operating on insufficient voltage produces corrupt behaviour. That protective reset is what you observe as the robot dying.

The term for this is a **brownout**. The supply did not fail completely, and it sagged far enough to matter.

Everything in this exercise is a combination of ideas you already have. The internal resistance and the loads form a voltage divider, the microcontroller and the motor sit in parallel across the rail, and Kirchhoff's current law gives you the total current.

### Build

```
        ┌──[ 10 Ω ]──●──────────────┐   ● = Vcc, scope this node
        │            │              │
        │        [ 500 Ω ]        [ 5 Ω ]
        │          "MCU"         "motor"
     [ 5 V ]         │              │
        │            │              o
        │            │               \   switch closed = stalled
        │            │              o
        │            │              │
        └────────────┴──────────────┘
                     │
                    ─┴─
                    GND
```

The 10 Ω is the battery's internal resistance, the same trick as exercise J. The two loads hang side by side off `Vcc`, which makes them parallel in the sense of exercise C. Closing the switch is what a stall does.

1. Place a 5 V source with ground on its negative terminal.
2. Put a **10 Ω** resistor in series with the positive terminal, representing the battery's internal resistance and the wiring.
3. Call the far side of that resistor `Vcc`. Both loads connect here.
4. From `Vcc` to ground, place a **500 Ω** resistor. This is the microcontroller, which draws a modest steady current.
5. Also from `Vcc` to ground, place a switch in series with a **5 Ω** resistor. This is the motor in its stalled state. The switch lets you apply the stall on demand.
6. Right-click `Vcc` and choose View in Scope.

Both loads must connect to the same `Vcc` terminal and the same ground, which is the parallel arrangement from exercise C.

### Predict

**Switch open**, with only the microcontroller drawing current:

```
total resistance = 10 + 500 = ?
I = 5 / (total resistance) = ?
Vcc = 5 x 500 / (total resistance) = ?
```

Judge your answer against the 5 V the supply provides, and decide whether the 10 Ω is doing much at this current.

**Switch closed**, with the stalled motor in parallel with the microcontroller:

```
load resistance = (500 x 5) / (500 + 5) = ?
Vcc = 5 x (load resistance) / (10 + load resistance) = ?
```

Look closely at your combined load resistance and compare it with the 5 Ω motor on its own. Note how much difference the 500 Ω microcontroller makes to that figure, and what that tells you about which of the two loads is drawing the current.

Take a microcontroller minimum supply of about 3 V, and decide from your second figure whether it would still be running.

### Check

Read `Vcc` with the switch open and then closed, and compare both against your predictions. Picture a line on the scope at 3 V and note which side of it the stalled value falls.

Hover the 5 Ω resistor to read the stall current, and compare it with the current the microcontroller draws. Write down the ratio between the two, because that difference in scale is what causes the problem.

### Try a capacitor

Add a 470 µF capacitor from `Vcc` to ground and stall again.

Predict first, drawing on exercise J. Say what you expect to change about the shape of the dip, and whether you expect the settled voltage to end up anywhere different.

Then explain why a capacitor helps less here than it did in exercise J, given that the motor keeps drawing current for as long as it stays stalled. Note down what would actually fix this, thinking about the 10 Ω internal resistance and about whether the motor needs to share a rail with the electronics at all.

### Write

This is the Module 1 verbal milestone, so prepare it properly. Draw a circuit diagram with four labelled boxes: the battery, its internal resistance, the microcontroller, and the motor. Then explain out loud, without notes, why stalling the motor resets the microcontroller.

Your explanation needs to answer four questions in order. What changes about the motor's current draw when it stalls. Where does that current have to pass through on its way from the battery. What does that do to the voltage on the shared rail. And why does the microcontroller stop running as a result.

---



## L. Reading PWM on an oscilloscope (Module 1.2)

**Teaches:** How to read a signal that changes over time, and what pulse width modulation means. Covers oscilloscope basics: voltage against time, frequency and duty cycle.

**Why you need it:** PWM is how you control motor speed, LED brightness and servo position. Nearly every output on a robot that is not simply on or off uses it. Reading it on a scope trace is also your introduction to the instrument you will need whenever a signal misbehaves in a way a multimeter cannot show.

### The idea

Everything measured so far has been a steady voltage. A multimeter is fine for that. Many useful signals change constantly instead, and to see those you need an **oscilloscope**, which draws a graph of voltage against time. Time runs left to right and voltage runs bottom to top.

**Pulse width modulation**, or PWM, is a way of getting an in-between result from an output that can only be fully on or fully off. Instead of producing half voltage, the output switches between on and off very rapidly, and spends half its time in each state. Averaged out, the effect is the same as half power. Do it fast enough and an LED looks steadily dimmer rather than flickering, and a motor turns more slowly rather than juddering.

Three terms describe the signal.

- The **period** is the time for one complete on and off cycle, measured in seconds or milliseconds.
- The **frequency** is how many cycles happen per second, measured in hertz (Hz). Frequency and period are opposites of each other, so a 1 ms period means 1000 cycles per second, which is 1000 Hz.
- The **duty cycle** is the fraction of each period spent switched on, given as a percentage.

```
duty cycle = (time on / period) x 100
```

A 25 percent duty cycle means the output is on for a quarter of each cycle, and the average voltage works out at a quarter of the supply.

Duty cycle and frequency are independent. Duty cycle sets how much power is delivered, and frequency sets how rapidly the switching happens. You normally pick a frequency high enough to avoid visible flicker or audible whine, then vary duty cycle to control the output.

### Build

```
        ┌──────────────┐
        │              │
        │          [ 330 Ω ]
        │              │
   [ PWM out ]         ▼   LED
        │             ───
        │              │
        └──────┬───────┘
               │
              ─┴─
              GND
```

Scope the node at the PWM output, where the signal leaves the source. The circuit is exercise F with the steady 5 V source swapped for one that switches on and off. The interest here is in the trace on the scope rather than in the loop itself, so the LED is optional.

1. Start a new circuit and place a **PWM Output** from Inputs and Sources. Alternatively use a voltage source and right-click it to set a square wave, then set its frequency and duty cycle.
2. Optionally drive an LED through a 330 Ω resistor to ground, so you can see the brightness change.
3. Right-click the PWM node and choose View in Scope.
4. Slow the simulation speed down until you can see individual pulses instead of a blur.



### Read and change the signal

**First, read the signal.** Look at the trace and identify one complete cycle, from the start of one pulse to the start of the next. Measure the period, then measure how long the signal was high within it. Work out the duty cycle from those two figures.

Here is what you are looking at, with the two measurements marked.

```
   5 V   ┌─────┐     ┌─────┐     ┌─────┐
         │     │     │     │     │     │
   0 V ──┘     └─────┘     └─────┘     └──

         |<--->|                time on
         |<--------->|          one full period

         time runs left to right
```

The period is measured from the start of one pulse to the start of the next, so it covers the on part and the off part together.

Do this by eye from the trace first, then open the component's Edit dialog and compare. Reading a waveform is a skill worth practising while there is something to verify against.

**Second, change the duty cycle.** Set it to 25 percent, then 50, then 75. Work out the average voltage each time, taking the supply as 5 V.

```
25% of 5 V = ?
50% of 5 V = ?
75% of 5 V = ?
```

Also predict what happens to the width of the pulses and to the spacing between them. If you added the LED, note whether its brightness follows your figures.

**Third, change the frequency.** Leave the duty cycle at 50 percent and raise the frequency. Before you look, predict what happens to the width of the pulses, to the duty cycle, and to the average voltage. Then check which of those three actually changed.

### Write

Note down the difference between duty cycle and frequency, and give the formula for duty cycle.

One caution for later. Duty cycle is not the same as motor speed. Setting 50 percent duty does not give you half the maximum RPM, because a motor's speed also depends on the load it is pushing against and on the supply voltage. Module 2 covers that. All you are proving here is that you can look at a trace and state its duty cycle.

---



## M. Reading schematics and finding faults

**Teaches:** Reading and drawing circuit diagrams, and diagnosing a fault from measurements rather than by looking for the broken bit. Covers the assessment criterion about identifying every component and its orientation.

**Why you need it:** A schematic is how circuits are communicated. Every datasheet, tutorial and module you buy comes with one, and being unable to read it means copying pictures and hoping. Fault finding matters just as much. Most of your build time will be spent working out why something does not work, and the difference between a productive hour and a wasted one is whether you measure or guess.

No new components are needed here. This exercise practises the two skills that make everything before it useful.

### Part 1: draw the circuit

Pick one of your finished circuits from exercise G, H or K. Redraw it on paper, away from the screen.

There is no diagram for this exercise on purpose. Producing the diagram is the task. When you are finished you can compare yours against the one in whichever exercise you chose, though give yourself an honest attempt first.

Your drawing must include:

- The supply, shown as a battery or a Vcc symbol with its voltage written next to it
- The ground symbol, and every connection that reaches it
- Every resistor with its value written beside it
- Any diode or LED, drawn so the direction is unambiguous
- Any transistor, with the collector, base and emitter clearly labelled
- Every wire that joins two components

That last point is where drawings usually fail. It is easy to draw all the parts correctly and leave out a connection, and ground connections are the ones most often forgotten, because they feel like background rather than part of the circuit.

### Part 2: rebuild from your drawing

Close Falstad, or start a fresh blank circuit, and rebuild using only your paper drawing as the reference. No peeking at the original.

If the rebuild does not work, do not fix it from memory. Work out what your drawing failed to record, and correct the drawing first. That gap is what you would have got wrong reading somebody else's schematic too.

### Part 3: find the fault

This is the important half of the exercise.

Take a working copy of circuit D or G. Introduce a single fault, then diagnose it using voltage and current readings only, as though the wire were hidden inside a device you cannot open.

Faults worth trying:

- Delete a resistor, leaving a gap where current cannot flow
- Turn the LED around
- Disconnect the ground connection
- Change a resistor to a badly wrong value, such as 10 kΩ where 220 Ω belongs

For each one, work through it methodically. Start at the supply and confirm it is present. Then follow the circuit along, reading the voltage at each point, until you find where the readings stop matching what you expect. The fault is between the last correct reading and the first wrong one.

A few patterns are worth memorising, because they come up again and again in real hardware:

- A voltage of zero where you expected something usually means a break earlier in the path, or a short to ground
- Full supply voltage across a component that should be dropping only part of it usually means the path after it is broken
- Everything reading correctly with nothing working usually means a missing ground or a missing return path



### Why you diagnose rather than inspect

The temptation with a broken circuit is to stare at it looking for the mistake. That works occasionally and fails badly on anything complicated, because you tend to re-read what you meant to build rather than what you actually built.

Measuring avoids that entirely. Each reading eliminates part of the circuit, and a few readings narrow the problem down to a small area regardless of how large the board is. This is exactly what you will do later with a real multimeter, and practising it in the simulator is free.

### Write

Record the fault you introduced, the readings you took, and how those readings led you to it. Do this for at least two different faults.

---



## You are finished when

Without looking anything up, you can do all of the following.

1. Predict the output of a voltage divider and confirm it in the simulator. Exercise D.
2. Explain why attaching a load changes that output voltage. Exercise E.
3. Switch an LED using an NPN transistor driven from a 3.3 V source. Exercise G.
4. Say what happens to a floating input and how a pull-up resistor fixes it. Exercise H.
5. Sketch and explain why a stalled motor resets a microcontroller. Exercise K.

There is a sixth test, and it is the one worth caring about. Take any circuit in this file, cover the text, and work out from the diagram alone how many nodes it has, which parts are in series, which are in parallel, and which calculation you would reach for. If you can do that without reading the surrounding explanation, the arithmetic will look after itself.

Once those hold, move on to the physical tasks in `01-electronics-and-tools.md`. Those are building a voltage divider on a real breadboard, reading resistor colour bands and checking them with a meter, and using continuity mode to find a break in a wire you have damaged yourself.

Falstad has done its job for Module 1 at that point. [Tinkercad Circuits](https://www.tinkercad.com/circuits) is an optional extra if you want to practise on a virtual breadboard while you wait for parts to arrive, since it looks more like real hardware than a schematic does.

---

