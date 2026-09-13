# Module 1: Electronics, Tools, and Foundations

**Estimated time:** 8 weeks · **80–100 hours** (Standard) · Fast path: 3 weeks · 35–45 hours
**Prerequisites:** None. This module starts from zero electronics knowledge.

Hours include buying parts, waiting for shipping (plan around it), failed joints, and writing READMEs. They are not watch time.

---

## Quick-Reference Index

If you already know some of this, jump straight to the section you need. These are the standalone skills used throughout the module; they don't have their own spiral cycle because they get applied across cycles.


| Skill                                          | Page                       |
| ---------------------------------------------- | -------------------------- |
| How to read a schematic                        | [below](#reference-skills) |
| Soldering technique                            | [below](#reference-skills) |
| Using a multimeter                             | [below](#reference-skills) |
| Python basics (functions, loops, files, NumPy) | [below](#reference-skills) |
| Terminal and Git                               | [below](#reference-skills) |
| Oscilloscope basics (Tier 3)                   | [below](#reference-skills) |
| Safety (LiPo, soldering fumes, eye protection) | [below](#reference-skills) |


---



## Goals

By the end of this module you should be able to:

- Read a schematic and build the circuit it describes on a breadboard
- Calculate resistor values and verify them with a multimeter
- Find a short, a break, or a dead component with diagnostic tools
- Solder a clean through-hole joint and verify it electrically
- Write a Python script, run it from the terminal, and push it to GitHub
- Explain why a motor stalling can reset a microcontroller

---



## How This Module Is Structured

This module uses a **spiral approach**: each major concept is encountered in multiple modalities, building deeper understanding each time. You don't "finish" a topic after one pass. You meet it four times:

1. **Theory** — why the circuit works, equations, rules of thumb
2. **Simulate** — Falstad or Tinkercad, where you can see current flow and change values without buying anything
3. **Build** — real parts on a breadboard, where tolerances, messy wires, and real-world quirks appear
4. **Make permanent** — solder the circuit onto perfboard, where you learn to commit to a layout and debug something you can't just undo by plugging a different wire in

Reference skills (soldering, multimeter, Python, Git) sit at the back and are consulted as needed. You'll use them in the cycles but they don't have their own cycle — they're the tools the cycles are built with.  
Reference Skills

These are the standalone skills used throughout the module and in every module that follows. They are not spirals — they are layering skills. You learn them once and use them repeatedly. Consult them as needed during the above.

### How to Read a Schematic

A schematic is a map. It doesn't show where components are placed — it shows how they are connected.

- **Symbols** — resistor, capacitor, diode, transistor, ground, Vcc. These are standard. If you don't know a symbol, look it up; you will need it.
- **Net labels** — text next to a wire that tells you it connects to something else with the same label. Two dots on a line mean the wires cross and connect. A dotless crossing means the wires do not connect.
- **Power symbols** — `VCC`, `+5V`, `GND`, `+3.3V`. These are shortcuts for connections to a power rail. You don't trace them on the schematic; you trace them on the board.
- **Ground symbols** — there are many types. Chassis ground (mounting), signal ground (reference), and earth ground (AC mains safety). In robotics, signal ground is what matters: it is the common reference voltage for all your measurements.

**Practice:** Take any schematic from the Falstad exercises and build it on breadboard without looking at a wiring diagram — only the schematic. If you can do that, you can read any schematic.

### Soldering

**Resources:**


| Resource                                                                                               | Format     | Why                                                          |
| ------------------------------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| [Adafruit Guide to Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering) | Free guide | Iron selection, joint technique, failure photographs, safety |


**What to focus on:**

- Tinning the tip and keeping it clean
- Heating the joint, not the solder
- Recognizing a cold joint by sight and touch
- Through-hole first, surface-mount much later
- Using flux — fixes most problems beginners blame on the iron
- Desoldering: pump, wick, and when to give up

**Practice tasks:**

1. Solder header pins onto a cheap breakout board. Test every pin with continuity mode. Do it three times.
2. Desolder one and resolder it — removing components badly is how most beginners destroy boards.
3. Fast-path skip / Optional on Tier 1: If you have no iron yet, stay on jumper wire for Module 2 and solder before the arm in Module 3.

**Assessment criteria:**

- Can you identify a cold joint vs. a good joint from a photograph?
- Can you solder a through-hole joint in under 5 seconds?
- Can you desolder a component without lifting the pad?



### Using a Multimeter

**Resources:**


| Resource                                                                                          | Format     | Why                                                                 |
| ------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------- |
| [SparkFun: How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter) | Free guide | Voltage, current, continuity, and what to do when you blow the fuse |


**Modes:**


| Mode       | What it measures                        | When to use it                                          |
| ---------- | --------------------------------------- | ------------------------------------------------------- |
| DC Voltage | Potential difference between two points | Is the supply at the right voltage?                     |
| AC Voltage | Alternating potential difference        | Rarely in robotics. Ignore.                             |
| Resistance | Opposition to current flow              | Is a resistor the right value?                          |
| Continuity | Whether two points are connected        | Is this wire broken? Is there a short?                  |
| DC Current | Flow of charge through a circuit        | Measuring supply current (break the circuit to do this) |


**Golden rule:** Always start on the highest range if you're unsure. Setting the meter to measure 200mV when the circuit has 12V will blow the fuse.

### Oscilloscope Basics (Tier 3)

**Resources:**


| Resource                                                                            | Format      | Why                                      |
| ----------------------------------------------------------------------------------- | ----------- | ---------------------------------------- |
| [EEVblog oscilloscope tutorial series](https://www.youtube.com/watch?v=Oe9kF8s3f0Q) | Free videos | Best practical intro to oscilloscope use |


**What to focus on:**

- Voltage vs. time display: what you're actually looking at
- Triggering: making a waveform appear stable on the screen
- Measuring frequency and duty cycle of PWM signals
- Current sensing: using a shunt resistor or a current probe to see motor current

If you are on Tier 0–2, learn the concepts from video and measure what you can with a multimeter. Hands-on PWM and I2C traces wait until you have Tier 3. Do not assess yourself on traces you have never seen.

### Python for Robotics

**What to learn:**

- **Python:** functions; choosing with `if` and `else`; loops; a loop that keeps time; degrees and radians; reading and writing files (including CSV and JSON); handling errors; classes; virtual environments and pip; parsing text lines as if they came from a microcontroller; NumPy (the array library most robotics Python uses)
- **Terminal:** cd, ls, grep, running scripts, environment variables, SSH
- **Git:** init, add, commit, push, branches, writing a README someone can follow

**Resources:**


| Resource                                                                           | Format           | Why                                                                                                                        |
| ---------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Python for Everybody (Coursera)](https://www.coursera.org/specializations/python) | Free to audit    | Gentler starting point; enough for this syllabus if you do the problem sets                                                |
| [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Free             | Rigorous, with problem sets and a final project. A 30–50 hour course hiding inside this module if you treat it as required |
| [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)        | Free             | Shell, scripting, CLI fluency — lectures 1–3 and 4 are enough now                                                          |
| [Learn Git Branching](https://learngitbranching.js.org/)                           | Free interactive | Visual tool for branches and merges                                                                                        |


**Practice tasks:**

**Mandatory.** From today, every project you build lives in a GitHub repo with a README that has:

1. A photo or diagram
2. A wiring or architecture description
3. A section titled **"What broke and how I fixed it"**

That last section is what makes a repo look like engineering instead of a tutorial.

**Mandatory unless Fast-path skip.** Create a virtual environment, install a package, write a Python function that reads a CSV and writes JSON, commit it on a branch, merge, push.

**Mandatory unless Fast-path skip.** Complete the Python practice exercises in `1.5_python_practice/` before the capstone task. Each exercise has a spec, a "What you will need" list, and assertions — run the file to check your work.

Do them in numbered order:

1. `001_format_pick.py` — functions and lists
2. `002_decisions.py` — `if` / `else` on a sensor value
3. `003_loops.py` — `for`, `while`, and `range`
4. `004_timed_loop.py` — period, leftover sleep, and a time step (`dt`)
5. `005_angles.py` — degrees, radians, distance, heading
6. `006_file_io_json.py` — CSV in, JSON out
7. `007_error_handling.py` — retries and your own error type
8. `008_reading_class.py` — classes
9. `009_env_pip.py` — virtual environments and pip
10. `010_serial.py` — parse lines as if they came from a microcontroller
11. `011_aggregate_sensors.py` — group readings and compute stats with loops
12. `012_numpy_basics.py` — arrays, variance, moving average
13. `013_numpy_robotics.py` — rotate a point, combine two moves, blend gyro and accelerometer angles

**Assessment criteria:**

- Can you create a virtual environment, install a package, and run a script?
- Can you explain `init`, `add`, `commit`, `push`, and `branch` to someone?
- Can you write a Python function that reads a CSV file and writes a JSON file?



### Safety

- **LiPo batteries:** never leave a LiPo charging unattended. Charge on a fireproof surface. If a cell swells, do not puncture it.
- **Soldering fumes:** ventilate. Use a fume extractor or work near an open window. Flux smoke is not pleasant.
- **Eye protection:** clip leads and solder splatter fly. Safety glasses are $5 and prevent a real injury.
- **Wrist strap / touch ground:** before handling ICs, touch a grounded metal surface to discharge static electricity.

---



## Section 1: Voltage Dividers and Measuring

> **What you'll build:** A voltage divider that produces a known fraction of a supply voltage, measured by hand, simulator, and multimeter, then soldered and read by Python.
>
> **Why this first:** It is the simplest circuit that has two components interacting to produce a useful output, and every other electronics skill you learn depends on being comfortable with it.



### Step 1 — Theory: Ohm's law, KVL, and the voltage divider equation

**Resources:**


| Resource                                                                                                                                          | Format           | Why                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------- |
| [All About Circuits, DC Vol. 1, Chapter 2](https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relations/) | Free textbook    | Kirchhoff's laws and Ohm's law with worked examples                       |
| [Afrotechmods: Resistors in Series and Parallel](https://www.youtube.com/watch?v=KdHf1ObYJ6w)                                                     | Short video      | Intuition before algebra                                                  |
| [Ultimate Electronics, Section 2.12–2.15](https://ultimateelectronicsbook.com/)                                                                   | Free online book | The best treatment of nodes, labelling, and solving a circuit as a system |


**What to focus on:**

- Ohm's law (`V = I * R`) and when to use it
- Kirchhoff's Voltage Law: the sum of voltage drops around any closed loop equals the supply
- The voltage divider formula: `V_out = V_in * R2 / (R1 + R2)`, and why it is just Ohm's law applied to a series loop
- Series circuits: the same current flows through every component
- How to calculate resistor values from power ratings

**What to learn by the end of this step:**

Given a 9V battery, a 1 kΩ resistor, and an LED with a forward voltage of 2V, calculate the resistor needed to run the LED at 20mA. (Hint: the resistor and LED are in series; the resistor drops `9V - 2V = 7V`.)

### Step 2 — Simulate: Build it in Falstad

**Resources:**


| Resource                                                      | Format           | Why                                               |
| ------------------------------------------------------------- | ---------------- | ------------------------------------------------- |
| [Falstad Circuit Simulator](https://www.falstad.com/circuit/) | Free browser app | Animated electron flow and live voltage colouring |


**Task:**

1. Open Falstad. Build a voltage divider: two resistors in series between Vcc and ground, with a voltmeter between them.
2. Calculate the output voltage by hand. Then set the resistor values in the simulator and confirm your calculation.
3. Change one resistor value and predict what happens to `V_out`. Update the simulator and check.
4. Add a second voltmeter across the top resistor and one across the bottom. Watch how the voltage splits proportionally.
5. Replace the bottom resistor with an LED. Watch the LED light up more brightly as you adjust the top resistor — that's the real-world voltage divider with a non-linear load.

**Work through** `01-falstad-exercises.md` **(exercises A–C).** These are ordered from simplest divider to more complex configurations. Do them before touching real parts.

### Step 3 — Build: Real breadboard, real multimeter

**What you'll need:** A breadboard, a 5V power supply (or USB cable), two 10 kΩ resistors, jumper wires.

**Task:**

1. Build the same voltage divider you simulated — two 10 kΩ resistors in series, 5V on top, ground on bottom.
2. Measure the mid-point voltage against ground with a multimeter in DC voltage mode. It should read close to 2.5V. How close? That tells you about resistor tolerance.
3. Now swap one resistor for a 4.7 kΩ. Recalculate what `V_out` should be, then measure it. The equation works on real parts too.
4. Measure the resistance of five random resistors with your multimeter's ohmmeter. Check each against the colour bands. Note any discrepancies.
5. Intentionally break one connection — pull a wire out or reseat a component in the wrong row. Use continuity mode to find the break without looking at the board.

**This is where theory meets reality.** Your 10k resistor probably isn't exactly 10k. The multimeter has its own tolerance. The breadboard adds a few ohms of contact resistance. These are not mistakes; they're the first lesson in why you always measure.

### Step 4 — Python: Read sensor data and process it

**Resources:**


| Resource                              | Format        | Why                   |
| ------------------------------------- | ------------- | --------------------- |
| `1.5_python_practice/006_file_io_json.py` | Exercise file | CSV read + JSON write |


**Task:**

Write a Python function that takes a CSV file of voltage divider measurements (sensor_name, value, unit) and writes the filtered results to JSON. This is the bridge between the physical circuit and the software that will read sensors on a real robot.

Complete the exercises in `1.5_python_practice/` before the capstone task, in the order listed in the Python for Robotics section. Each exercise has a spec and assertions — run them to check your work.

### Step 5 — Make permanent: Solder the divider onto perfboard

> **Skip for now if you don't have a soldering iron yet. The reference skill section below tells you when to learn it.**

Transfer the voltage divider from breadboard to perfboard. Solder every joint. Test every connection with continuity mode. This is the first time you commit to a layout you can't undo.

**By the end of Cycle A you can:**

- Calculate `V_out` for any two-resistor divider
- Build it in Falstad, on breadboard, and soldered
- Measure it with a multimeter and interpret tolerance drift
- Find a break you made yourself using continuity mode
- Write a Python function that reads measurement data from CSV

---



## Section 2: Transistor Switches and Active Circuits

> **What you'll build:** A transistor switch that turns an LED on from a logic-level input. This is the exact circuit that lets a 3.3V microcontroller pin control something that needs more current than the pin can supply.
>
> **Why this next:** Voltage dividers are passive. Transistors introduce active control — a small input signal controls a larger output. Everything in robotics depends on this pattern.



### Step 1 — Theory: Switching, transistors, and pull-up resistors

**Resources:**


| Resource                                                                                                                                              | Format         | Why                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------- |
| [All About Circuits, DC Vol. 1, Chapter 4: Transistor Circuits](https://www.allaboutcircuits.com/textbook/direct-current/chpt-4/transistor-circuits/) | Free textbook  | NPN transistor as a switch, biasing, saturation            |
| [Afrotechmods: How a Transistor Works](https://www.youtube.com/watch?v=1WzMtP2hft8)                                                                   | Short video    | Intuition about base current controlling collector current |
| [Falstad: Transistor as Switch](https://www.falstad.com/circuit/e-transswitch.html)                                                                   | Free simulator | See base current trigger collector current                 |


**What to focus on:**

- What a transistor does: a small base current controls a much larger collector current
- NPN vs PNP: which way the current flows, how to wire each
- Saturation: when a transistor is fully "on" and acts like a closed switch
- Why you need a base resistor: without it, too much base current destroys the transistor
- Pull-up and pull-down resistors: why digital inputs need a defined default state
- What a diode does: protects against back-EMF when a transistor switches off an inductive load (like a motor)

**What to learn by the end of this step:**

Given a 5V supply, an NPN transistor, an LED, and a 3.3V logic input, sketch the circuit that turns the LED on when the logic input is high. What resistor values do you choose for the base and the LED?

### Step 2 — Simulate: Transistor switch in Falstad and Tinkercad

**Resources:**


| Resource                                                                         | Format            | Why                                    |
| -------------------------------------------------------------------------------- | ----------------- | -------------------------------------- |
| [Falstad: Transistor Switch](https://www.falstad.com/circuit/e-transswitch.html) | Free simulator    | See the exact circuit you're building  |
| [Tinkercad Circuits](https://www.tinkercad.com/circuits)                         | Free with account | Virtual breadboard, virtual multimeter |


**Tasks:**

1. In Falstad: build the transistor switch circuit. Turn the base on and off. Watch the LED light and the current through the collector.
2. In Tinkercad: build the same circuit on a virtual breadboard. Wire it the same way. Use the virtual multimeter to measure the voltage at the collector when the transistor is on and when it is off.
3. Add a resistor to the base. Predict what happens to the base current. Update the circuit and check.
4. Add a flyback diode across a small motor instead of the LED. Watch what happens when you switch off — without the diode, the collapsing magnetic field creates a voltage spike that can damage the transistor.

**Work through** `01-falstad-exercises.md` **(exercises D–G).** These build from a simple divider to transistor switches and basic logic circuits.

### Step 3 — Build: Real transistor switch on breadboard

**What you'll need:** NPN transistor (2N2222 or BC547), LED, three resistors (1 kΩ, 10 kΩ, a current-limiting resistor for the LED), 5V supply, breadboard, jumper wires.

**Task:**

1. Build the transistor switch. Connect the base to a 3.3V source through a 10 kΩ resistor. The LED + current-limiting resistor goes on the collector side.
2. Measure the voltage at the base, collector, and emitter with a multimeter. The collector should be close to 5V when the transistor is off and close to 0V when it is on.
3. Swap the 10 kΩ base resistor for different values. Watch how the LED brightness changes — the transistor is acting like a variable resistor before it hits saturation.
4. Build a pull-up resistor circuit: connect a resistor between Vcc and a microcontroller input pin, and a button between the pin and ground. Measure the voltage at the pin when the button is pressed and released.

**Optional — motor load:** If you have a small DC motor, replace the LED. Measure the back-EMF spike on a scope (Tier 3) or just observe what happens to a transistor with and without a flyback diode.

### Step 4 — Solder: Move the circuit to perfboard

**Reference:** See the [Soldering](#reference-skills) section below for technique.

Solder the transistor switch circuit onto perfboard. Every joint. Every connection. This is your first full circuit on permanent hardware. Test it after every soldering session — don't wait until it's all done and hope for the best.

### Step 5 — Python: Log the measurements

Use the Python functions you built in Cycle A to read and filter the voltage measurements from your transistor switch experiments. Write a function that compares the measured collector voltage to the expected value and flags any readings outside tolerance.

**By the end of Cycle B you can:**

- Sketch a transistor switch circuit from memory
- Wire it on breadboard and verify operation
- Choose correct resistor values for base and collector
- Understand pull-up and pull-down resistors
- Solder the circuit to perfboard
- Log and compare measured values against expected values

---



## Section 3: Power, Real-World Behaviour, and Noise

> **What you'll build:** A complete circuit with a power supply, decoupling, and a motor load — observing how real power behaves when a motor stalls.
>
> **Why this last:** This is where theory, simulation, breadboarding, and soldering all come together. It's the cycle that connects directly to everything in Module 2 (motors, microcontrollers, sensors).



### Step 1 — Theory: Battery chemistry, regulator sag, and decoupling

**Resources:**


| Resource                                                                                                                                                    | Format        | Why                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------- |
| [All About Circuits, DC Vol. 1, Chapter 11: Batteries](https://www.allaboutcircuits.com/textbook/direct-current/chpt-11/batteries-and-power-supplies/)      | Free textbook | Battery types, ratings, internal resistance |
| [Afrotechmods: Capacitors](https://www.youtube.com/watch?v=4Z2dYmJgJcM)                                                                                     | Short video   | What a capacitor actually does in a circuit |
| [All About Circuits, AC Vol. 1, Chapter 2: Capacitive Reactance](https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/capacitor-impedance/) | Free textbook | Decoupling capacitors and bypass            |


**What to focus on:**

- Battery chemistry: LiPo cell counts, C ratings, why you never leave a LiPo charging unattended
- Internal resistance: why a battery voltage sags under load and recovers when the load drops
- Voltage regulators: linear vs switching, dropout voltage, heat dissipation
- Decoupling capacitors: why every IC needs one near its power pins, what value to use, and how fast they respond
- Ground: why it's not just "the negative terminal" and how ground loops create noise
- Current draw: why a motor stalling browns out your regulator

**What to learn by the end of this step:**

Given a 3-cell LiPo (11.1V nominal, 30C rating) powering a motor that draws 2A normally and 10A when stalled, calculate whether the battery can safely supply the stall current. What happens if you add a 100µF decoupling capacitor across the motor terminals?

### Step 2 — Simulate: Weak supply + motor load in Falstad

**Task:**

1. Build a circuit with a voltage source, a regulator, and a motor (modelled as a resistive load that spikes). Watch the rail sag when the load increases.
2. Add a decoupling capacitor near the IC. Observe how it stabilises the rail during the spike.
3. Add a motor stall: replace the resistive load with a near-zero resistance briefly. Watch the voltage collapse. Sketch why this resets a microcontroller.

**Work through** `01-falstad-exercises.md` **(exercises H–L, if not already done).** These complete the simulation exercises with power-related circuits.

### Step 3 — Build: Measure power sag on real hardware

**What you'll need:** Battery or bench supply, a small DC motor, a voltage regulator (LM7805 or buck converter), a 100µF capacitor, breadboard, multimeter, oscilloscope (Tier 3).

**Task:**

1. Build a regulator circuit: battery → regulator → 5V rail. Measure the output with and without a capacitor.
2. Add a motor to the 5V rail. Start it. Watch the 5V rail with a multimeter — does it dip? How much?
3. Add a 100µF decoupling capacitor near the motor. Start it again. Measure the dip. Compare.
4. (Tier 3) Put the scope on the 5V rail. Trigger on the motor start. See the sag visually.
5. Stall the motor (gently!) and watch the rail collapse. This is why motors need their own supply rail.



### Step 4 — Solder: Final circuit, all skills combined

Solder the complete circuit: regulator, decoupling, motor, and whatever logic you built in Cycle B. This is your first full-skill build — you're using Ohm's law for calculations, breadboarding for prototyping, and soldering for permanence.

### Step 5 — Python: Data analysis on power measurements

Write a Python script that reads the power measurements from a CSV file, computes statistics, and writes a summary to JSON. This mirrors the real-world workflow of logging sensor data from a robot and analysing it afterwards.

**By the end of Section 3 you can:**

- Choose the right battery for a motor's current demand
- Explain why decoupling capacitors matter and what value to use
- Build a regulator circuit on breadboard and perfboard
- Measure power sag and verify the effect of decoupling
- Diagnose why a motor stall can reset a microcontroller
- Analyse power measurement data with Python

---



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

---



## Module 1 Milestones


| Criterion                                                              | Test                                                               | Required?            |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------- |
| Read a schematic and build the circuit it describes on a breadboard    | Given a new schematic, build it without a tutorial                 | Mandatory            |
| Calculate whether a resistor value is right before you plug it in      | Solve a series LED + resistor for correct current                  | Mandatory            |
| Find a short, a break, or a dead component with a multimeter           | Given a broken circuit, locate the fault without visual inspection | Mandatory            |
| Solder a clean through-hole joint and check it electrically            | Produce 5 consecutive good joints                                  | Mandatory if Tier 2+ |
| Write a Python script, run it from the terminal, and push it to GitHub | Repo with README, code, and commit history                         | Mandatory            |
| Explain out loud why a motor stalling can reset your microcontroller   | Verbal explanation with a circuit diagram                          | Mandatory            |
| Show PWM duty cycle on a scope                                         | Measured frequency and duty                                        | Mandatory if Tier 3  |


---



## Hardware Tiers (repeated for convenience)


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