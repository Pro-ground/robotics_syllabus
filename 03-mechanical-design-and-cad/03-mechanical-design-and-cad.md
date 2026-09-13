# Module 3: Mechanical Design, CAD, and Manufacturing

**Estimated time:** 8 weeks · **80–120 hours** (Standard) · Fast path: 4 weeks · 45–65 hours  
**Prerequisites:** Module 2 — you can read datasheets, wire circuits, and have built the line follower (or equivalent).

## Goals

By the end of this module you should be able to:

- Model a part from a datasheet in CAD with fully constrained sketches
- State your printer's (or print service's) real clearance numbers from measurement rather than guesswork
- Design a part specifically for FDM, accounting for orientation, overhangs, and layer adhesion
- Choose PLA, PETG, ABS, or TPU for a given part and justify it
- Explain what backlash is
- Show a working robot arm you assembled, calibrated, and modified with at least one part of your own

## 3.1 Computer-Aided Design (CAD)

Pick one tool and go deep rather than sampling all of them.

**Decision framework:**

| Tool | Pros | Cons | When to choose |
|---|---|---|---|
| **Onshape Free** | Runs in browser, works on any machine including Chromebook, assembly/mate system behaves like real robot joints | Every document is public on the free tier | Happy designing in public, want a credential for your CV |
| **Fusion Personal** | CAM integration, 3D-print integration, industry-standard | Revocable licence, limited import/export on free tier | Want CAM later, revenue under $1,000/year |
| **FreeCAD** | Open source, no licence, no card payment required | Steeper learning curve, UI is less polished | Cloud CAD or card payment is a problem, or you object to revocable licences |
| **SOLIDWORKS for Makers** | Industry-standard tool | $48/year, native files are watermarked | Want SW specifically |

### Concepts

- Fully constrained sketches — an under-constrained sketch will move when you edit it later and ruin your day
- Parametric design driven by variables — changing one dimension updates the whole part
- Assemblies and mates that mirror real joints: revolute, slider, fixed, cylindrical
- Designing around hardware you actually own — start from the servo's datasheet dimensions, not from guesswork
- Exporting STEP for sharing and STL for printing, and knowing the difference

### Resources

