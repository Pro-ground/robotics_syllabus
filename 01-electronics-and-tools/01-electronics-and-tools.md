# Module 1: Electronics, Tools, and Foundations

**Estimated time:** 8 weeks · **80–100 hours** (Standard)  
**Prerequisites:** None. This module starts from zero electronics knowledge.

Hours include buying parts, waiting for shipping (plan around it), failed joints, and writing READMEs. They are not watch time.

## Goals

By the end of this module you should be able to:

- Read a schematic and build the circuit it describes on a breadboard
- Calculate resistor values and verify them with a multimeter
- Find a short, a break, or a dead component with diagnostic tools
- Solder a clean through-hole joint and verify it electrically
- Rearrange a formula, convert units, and work out an angle step from a rate and a time
- Write a Python script, run it from the terminal, and push it to GitHub
- Explain why a motor stalling can reset a microcontroller



## 1.1 Electronics Fundamentals



### What to learn

- Ohm's law, voltage dividers, Kirchhoff's laws
- What a capacitor does, how a transistor switches, what a diode does
- Reading schematics: symbols for resistor, capacitor, diode, transistor, ground, Vcc
- Pull-up and pull-down resistors — used everywhere, not optional
- Decoupling capacitors — why every IC needs one near its power pins
- Battery chemistry basics: LiPo cell counts, C ratings, charging safety (never leave a LiPo charging unattended)
- Current draw: why a motor stalling browns out your regulator
- ESD and bench safety: wrist strap or touch ground before handling ICs, eye protection when clipping and soldering, ventilate flux fumes

If turning `V = I x R` around, or converting milliamps and kilohms, feels rusty, do practice files `001`–`003` in [`1.5_maths_practice/`](1.5_maths_practice/) before you spend long on the Falstad sheet.



### Resources


