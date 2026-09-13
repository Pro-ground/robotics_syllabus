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