| Resource | Format | Why |
|---|---|---|
| [Onshape Learning Center: Fundamentals CAD](https://learn.onshape.com/learning-paths/onshape-fundamentals-cad) | Free with account | Only free structured CAD curriculum that ends in a credential, ships a robotics-competition track |
| [Product Design Online, Learn Fusion in 30 Days](https://productdesignonline.com/learn-autodesk-fusion-360-in-30-days-official-course/) | Free | 30 modeled objects in 30 days — do **week 1–2**, not all 30, unless CAD is your job |
| [MangoJelly Solutions FreeCAD tutorials](https://www.youtube.com/@MangoJellySolutions) | Free videos | Best FreeCAD teacher for makers |
| [Protolabs Network, Design for 3D Printing](https://www.hubs.com/knowledge-base/design-for-3d-printing/) | Free | Wall thickness, orientation, tolerances, supports, snap-fits, STL vs 3MF vs STEP |

### Estimated hours

- Chosen CAD tool, enough to model a constrained bracket: 10–16 hours
- Design-for-manufacture reading: 2–3 hours
- Bracket iterate-to-fit: 6–12 hours including print wait

### Practice tasks

1. **Mandatory.** Model a bracket that holds a servo or motor you own (or the SO-101 servo from the datasheet), with correctly sized screw holes and a shaft clearance, from the manufacturer's drawing rather than by eye.
2. **Mandatory.** Manufacture it (home printer, Fab Lab, or print service) and see if it fits — which it probably will not the first time.
3. **Mandatory.** Iterate until it fits.
4. **Optional.** Change one parameter and have the assembly update. Export STEP and reopen it.

### Assessment criteria

- Is every sketch fully constrained (all lines/points turn black or dark blue in Onshape, or show "Fully Defined" in Fusion)?
- Can you change a single variable and have the part update correctly?
- Can you export a STEP file?

## 3.2 3D Printing

### What to learn

- Filament selection and when to use each
- Printer calibration: temperature tower, flow rate, pressure advance, retraction, tolerance
- Print orientation and why it matters (layer adhesion is the weakest direction)
- Tolerances and clearance for your specific machine
- Design for FDM: wall thickness, overhangs, supports, bridging, snap-fits

**Filament guide:**

| Material | Use case | Pros | Cons |
|---|---|---|---|
| **PLA/PLA+** | Prototype brackets, jigs, SO-101 arm (specifies PLA+ at 15% infill, 0.2mm layers) | Stiffest of the easy materials | Creeps under sustained load, softens ~55–60°C |
| **PETG** | Default real robot part: chassis plates, gearbox housings, servo mounts | Tough, better layer adhesion than PLA | Stringy |
| **ABS/ASA** | Parts near hot motors, outdoor rovers | Heat resistant | Warps badly without enclosure |
| **Nylon** | Gears, cable guides | Strong, flexible | Easier to order than to print |
| **CF-filled** | Stiff structural links | Very stiff | Abrasive — needs hardened nozzle |
| **TPU** | Feet, bumpers, compliant gripper fingers | Flexible, grippy | Slow to print |

### Printer prices (verified, September 2026)

| Printer | Price | Notes |
|---|---|---|
| Creality Ender-3 V3 SE | $199 | Entry-level, good for learning |
| Bambu Lab A1 mini | $219.99 | Small bed (180mm class) — check current bed size before you buy |
| Bambu Lab A1 | $299.99 | Larger bed you will want for bigger brackets |
| Creality K1C | $369 | Enclosed, hardened for carbon-fibre filaments |
| Bambu Lab P1S | $799 | Enclosed CoreXY for ABS and ASA |

You do **not** need to buy a printer to finish this syllabus.

### Resources

| Resource | Format | Why |
|---|---|---|
| [OrcaSlicer Calibration wiki](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration) | Free docs | Temperature, flow, pressure advance, retraction, tolerance |
| [Teaching Tech 3D Printer Calibration](https://teachingtechyt.github.io/calibration.html) | Free interactive | Printer-agnostic walkthrough |
| [CNC Kitchen (YouTube)](https://www.youtube.com/@CNCKitchen) | Free videos | Instrumented strength tests on infill, walls, inserts, orientation |
| [Clearance and Tolerance Gauge (STL)](https://www.printables.com/model/57067-clearance-and-tolerance-3d-printer-gauge) | Free STL | Print once, know your machine's real clearance |

### If you cannot buy a printer

| Option | Notes |
|---|---|
| [Fab Labs](https://fablabs.io/labs) | ~2,875 worldwide, searchable by country |
| Public library makerspaces | Free or near-free in much of the US and some other countries |
| [Craftcloud](https://craftcloud3d.com/) | Compares quotes across 95 countries |
| [JLC3DP](https://jlc3dp.com/) | Starts at $1.00/part for MJF nylon and FDM, 3-day builds |

### The honest economics

An SO-101 arm needs roughly 1kg of PLA+, about $20–$25 of filament on your own machine against $30.99 for a ready-printed set. A printer does not pay for itself on one build. It pays for itself on iteration.

### Estimated hours

- Printer setup and calibration (if you bought one): 8–14 hours including failed prints
- Tolerance gauge + snap-fit: 4–8 hours
- Using a service: 2–4 hours of file prep plus wait time (do not count shipping as study hours, but plan the calendar)

### Practice tasks

1. **Mandatory.** Get one physical part in your hands from a design you made (home, lab, or service).
2. **Mandatory if you own a printer / Optional if using a service.** Print the tolerance gauge. Write down clearance numbers for press fits and sliding fits.
3. **Optional.** Design and print a two-part snap-fit enclosure for your ESP32 that closes without glue. Iterate until it clicks.
4. **Optional.** Write a three-line filament justification for PLA vs PETG vs TPU on three different parts.

### Assessment criteria

- Can you state clearance numbers from measurement, or the service's published tolerance?
- Can you justify filament choice for a given part?
- Can you design for FDM — orientation, overhangs, layer adhesion?

## 3.3 Actuators, Transmissions, and Why Robots Are Hard

Understanding gear reduction, backlash, and torque density is what separates a robot that works in a video from a robot that works repeatedly.

### What to learn

- Gear ratios and the trade-off between speed and torque
- Backlash — why it destroys position accuracy in a way software cannot fully fix
- Bearing selection and preload (vocabulary; you do not need to spec a preload this month)
- Belt versus gear versus direct drive
- Why a cheap servo's plastic gearset is the first thing to fail on any arm

A printed planetary or cycloidal reducer is a **multi-week project**, not a 4-hour lab. Treat it as Optional. You can learn backlash by measuring a cheap servo horn or a printed spur pair.

### Estimated hours

- Reading and video: 3–4 hours
- Measure backlash on something you already have: 1–2 hours
- Optional printed reducer: 15–40 hours — only if you are heading Embedded/Mechatronics and have calendar room

### Practice tasks

1. **Mandatory.** Calculate gear ratio and output torque for a given motor and gearset (use the datasheet of a motor you own, or the SO-101 servo).
2. **Mandatory.** Demonstrate backlash: hold an output and rock it. Measure the angle or linear play. Write two sentences on why software cannot fully cancel it.
3. **Optional / not Fast path.** Design and print a simple planetary or cycloidal reducer. Accept that the first one will be bad. Redesign to reduce backlash. Reference: [OpenCycloid](https://www.instructables.com/OpenCycloid-3D-printed-Open-Source-Robotic-Actuato/).

### Assessment criteria

- Can you explain what backlash is and show it on hardware you have?
- Can you calculate gear ratio and output torque?

## 3.4 Build a Real Robot Arm

This is the capstone of Module 3 and the best hardware purchase in the trunk.

### The SO-101

The SO-101 is an open-source 5-DOF arm plus gripper from TheRobotStudio and Hugging Face, designed to be built as a leader and follower pair so you can hand-guide one and have the other mirror it. That teleoperation setup is what the Learning track is built on.

**Official bill of materials (verified in repo):**
- $229.88 US for a leader and follower pair, excluding 3D printing
- $121.94 for a single follower arm, excluding 3D printing

Where to buy: [github.com/TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100)

### Which arm to buy

| Path | What to buy | Why |
|---|---|---|
| **Mandatory / Fast hardware path** | Single follower + print parts yourself or buy the $31 printed set | Keeps the entire software path. Teleop with a gamepad, keyboard, or MuJoCo leader. |
| **Standard if budget allows** | Leader + follower pair | Best for the Learning track. Buy this if you already know you will take that track. |
| **If you cannot import hardware** | $0 — LeRobot stack in MuJoCo | Valid. Say so in the README. You cannot claim hardware calibration. |

### Pricing

| Source | Price | Notes |
|---|---|---|
| Seeed Studio SO-ARM101 Pro servo kit | $277.99 | Motors and control boards without printed parts |
| Seeed Studio printed parts set | $30.99 | If you have no printer |
| Robonine SO-ARM101 complete kit | $349.00 | Ships from Delaware |
| WowRobo via OpenELAB | $325.99 printed + servos / $489.99 fully assembled | |

### Cheaper alternatives

| Cost | Option | Notes |
|---|---|---|
| $0 | LeRobot stack in MuJoCo | If you cannot import anything |
| $50–80 | EEZYbotARM MK2 | Free STLs, MG996R hobby servos — teaches linkage kinematics |
| $122 | Single SO-101 follower (print yourself) | **Recommended default** |
| $199.99 | Hiwonder xArm 1S | Intelligent bus servos that report position and voltage |

### Estimated hours

- Single follower assembly and calibration: 10–16 hours
- Leader + follower + teleop: 14–22 hours
- Custom gripper fingers: 4–8 hours

### Practice tasks

1. **Mandatory.** Assemble one arm (follower, or EEZYbot / xArm if that is what you have). Calibrate every servo's zero.
2. **Mandatory.** Command the arm through a few poses (leader, gamepad, or script) and film it.
3. **Mandatory.** Design and manufacture **one** replacement part (gripper finger, camera mount, or cable clip). It does not have to be TPU if you have no flexible filament — document the compromise.
4. **Optional.** Full leader–follower teleop across the workspace.
5. **Optional.** TPU fingers tested on three object shapes.

The arm is the platform for Module 6 kinematics, Module 7 (if you capstone on the arm), and the Learning track. The custom part is what proves you can design as well as assemble.

### Assessment criteria

- Can you calibrate every servo to a known zero?
- Can you move the arm through a repeatable motion and film it?
- Did you design and manufacture at least one custom part that is on the robot?

## Module 3 Milestones

| Criterion | Test | Required? |
|---|---|---|
| Model a part from a datasheet in CAD with fully constrained sketches | Servo/motor bracket from scratch | Mandatory |
| State real clearance or service tolerance numbers | Gauge print or vendor spec in the README | Mandatory |
| Design a part for FDM | Show orientation and support strategy | Mandatory |
| Choose a filament and justify it | Written justification for the custom part | Mandatory |
| Explain backlash and show it | Measurement on a servo or gearset | Mandatory |
| Working arm, calibrated, with one custom part | Video + part on the robot | Mandatory |
| Printed cycloidal/planetary reducer | Backlash before/after | Optional |
| Leader–follower teleop | Video across full range | Optional |