| Resource                                                                                                              | Format            | Why                                                                                                                                                                                                                                                                                                                                                                                     | Path                   |
| --------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [Falstad Circuit Simulator](https://www.falstad.com/circuit/)                                                         | Free browser app  | Animated electron flow — watch current move                                                                                                                                                                                                                                                                                                                                             | Mandatory              |
| [Module 1 Falstad exercises](01-falstad-exercises.md)                                                                 | Lab sheet         | Ordered read-then-predict-then-build circuits for every 1.1 idea Falstad can show                                                                                                                                                                                                                                                                                                       | Mandatory              |
| [Tinkercad Circuits](https://www.tinkercad.com/circuits)                                                              | Free with account | Virtual breadboard + virtual Arduino + virtual multimeter                                                                                                                                                                                                                                                                                                                               | Mandatory              |
| [Afrotechmods Tutorials](https://www.afrotechmods.com/tutorials/)                                                     | Free videos       | Short, fast, beginner-friendly                                                                                                                                                                                                                                                                                                                                                          | Mandatory              |
| [Make: Electronics, 3rd ed, Charles Platt](https://www.makershed.com/products/make-electronics-3rd-edition-print)     | Book, ~$30        | Deliberately destroys components to teach their limits                                                                                                                                                                                                                                                                                                                                  | Optional               |
| [All About Circuits, Lessons in Electric Circuits](https://www.allaboutcircuits.com/textbook/)                        | Free textbook     | Reference when a video hand-waves. Do **not** read Volumes 1–3 cover to cover                                                                                                                                                                                                                                                                                                           | Optional (lookup only) |
| [Ultimate Electronics](https://ultimateelectronicsbook.com/)                                                          | Free online book  | The best fit if you can do the arithmetic but cannot tell which calculation a circuit needs. Sections 2.12 to 2.15 cover series and parallel, Kirchhoff's laws, labelling nodes, and solving a circuit as a system, which is exactly the reasoning the lab sheet asks you to do. Every schematic opens in a simulator you can edit and re-run, and chapter 2 has 121 worked DC examples | Optional               |
| [Khan Academy circuit analysis](https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic) | Free videos       | Willy McAllister narrates why he reaches for a particular method before he starts the algebra. Useful if you prefer watching someone reason out loud to reading it                                                                                                                                                                                                                      | Optional               |
| Learning the Art of Electronics, Hayes and Horowitz                                                                   | Book, ~$70        | A lab course built around reasoning about circuits and estimating answers rather than deriving them. The approachable companion to The Art of Electronics, which is the standard reference but heavy going as a first book                                                                                                                                                              | Optional               |




### Estimated hours

- Falstad + Tinkercad + short videos: 12–16 hours
- Physical breadboard practice: 6–8 hours
- Platt experiments (if you bought the book): 8–12 hours Optional
- All About Circuits as a course: skip. Use it when stuck.
- Ultimate Electronics chapter 2, read alongside the Falstad exercises: 4–6 hours Optional



### Assessment criteria

- Can you look at a schematic and identify every component and its orientation?
- Can you calculate the current through a series circuit with an LED and resistor?
- Can you measure voltage, resistance, and continuity correctly?
- If a circuit doesn't work, can you diagnose whether it's a wiring issue, a dead component, or a wrong value?



## 1.2 Breadboarding Basics



### What to learn

Before you touch an iron, you need to know how a breadboard works. Jumper wires and a breadboard are your first prototyping platform, and getting good at them saves hours of frustration in every module that follows.

- **How a breadboard connects internally** — which rows and columns are electrically the same node, which are not
- **Terminal strips** — the two groups of five-hole columns in the middle, and why each row (a–h) is a node but columns are separate
- **Power rails** — the long rows on the edges (usually red and blue) that run the full height of the board, and why you need to jumper them at the ends if the board doesn't already
- **Component insertion** — how firmly to press, how to orient ICs relative to the notch, and how to tell you got it wrong
- **Wire routing habits** — short runs, colour-coding VCC and GND, avoiding crossover spaghetti
- **Checking your work** — the first thing you do after building and before powering anything



### How a breadboard works

A breadboard is a grid of small metal clips hidden underneath. Each clip grabs the legs of parts and holds them together, but the grid is not fully connected — it is deliberately partitioned so you can make connections without solder.

**The terminal strip** — the main area in the centre — has five vertical columns (numbered 1 to 30 or more, depending on board size). Each horizontal row across those five columns (labelled a to e on the left side, f to j on the right) is one electrical node. That means holes a1, b1, c1, d1, and e1 all connect to each other. Holes f1 through j1 connect to each other. But a1 and f1 do **not** connect — there is a physical gap running horizontally between the left and right halves. That gap is where you put a DIP IC so its pins on either side land in separate groups.

```
  ┌───── terminal strip (one node per row) ─────┐
  | a  b  c  d  e | f  g  h  i  j
  | 1  1  1  1  1 | 1  1  1  1  1    ← row 1 is one node on each side
  | 2  2  2  2  2 | 2  2  2  2  2    ← gap between columns e and f
  | 3  3  3  3  3 | 3  3  3  3  3    ← row 3 is a separate node
  └───────────────────────────────────┘
```

**The power rails** — the long rows along the top and bottom edges (usually red for VCC and blue for GND) run the full height of the board. Each side of each rail is usually one continuous node, meaning every red hole is connected to every other red hole on that side. The two sides of the same rail (left and right) may or may not connect at the ends, depending on the board. Many beginner boards do not connect the left side to the right side, so you need to add a short jumper wire between them yourself.

```
  ┌─────── rails (VCC / GND) ─────────┐
  |  +  +  +  +  +  +  +  +  +  +  + |  ← VCC rail
  |                                   |
  |  a  b  c  d  e | f  g  h  i  j   |
  |  1  1  1  1  1 | 1  1  1  1  1   |  ← terminal strip
  |  ...            | ...             |
  |                                   |
  |  -  -  -  -  -  -  -  -  -  -  - |  ← GND rail
  └───────────────────────────────────┘
```



### Inserting components

- Push each leg in straight and firm. It should take a deliberate push with your thumb — not a tentative tap, not a hammer blow. A loose connection causes intermittent faults that are almost impossible to debug.
- For ICs, orient the notch (or the dot next to pin 1) toward the top of the board. Pin 1 is always top-left when the notch faces up. Double-check the first pin before you push the whole thing in.
- Resistors and capacitors have no polarity. LEDs do — the longer leg (or the flat edge on the plastic body) is the cathode. The symbol crib in the Falstad exercises covers this.
- Do not bend component legs before inserting them unless they are very long. A leg that bends in the clip is a leg that can come loose.



### Wire routing habits

Good wire routing is what separates a board you can understand from a board you need to photograph and cry over.

- **Keep wires short.** A three-centimetre wire is fine. A fifteen-centimetre wire is a snarled knot waiting to happen.
- **Colour-code power.** Red for VCC, black for GND. Every other colour for signal wires. Once you build this habit it takes seconds to trace a circuit by eye.
- **Run power rails last.** Build the signal path first, then add the VCC and GND connections. If a signal wire is blocking a power wire, you have wired in the wrong order.
- **Avoid crossing wires on the same plane.** If two wires must cross, put one on the terminal strip and the other near the edge of the board, or use a different layer of the board's height.



### Checking before you power on

Never plug a breadboard circuit into a power supply or battery without checking it first. The sequence is:

1. **Visual trace.** Start at the positive terminal of your power source and follow the circuit through to ground, confirming each connection matches the schematic or your mental diagram. This is the same skill the Falstad exercises ask you to develop, only with real parts.
2. **Continuity check.** Use a multimeter in continuity mode to confirm every expected connection exists and no unexpected shorts are present. A common test: touch one probe to VCC and the other to GND. A buzzer means a dead short — fix it before powering.
3. **Component verification.** For each resistor, read its value with the multimeter's ohmmeter and compare against the expected value. Check that LEDs are pointing the right way.



### Practice tasks

1. **Mandatory.** Read the resistance of five resistors using your multimeter, then confirm each value against the colour bands. Note any discrepancies and think about why the actual value might differ from the band colour.
2. **Mandatory.** Build the voltage divider from exercise D (two 10 kΩ resistors, 5 V source, ground on the bottom) on a real breadboard. Measure the mid-node voltage against ground. Confirm it is within 5 percent of the expected 2.5 V.
3. **Mandatory.** Intentionally break one of the connections in your breadboard divider — pull a wire out, or reseat a component so it sits in the wrong row. Use continuity mode to find the broken connection. Do not look at the board; use only the multimeter.
4. **Optional.** Build the transistor switch circuit from exercise G on a breadboard. Verify the LED lights when you apply 3.3 V to the base, and confirm that removing the base voltage turns it off.



### Estimated hours

- Learning how the breadboard connects internally and practising component insertion: 2–3 hours
- Building and checking circuits from the Falstad exercises: 4–6 hours



## 1.3 Debugging Tools and the Workbench



### What to learn

This section fills a gap in most syllabi: diagnostic instrumentation beyond a multimeter.

- **Oscilloscope basics** — voltage vs. time, triggering, measuring frequency and duty cycle of PWM signals
- **Logic analyzer** — viewing digital bus signals (UART, I2C, SPI), decoding protocols
- **Bench power supply** — current limiting, compliance voltage, why it matters for debugging
- **Current sensing** — measuring supply current to diagnose short circuits and motor stalls
- **Signal integrity** — noise on power rails, decoupling, ground loops

If you are on Tier 0–2, learn the concepts from video and measure what you can with a multimeter. Hands-on PWM and I2C traces wait until you have Tier 3 or borrow a scope. Do not assess yourself on traces you have never seen.

### Resources


| Resource                                                                                          | Format      | Why                                                                 |
| ------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------- |
| [EEVblog oscilloscope tutorial series](https://www.youtube.com/watch?v=Oe9kF8s3f0Q)               | Free videos | Best practical intro to oscilloscope use                            |
| [Saleae logic analyzer tutorials](https://learn.saleae.com/)                                      | Free docs   | Protocol decoding for UART, I2C, SPI                                |
| [How to Use a Multimeter, SparkFun](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter) | Free guide  | Voltage, current, continuity, and what to do when you blow the fuse |




### Estimated hours

- Oscilloscope and analyzer videos: 3–4 hours
- Hardware practice: 4–8 hours (more if Tier 3 just arrived)



### Hardware


| Tier | Cost      | What you get                                                                                                                                                                                                                                                             |
| ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0    | $0        | Simulators only (Falstad, Tinkercad)                                                                                                                                                                                                                                     |
| 1    | ~$50–60   | Elegoo UNO starter kit + multimeter (Adafruit 9205B+, ~$18)                                                                                                                                                                                                              |
| 2    | ~$160     | Tier 1 + soldering station (Pinecil V2, ~$26), solder, flux, side cutters, wire strippers, helping hands, perfboard, safety glasses                                                                                                                                      |
| 3    | ~$350–550 | Tier 2 + bench power supply with current limit (~$40–80), **USB oscilloscope** (e.g. a 2-channel 20 MHz-class USB scope, ~$50–150) **or** a Pico-based scope kit, **logic analyzer** (24 MHz 8-channel USB clone or Saleae, ~$15–150), desoldering pump, storage drawers |


Tier 3 exists so Module 2 PWM and I2C are something you can **see**, not only describe. If you plan to take the Embedded track, buy Tier 3 before Module 2, not after.

### Where to order

- **AliExpress** — cheapest (3–10× less), 2–6 weeks shipping, no support for dead parts
- **Amazon** — mid-priced, fast, right place for your first kit
- **Elegoo direct** — regional warehouses, ~1 week
- **Adafruit / SparkFun** — more expensive, full tutorials with every product, real support
- **DigiKey / Mouser** — exact parts by specification with genuine datasheets
- **Pololu** — motors and drivers, ships internationally

For your first order, pay the premium and buy from Amazon or Elegoo direct so you are building within days. Once you know what components look like, order from AliExpress.

### Practice tasks

- **Mandatory.** Measure the voltage of a battery, the resistance of five random resistors (check against colour bands), then use continuity mode to find a deliberately broken wire.
- **Mandatory if Tier 3 / Optional otherwise.** Use the bench supply's current limit to find a short. Watch the current spike, set the limit, watch the voltage drop.
- **Mandatory if Tier 3 / Optional otherwise.** Put a PWM pin on the scope. Measure frequency and duty cycle. Change `analogWrite` and watch the duty cycle move.
- **Optional.** Decode an I2C transaction with the logic analyzer while reading a sensor.



## 1.4 Soldering



### What to learn

- Tinning the tip and keeping it clean
- Heating the joint, not the solder
- Recognizing a cold joint by sight and touch
- Through-hole first, surface-mount much later
- Using flux — fixes most problems beginners blame on the iron
- Desoldering: pump, wick, and when to give up



### Resources


| Resource                                                                                               | Format     | Why                                                          |
| ------------------------------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| [Adafruit Guide to Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering) | Free guide | Iron selection, joint technique, failure photographs, safety |




### Estimated hours

- Reading + practice: 4–8 hours



### Practice tasks

1. **Mandatory** (needs Tier 2). Solder header pins onto a cheap breakout board. Test every pin with continuity mode.
2. **Mandatory.** Do the whole thing three times.
3. **Mandatory.** Desolder one and resolder it — removing components badly is how most beginners destroy boards.
4. **Fast-path skip / Optional on Tier 1.** If you have no iron yet, stay on jumper wire for Module 2 and solder before the arm in Module 3.



### Assessment criteria

- Can you identify a cold joint vs. a good joint from a photograph?
- Can you solder a through-hole joint in under 5 seconds?
- Can you desolder a component without lifting the pad?



## 1.5 The calculations this module uses

This section is for people who last saw this material years ago. It is not a maths course. It is the small set of calculations you already used on circuits, plus the ones the Python files and Module 2 will ask for.

Do the practice files in [`1.5_maths_practice/`](1.5_maths_practice/) in numbered order, on paper or in a notes app. Each file teaches one idea, then asks you to use it. Answers sit at the bottom of the same file. Write yours first.

Do `001`–`003` as soon as the Falstad arithmetic feels shaky, even if you are still in section 1.1. Finish `004`–`006` **before** you start the Python files that use them (`004_timed_loop.py`, `005_angles.py`, and the later files that average readings). Do not move to Module 2 until every file in the folder is one you can do without looking up the method.

Module 4 is where you meet the extra maths for later labs. You do not need it to finish this module.

### What to learn

- Turning one formula around so you can find any one of voltage, current, or resistance when you know the other two
- Writing a current in amps or milliamps, and a resistance in ohms or kilohms, without mixing the two
- Sharing a voltage in proportion to two resistances (the voltage divider you already built)
- A change equals a rate times a time step. Later code writes this as `angle = angle + gyro * dt`
- Degrees and radians as two units for the same turn; shifting an angle by whole turns so it stays in a useful range; straight-line distance; the direction of a point from the origin, as an angle
- The mean of a list of readings, and blending two guesses with a weight

### Practice tasks

**Mandatory.** Complete every file in `1.5_maths_practice/` and check your answers.

1. `001_rearrange.md` — find voltage, current, or resistance from the other two
2. `002_units.md` — milli- and kilo- prefixes, and why mixed units give answers that are wrong by a thousand
3. `003_proportion.md` — share a voltage the way a divider does
4. `004_rate_and_dt.md` — rate times time step
5. `005_angles_and_distance.md` — degrees, radians, wrap, distance, heading
6. `006_mean_and_blend.md` — mean of readings, and a weighted blend of two angles

### Estimated hours

- If the Falstad numbers already felt easy: 2–3 hours
- If you are relearning this from scratch: 5–8 hours. That time is part of Module 1, not extra guilt.

### Assessment criteria

- Given any two of voltage, current, and resistance, can you find the third and attach the unit?
- Can you convert 12 mA to amps and 4.7 kΩ to ohms, then divide them without being out by a thousand?
- Can you say what share of 5 V sits across the bottom resistor of a 1 kΩ / 3 kΩ divider without reaching for a new formula?
- Can you update an angle of 10° when a gyroscope reads 20° per second for 0.1 s?
- Can you convert 180° to radians, wrap 190° into the range (−180, 180], and get the distance from (0, 0) to (3, 4)?
- Can you find the mean of three readings and blend two angle guesses with a weight of 0.98?


## 1.6 Python, Terminal, and Git



### What to learn

You will use all three every week from here to your track.

Finish the calculation files that this section uses (`004`–`006` in `1.5_maths_practice/`) before the matching Python files. The Python exercises assume the numbers, not the other way around.

- **Python:** functions, classes, file I/O, JSON, virtual environments, pip
- **Terminal:** cd, ls, grep, running scripts, environment variables, SSH
- **Git:** init, add, commit, push, branches, writing a README someone can follow



### Resources


| Resource                                                                           | Format           | Why                                                                                                                        | Path                                                     |
| ---------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [Python for Everybody (Coursera)](https://www.coursera.org/specializations/python) | Free to audit    | Gentler starting point; enough for this syllabus if you do the problem sets                                                | Standard default                                         |
| [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Free             | Rigorous, with problem sets and a final project. A 30–50 hour course hiding inside this module if you treat it as required | Optional (or Fast-path skip if you already write Python) |
| [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)        | Free             | Shell, scripting, CLI fluency — lectures 1–3 and 4 (data wrangling) are enough now                                         | Mandatory unless Fast-path skip                          |
| [Learn Git Branching](https://learngitbranching.js.org/)                           | Free interactive | Visual tool for branches and merges                                                                                        | Mandatory unless Fast-path skip                          |




### Estimated hours

- Python (Python for Everybody core, or equivalent you already have): 15–25 hours Standard / 0 Fast-path skip
- Missing Semester (selected): 4–6 hours
- Learn Git Branching: 2–3 hours
- First repo and README: 2–4 hours



### Practice tasks

**Mandatory.** From today, every project you build lives in a GitHub repo with a README that has:

1. A photo or diagram
2. A wiring or architecture description
3. A section titled **"What broke and how I fixed it"**

That last section is what makes a repo look like engineering instead of a tutorial.

**Mandatory unless Fast-path skip.** Create a virtual environment, install a package, write a Python function that reads a CSV and writes JSON, commit it on a branch, merge, push.

**Mandatory unless Fast-path skip.** Complete the Python practice exercises in [`1.6_python_practice/`](1.6_python_practice/) before the capstone task. Each exercise has a spec and assertions — run them to check your work. Do `1.5_maths_practice/004_rate_and_dt.md` before `004_timed_loop.py`, and `005_angles_and_distance.md` before `005_angles.py`.

Do them in numbered order:

1. `001_format_pick.py` — functions and lists
2. `002_decisions.py` — `if` / `else` on a sensor value
3. `003_loops.py` — `for`, `while`, and `range`
4. `004_timed_loop.py` — period, leftover sleep, and a time step (`dt`)
5. `005_angles.py` — degrees, radians, distance, heading
6. `006_file_io_json.py` — CSV in, JSON out
7. `007_error_handling.py` — retries and your own error type
8. `008_drive_log.py` — put 001–007 together: clean a CSV drive log, replay it, write JSON
9. `009_reading_class.py` — classes
10. `010_env_pip.py` — virtual environments and pip
11. `011_serial.py` — parse lines as if they came from a microcontroller
12. `012_aggregate_sensors.py` — group readings and compute stats with loops
13. `013_numpy_basics.py` — arrays, variance, moving average
14. `014_numpy_robotics.py` — rotate a point, combine two moves, blend gyro and accelerometer angles
15. `015_imu_heading.py` — put the whole folder together: estimate heading from a fake motion-sensor log

### Assessment criteria

- Can you create a virtual environment, install a package, and run a script?
- Can you explain `init`, `add`, `commit`, `push`, and `branch` to someone?
- Can you write a Python function that reads a CSV file and writes a JSON file?
- After `008`, can you clean a messy drive log, skip bad rows, replay it, and write JSON?
- After `015`, can you estimate a heading from a fake motion-sensor log and write a short report?



## Module 1 Milestones


| Criterion                                                              | Test                                                               | Required?            |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------- |
| Read a schematic and build the circuit it describes on a breadboard    | Given a new schematic, build it without a tutorial                 | Mandatory            |
| Do the calculation practice set without looking up the method          | All six files in `1.5_maths_practice/`, answers checked            | Mandatory            |
| Calculate whether a resistor value is right before you plug it in      | Solve a series LED + resistor for correct current                  | Mandatory            |
| Find a short, a break, or a dead component with a multimeter           | Given a broken circuit, locate the fault without visual inspection | Mandatory            |
| Solder a clean through-hole joint and check it electrically            | Produce 5 consecutive good joints                                  | Mandatory if Tier 2+ |
| Write a Python script, run it from the terminal, and push it to GitHub | Repo with README, code, and commit history                         | Mandatory            |
| Explain out loud why a motor stalling can reset your microcontroller   | Verbal explanation with a circuit diagram                          | Mandatory            |
| Show PWM duty cycle on a scope                                         | Measured frequency and duty                                        | Mandatory if Tier 3  |


