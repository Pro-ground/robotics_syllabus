# Track: Embedded, Mechatronics, and Integration

**Estimated time:** 12 weeks · **120–160 hours** (Mandatory only: ~80–100)  
**Prerequisites:** Module 7. You have closed a loop on a microcontroller, a power budget, and a safety cutoff.

Pick this track if you want **the most consistently employable** path: firmware, motor control, bring-up, test fixtures, contracting, technician-to-engineer.

PLCs and ISO 10218 are **literacy plus one concrete artifact**, not a full safety-engineer degree.

Do **not** also complete the other two tracks.

## Goals

- Run a real-time loop with a measured period and a watchdog
- Use FreeRTOS (or ESP-IDF tasks) for at least two tasks that cannot starve each other
- Sense current or stall and enter a fault state
- Read one industrial-ish bus **or** produce a bring-up document that a stranger could follow
- Explain functional safety in plain language and show one safety function you implemented

## Mandatory projects

### 1. Timing budget and watchdog

On ESP32 (Arduino-ESP32 or ESP-IDF):

- Control loop at a declared rate (e.g. 200 Hz)
- Log max / mean loop time
- Watchdog reboots or disables motors if the loop overruns or the host dies
- README table: period, measured jitter, what you did when it missed

If you have Module 1 Tier 3, **show the loop on the scope** (a toggling GPIO is enough).

**Hours:** 15–25

### 2. FreeRTOS / ESP-IDF two-task robot

- Task A: motor / PWM
- Task B: sensor or comms
- Prove that a blocking print or a WiFi call cannot stall the motor task (or document that it can, then fix it)
- Idle / run / fault states with a clear fault reason on serial

**Hours:** 20–30

### 3. Current, stall, and a fault that is not a comment in the code

- INA219 / ACS712 / driver current pin / series meter — pick one
- Detect stall or overcurrent
- Cut PWM, require an explicit reset
- Film it

**Hours:** 10–15

### 4. Bring-up packet

A stranger should be able to clone the repo, wire from a diagram, flash, and get the fault demo. Include:

- Schematic or equivalent (KiCad optional; a clean Fritzing-quality diagram is acceptable if pins are real)
- Power budget from Module 2, updated
- Connector / strain-relief note (even if the note is "this zip-tie is the strain relief")
- Flash instructions

**Hours:** 8–12

## Optional projects

- **SimpleFOC** on one hobby BLDC: spin, then current limit. This is the motor-control differentiator.
- **STM32 or Pico** port of the watchdog loop — useful if job ads say STM32
- **CAN**: two nodes, one command, one encoder-ish status (ESP32 TWAI or a cheap CAN hat)
- **KiCad** schematic + fab a simple breakout
- **PLC literacy:** complete one vendor's intro (CODESYS or a cheap Click/Do-more sim) and write one latch + e-stop interlock. Do not pretend you are a controls technician after a weekend.
- **Safety literacy:** read a plain-language guide to ISO 12100 / ISO 10218 / ISO/TS 15066 at "what category/PL means" level. Write one page mapping **your** cutoff to a safety function (and what it is **not**).
- Cable management rebuild of the Module 2 rover so it survives 10 minutes of driving without a disconnected encoder

## Resources

| Resource | Why |
|---|---|
| [ESP-IDF Getting Started](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html) | Tasks, timers, TWAI |
| [FreeRTOS kernel docs](https://www.freertos.org/Documentation/RTOS_book.html) | Real-time vocabulary |
| [SimpleFOC](https://docs.simplefoc.com/) | FOC on-ramp |
| ESP32 TWAI / CAN examples in ESP-IDF | Optional bus lab |
| Manufacturer app notes for your motor driver | Absolute maximum ratings — read them |

## Hardware

You already have an ESP32 and a motor driver. Add, as needed:

| Item | Why |
|---|---|
| Current sensor or driver with IPROPI | Mandatory project 3 |
| Tier 3 scope / logic analyzer from Module 1 | Strongly recommended for this track |
| BLDC + ESC/driver for SimpleFOC | Optional |
| CAN transceiver breakout | Optional |

## Milestones

| Criterion | Required? |
|---|---|
| Measured loop rate + watchdog demo | Mandatory |
| Two-task firmware that isolates the motor loop | Mandatory |
| Overcurrent/stall fault filmed | Mandatory |
| Bring-up packet a stranger could use | Mandatory |
| Scope trace of the loop GPIO | Mandatory if you own a scope |
| FOC, CAN, KiCad, PLC, ISO write-up | Optional |

## What "done" looks like for jobs

Firmware repos with oscilloscope or serial timing plots beat ROS tutorial clones for this track. Apply to mechatronics, test, integration, robotics technician, and embedded intern roles. Functional safety knowledge is scarce; your one-page mapping plus a real cutoff is enough to talk, not enough to sign off a cell.
